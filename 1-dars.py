# # 1- masala
# # Mehmonlar soni kiriting.
# # < 50 → "Kichik to‘y", 50–200 → "O‘rtacha to‘y", 200+ → "Katta to‘y"
# try:
#  mehmonlar_soni=int(input('Mehmonlar sonini kiriting\n'))
#  if mehmonlar_soni<=50:
#      print('Kichik toy')
#  elif mehmonlar_soni>50 and mehmonlar_soni<=200:
#      print('O\'rtacha to\'y')
#  else:
#      print('Katta to\'y')
# except ValueError:
#     print('faqat son kiriting.Masalan : 20,30,34')
    
# # 2-masala
# # Foydalanuvchidan uning roli haqida so‘rang (admin, premium, guest).
# # •	Agar admin bo‘lsa: "Xush kelibsiz, Administrator!" chiqsin.
# # •	Agar premium bo‘lsa: "Xush kelibsiz, Premium foydalanuvchi!".
# # •	Aks holda: "Xush kelibsiz, Mehmon!".


# rol=input('Ro\'lingiz qanaqa: Admin ,premium yoki guest\n').title()
# if rol=='Admin':
#     print('Xush kelibsiz, administrator')
# elif rol=='Premium':
#     print('xush kelibsiz, Premium foydalanuvchi')
# elif rol=='Guest':
#     print('Xush kelibsiz, Mexmon')
# else:
#     print('Iltimos ko\'rsatilganlarini kiriting: Admin,premium va guesst')
    
# # 3-masala
# # •	Foydalanuvchi nomini ("admin") va parolni ("1234") saqlang.
# # •	Foydalanuvchidan ikkalasini ham so‘rang.
# # •	Agar to‘g‘ri bo‘lsa → "Xush kelibsiz!" chiqsin.
# # •	Aks holda → "Login yoki parol xato" chiqsin.


# nomi='admin'
# parol='1234'
# roli=input('Ro\'lingiz qanday\n')
# parolingiz=input('parolingizni kiriting:\t')
# if roli==nomi and parolingiz==parol:
#     print('Xush kelibsiz')
# else:
#     print('Login yoki parol xato') 

# # 4-misol
# # •	Haroratni so‘rang.
# # •	0 dan past → "Kurtka kiying", 0–20 → "Sviter kiying", 20+ → "Futbolka kifoya".

# try:
#     harorat=float(input('harorat nechi gradus\n'))
#     if harorat<=0:
#         print('kurtka kiying')
#     elif harorat>0 and harorat<=20:
#         print('svitir kiying')
#     else:
#         print('koylak  kiying')
# except:
#     print('iltimos raqam kiriting.Masalan;20.2,20,54')

# # 5-masala
# # Ombordagi mahsulot soni (stock_quantity) va foydalanuvchining xohlagan miqdori (desired_quantity)ni so‘rang.
# # •	Agar xohlangan son ombordagidan kam yoki teng bo‘lsa → "Buyurtma qabul qilindi".
# # •	Aks holda → "Kechirasiz, faqat X dona mahsulot bor" (X o‘rniga haqiqiy son chiqsin).

# maxsulot_soni=5400
# try:
#     buyurtma_soni=int(input('qancha buyurtma qilmoqchisiz\n'))
#     if buyurtma_soni<=maxsulot_soni:
#         print('Buyurtma qabul qilindi')
#     else:
#         print(f"Kechirasiz, faqat {buyurtma_soni} dona mahsulot bor")
# except:
#     print('Iltimos son kiriting.Misol uchun:20,65,115')

# # 6-masala
# # Foydalanuvchidan yoshini so‘rang va quyidagi qoidalarga asosan chipta narxini chiqaring:
# # •	Agar yosh 6 dan kichik bo‘lsa → "Bepul"
# # •	Agar yosh 6 dan 17 gacha bo‘lsa → 15000 so‘m
# # •	Agar yosh 18 dan 59 gacha bo‘lsa → 25000 so‘m
# # •	Agar yosh 60 va undan katta bo‘lsa → 12000 so‘m

