import sqlite3,re
def create_db():
    conn = sqlite3.connect('sales.db')
    cur = conn.cursor()
    cur.execute('''
 CREATE TABLE IF NOT EXISTS Transactions (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 customer TEXT,
 email TEXT,
 product TEXT,
 quantity INTEGER,
 price FLOAT,
 total FLOAT
 )
 ''')
    conn.commit()
    conn.close()

def add_sale():
 """yangi savdo qo'shuvchi funksiya"""
 while True:
        sales=[]
        ism=input('ismingizni kiriting\n')
        while True:
            email=input('email manzilingizni kiriting\n')
            pattern=r".*\S@\S.*"
            result=re.search(pattern,email) 
            if result:
              break
            else:
                print("emailni noto'g'ri farmatda kiritdingiz")
                continue

        maxsulot=input('maxsulot nomini kiriting\n')    
        while True:
          try:
            miqdor=int(input('nechi dona olmoqchisiz\n'))
            narx=int(input('narxi qancha\n'))
          except:
            print('iltimos son kiriting')      
            continue
          if miqdor>0 and narx>0:
            break
          else:
            print('narxni yoki miqdorini manfiy son kiritdingiz')
            continue

        jami_miqdor=narx*miqdor

        for i in (ism,email,maxsulot,miqdor,narx,jami_miqdor):
            sales.append(i)

        con=sqlite3.connect('sales.db')
        cur=con.cursor()

        cur.execute("insert into Transactions (customer,email,product,quantity,price,total) \
                    values(?,?,?,?,?,?)",sales)
        con.commit()
        con.close()
        print(f"{ism} uchun savdo muvaffaqiyatli qo'shildim.Jami savdo-{jami_miqdor}") 

        savol=input('yana savdo qilasizmi.ha/yoq\n')

        if savol=='yoq':
           break



def statistika():
    """statistikani ko'rsatuvchi funksiya"""
    con = sqlite3.connect("sales.db")
    cur = con.cursor()

    cur.execute("SELECT COUNT(*) FROM Transactions")
    umumiy_savdo = cur.fetchone()[0]

    cur.execute("SELECT SUM(total) FROM Transactions")
    umumiy_tushum = cur.fetchone()[0]

    cur.execute("SELECT AVG(total) FROM Transactions")
    ortacha_buyurtma = cur.fetchone()[0]

    cur.execute("""
        SELECT customer, SUM(total) 
        FROM Transactions 
        GROUP BY customer 
        ORDER BY SUM(total) DESC 
        LIMIT 1
    """)
    eng_faol_mijoz = cur.fetchone()

    if eng_faol_mijoz:
        mijoz, tolov = eng_faol_mijoz
    else:
        mijoz, tolov = "Yo‘q", 0

    cur.execute("""
        SELECT product, COUNT(*) 
        FROM Transactions 
        GROUP BY product 
        ORDER BY COUNT(*) DESC 
        LIMIT 1
    """)
    eng_mashhur = cur.fetchone()

    if eng_mashhur:
        maxsulot, dona = eng_mashhur
    else:
        maxsulot, dona = "Yo‘q", 0

    print(f"""
Umumiy savdo: {umumiy_savdo}
Umumiy tushum: {umumiy_tushum}
O‘rtacha buyurtma: {ortacha_buyurtma}
Eng faol mijoz: {mijoz} ({tolov})
Eng mashhur mahsulot: {maxsulot} ({dona} dona)
""")

    con.close()


def mijoz_qidirish():
    """mijoz nomi orqali qidirish"""
    ism = input('qidirilayotgan mijoz ismini kiriting: ')
    con = sqlite3.connect("sales.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM Transactions WHERE customer=?", (ism,))
    mijozlar = cur.fetchall()

    umumiy_sarf = 0

    if mijozlar:
        print(f"\n{ism} natijalari:")
        for i in mijozlar:
            maxsulot = i[3]
            dona = i[4]
            tolov = i[6]
            umumiy_sarf += tolov
            print(f"{maxsulot} - {dona} dona - {tolov}")

        print(f"Jami sarf: {umumiy_sarf}")
    else:
        print("Bunday mijoz mavjud emas")

    con.close()


def chiqish():
    """dastur yakunida hisobotni faylga saqlab dasturni tugatuvchi funksiya"""
    con = sqlite3.connect("sales.db")
    cur = con.cursor()

    cur.execute("SELECT COUNT(*) FROM Transactions")
    umumiy_savdo = cur.fetchone()[0]

    cur.execute("SELECT SUM(total) FROM Transactions")
    umumiy_tushum = cur.fetchone()[0]

    cur.execute("""
        SELECT customer, SUM(total) 
        FROM Transactions 
        GROUP BY customer 
        ORDER BY SUM(total) DESC 
        LIMIT 1
    """)
    eng_faol = cur.fetchone()

    if eng_faol:
        mijoz, tolov = eng_faol
    else:
        mijoz, tolov = "Yo‘q", 0

    cur.execute("SELECT date('now')")
    sana = cur.fetchone()[0]

    line = "Sales Report - DataNova\n"
    line += f"Sana: {sana}\n"
    line += f"Umumiy savdo: {umumiy_savdo}\n"
    line += f"Umumiy tushum: {umumiy_tushum}\n"
    line += f"Eng faol mijoz: {mijoz} - {tolov}\n"

    with open("report.txt", "a") as f:
        f.write(line + "\n")

    print("Hisobot saqlandi. Hayr")
    con.close()

   


def main():
 create_db()
 while True:
  print("\n==== DataNova Sales Tracker ====")
  print("1. Yangi savdo qo‘shish")
  print("2. Statistikani ko‘rish")
  print("3. Mijozni qidirish")
  print("4. Chiqish")
  choice = input("Tanlang (1-4): ")
  if choice == '1':
    add_sale()
  elif choice == '2':
    statistika()
  elif choice == '3':
     mijoz_qidirish()
  elif choice == '4':
    chiqish()
    break
  else:
    print("❌ Noto‘g‘ri tanlov, qayta urinib ko‘ring.")

  savol=input("Yana amaliyot bajarasizmi.ha\yoq")

  if savol=='yoq':
     
     break  
     

print("assalomu alaykum.Hush kelibsiz")
main()