# try:
#     yosh=int(input('yoshingiz nechida\n'))
#     if yosh<=6:
#         print('sizga kirish beepul')
#     elif yosh>6  and yosh<=17:
#         print('sizga kirish: 17 000 so\'m')
#     elif yosh>17 and yosh<=59:
#         print('sizga kirish:25 000 so\'m')
#     else:
#         print('sizga kirish:12 000 so\'m')
# except:
#     print('iltimos son kiriting.Masalan:54,21,36')
    
# # 7-masala
# # Tasavvur qiling, siz kompyuter o‘yinida jang qilyapsiz. Sizning sog‘lig‘ingiz (player_health) va dushman zarba kuchi (enemy_attack_power) mavjud.
# # Foydalanuvchi quyidagilarni kiritsin:
# # 1.	player_health – o‘yinchi sog‘ligi (masalan: 50).
# # 2.	enemy_attack_power – dushmanning zarba kuchi (masalan: 40).
# # 3.	armor – o‘yinchi zirhi (zarbani kamaytiradi).
# # Shartlar:
# # •	Avval dushman zarbasidan keyingi yangi sog‘likni hisoblang:
# # •	yangi_health = player_health - (enemy_attack_power - armor)
# # •	Agar yangi_health <= 0 → "❌ O‘yin tugadi! Siz mag‘lub bo‘ldingiz."
# # •	Agar yangi_health < 20 → "⚠️ Siz og‘ir jarohatlandingiz! Shifobaxsh ichimlik izlang."
# # •	Agar yangi_health >= 20 → "💪 Siz jangni davom ettiryapsiz!"

# try:
#     player_health=int(input('avataringizning jonini kiriting\n'))
#     enemy_attack_power=int(input('dushman zarba kuchini kiriting\n'))
#     armor=int(input('zirxingiz kuchini kiriting\n')) 
#     yanngi_soglik=player_health-(enemy_attack_power-armor)
#     if yanngi_soglik<=0:
#         print('o\'yin tugadi')
#     elif yanngi_soglik<20:
#         print('Siz og‘ir jarohatlandingiz! Shifobaxsh ichimlik izlang.')
#     else:
#         print('Siz jangni davom ettiryapsiz!')
# except:
#     print('iltimos son kiriting.Masalan:54,21,36')
    
# # 8-masala
# # Yangi karta olganingizda parol o’rnatib olishingiz kerak bo’ladi.
# # ATM (Bankomat) uchun shu jarayonni bajaradigan dastur yozing. Odatda default parol “0000” bo’ladi.
        
# parol=0000
# try:
#  eski_pin=int(input('Eski pinni kiriting\n'))
#  if eski_pin==parol:
#     yangi_parol=int(input('Yangi parol kiriting\n'))
#     Takrorlang=int(input('parolni takrorlang'))
#     if yangi_parol==Takrorlang:
#      parol=yangi_parol
#      print('parol yangilandi')
#     else:
#         print('takroriy parolingiz yangi parolga mos kelmadi')
#  else:
#     print('noto\'g\'ri parol kiritdingiz.')
# except:
#     print('Iltimos raqam kiriting.')
# print(parol)

# # 9-masala
# # foydalanuvchini kafega xush kelibsiz deb kutib oladi.
# # 2.	Menyuni chiqaradi (choy = 5000 so‘m, qahva = 8000 so‘m, sharbat = 10000 so‘m).
# # 3.	Foydalanuvchidan nima buyurtma qilmoqchi ekanini so‘raydi.
# # 4.	Nechta stakan olishini so‘raydi.
# # 5.	Umumiy narxni hisoblaydi.
# # 6.	Agar foydalanuvchi 3 tadan ko‘p buyurtma qilsa, "10% chegirma" beradi.
# # 7.	Yakuniy hisobni va buyurtma tafsilotlarini chiqaradi.

# try:
#     print('Assalomu alaykum,Xush kelibsiz')
#     print('''Menyu:
#             Choy=5000 so'm 
#             qahva=8000 so'm
#             sharbat=1000''')
#     buyurtma=input('Nima buyurtma qilasiz.\nChoy,Qahva va sharbat\n').lower()
#     soni=int(input('Qancha olasiz.Nechi stakan\n'))
#     if buyurtma=='choy':
#         choy=5_000
#         umumiy_tolov=choy*soni
#         print(f'Umumiy to\'lov:{umumiy_tolov}')
#         if soni>3:
#             chegirmali_qiymat=umumiy_tolov-umumiy_tolov*0.1
#             print(f'chegirmali to\'lov:{chegirmali_qiymat}')
#     elif buyurtma=='qahva':
#         qahva=8_000
#         umumiy_tolov=qahva*soni
#         print(f'umumiy to\'lov:{umumiy_tolov}')
#         if soni>3:
#             chegirmali_qiymat=umumiy_tolov-umumiy_tolov*0.1
#             print(f'chegirmali to\'lov:{chegirmali_qiymat}')
#     elif buyurtma=='sharbat':
#         sharbat=10_000
#         umumiy_tolov=sharbat*soni
#         print(f'umumiy to\'lov:{umumiy_tolov}')
#         if soni>3:
#             chegirmali_qiymat=umumiy_tolov-umumiy_tolov*0.1
#             print(f'chigirmali to\'lov:{chegirmali_qiymat}')
#     else:
#         print('Menuda bunday ichimlik yoq')
# except:
#     print('Iltimos son kiriting')

# # 10-masala
# # random modulidan foydalanib, foydalanuvchiga tasodifiy ikkita son va tasodifiy arifmetik amal (+, -, *, //) bilan savol chiqaring.
# # Quyidagi talablarga javob beradigan dastur yarating:
# # 1.	Foydalanuvchidan amalni tanlashni so‘rang: +, , , yoki //.
# # 2.	Kompyuter tasodifiy ikkita son (1 dan 10 gacha) tanlasin.
# # 3.	Shu sonlar va amal asosida savol chiqaring (masalan: 7 * 3 = ?).
# # 4.	Foydalanuvchi javob kiritsin.
# # 5.	Agar foydalanuvchi to‘g‘ri javob bersa "✅ To‘g‘ri!" chiqaring, aks holda "❌ Xato! To‘g‘ri javob: ..."deb ko‘rsating.
# # 6.	Agar foydalanuvchi amalni noto‘g‘ri kiritgan bo‘lsa, "❌ Noto‘g‘ri amal kiritdingiz!" deb chiqaring va dasturni to‘xtating.


# import random as r 
# a=r.randint(1,10)
# b=r.randint(1,10)
# try:
#     amal=input('matematik amal kiriting.Masalan +,-,*,/,//\n')
#     if amal=='+':
#         print('masalani bajaring')
#         savol=int(input(f'{a}+{b}\n'))
#         c=a+b
#         if savol==c:
#             print('Javobing to\'g\'ri')
#         else:
#             print(f'javobing xato.to\'g\'ri javob:{c}')
#     elif amal=='-':
#         print('Matematik masalani bajaring')
#         savol=int(input(f'{a}-{b}\n'))
#         c=a-b
#         if savol==c:
#             print('Javobing to\'g\'ri')
#         else:
#             print(f'noto\'g\'ri javob.to\'g\'ri javob:{c}')
#     elif amal=='*':
#         print('Matematik masalani bajaring')
#         savol=int(input(f'{a}*{b}\n'))
#         c=a*b
#         if savol==c:
# #             print('Javobing to\'g\'ri')
# #         else:
# #             print(f'noto\'g\'ri javob.to\'g\'ri javob:{c}')
# #     elif amal=='/':
# #         print('Matematik masalani bajaring')
# #         savol=int(input(f'{a}/{b}\n'))
# #         c=a/b
# #         if savol==c:
# #             print('Javobing to\'g\'ri')
# #         else:
# #             print(f'noto\'g\'ri javob.to\'g\'ri javob:{c}')
# #     elif amal=='//':
# #         print('Matematik masalani bajaring')
# #         savol=int(input(f'{a}//{b}\n'))
# #         c=a//b
# #         if savol==c:
# #             print('Javobing to\'g\'ri')
# #         else:
# #             print(f'noto\'g\'ri javob.to\'g\'ri javob:{c}')
# #     else:
# #         print('❌ Noto‘g‘ri amal kiritdingiz!')
# # except:
# #     print('Iltimos raqam kiriting')
# # print(a,b)

# # # 11-masala
# # # Oddiy bankomat dasturi tuzing.
# # # Unda quyidagi amallar bo‘lishi kerak:
# # # 1.	Balansni tekshirish
# # # 2.	Pul qo‘yish (deposit)
# # # 3.	Pul yechish (withdraw)
# # # 4.	PIN kodni o‘zgartirish
# # # 5.	Chiqish

# parol=1454
# balans=10_000_000
# try:
#     porolni_kiriting=int(input('parolni kiriting\n'))
#     if parol==porolni_kiriting:
#         print(""" 1-Balansni tekshirish
#     2-Pul qo‘yish (deposit)
#     3-Pul yechish (withdraw)
#     4-PIN kodni o‘zgartirish
#     5-Chiqish""")
#         amaliyot=int(input('amaliyotni tanlang\n'))
#         if amaliyot==1:
#             print(f'Balansingizda {balans} so\'m bor')
#         elif amaliyot==2:
#          print('''Depozitga pul qo\'yish.
#                     7-oygacha 2 %
#                     7 oydan 13 oygacha 5 %
#                     13 oydan 36 oygacha 20 %.Murakkab foiz''')
#         qiymat=int(input('Qancha pul qo\'ymoqchisiz\n'))
#         muddat=int(input('necha oyga qo\'ymoqchisiz\n'))
#         if muddat<=6:
#             foiz=0.02
#             maturity=qiymat+qiymat*foiz*muddat
#             print(f"sizning omonatingiz {maturity} so\'m bo\'ladi")
#         elif muddat>6 and muddat<=12:
#             foiz=0.05
#             maturity=qiymat+qiymat*foiz*muddat
#             print(f"sizning omanatingiz {maturity} so\'m bo'ladi")
#         elif muddat>12 and muddat<=36:
#                 foiz=0.2
#                 n=12
#                 yillik=muddat/n
#                 t=n*yillik
#                 maturity=qiymat*(1+foiz/n)**t
#                 print(f'sizning omanatingiz {maturity} so\'m bo\'ladi')
#         elif amaliyot==3:
#             print('Pul naxtlashda kamissiya bor 0.5 %')
#             summa=float(input('Qancha pul olmoqchisiz\n'))
#             foizi=summa/100*0.5
#             if balans-summa-foizi>0:
#                 print('amaliyot amalga oshirsa bo\'ladi')
#             else:
#                 print('amaliyotni amalga oshirib bo\'lmaydi')
#         elif amaliyot==4:
#             yangi_kod=int(input('yangi kodni kiriting'))
#             takrorla=int(input('kodni takrorlang'))
#             if yangi_kod==takrorla:
#                parol=yangi_kod
#                print('amaliyot muvofaqiyatli bajarildi')
#                print(parol)
#             else:
#                  print(f'takroriy kod xato kiritildi.Amaliyotni boshidan boshlang')
#         elif amaliyot==5:
#             print('chiqish')
#         else:
#             print('Mavjud bo\'lmagan amalyotni tanladingiz.Mavjud amaliyotlardan foydalaning')
#     else:
#         print('parol noto\'g\'ri')   
# except:
#     print("iltimos raqam kiriting")
         
        

player_health=int(input('avataringizning jonini kiriting\n'))
enemy_attack_power=int(input('dushman zarba kuchini kiriting\n'))
armor=int(input('zirxingiz kuchini kiriting\n')) 
yanngi_soglik=player_health-(enemy_attack_power-armor)
if yanngi_soglik<=0:
    print('o\'yin tugadi')
elif yanngi_soglik<20:
    print('Siz og‘ir jarohatlandingiz! Shifobaxsh ichimlik izlang.')
else:
    print('Siz jangni davom ettiryapsiz!')

print('iltimos son kiriting.Masalan:54,21,36')
    
    









