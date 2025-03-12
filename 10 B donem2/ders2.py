# koşullu ifadeler

#Şifre kontrolü

# sifre=input("Lütfen şifreniz giriniz :")

# if sifre == "abcd" or sifre == "ABCD" :
#     print("Girilen Şifre Doğrudur. Sisteme Giriş Yapılıyor.")
# else:
#     print("Veriler yanlıştır.")

#bAŞKENT ve ülke

# baskent= input("Başkenti giriniz:")
# ulke = input("ülkeyi giriniz.")

# if baskent == "Ankara" and ulke=="Türkiye":
#     print("Veriler doğrudur.")
# else:
#     print("Veriler Yanlıştır.")

#sayi tahmini

# sayi = int(input("tahmininizi giriniz:"))

# if sayi == 13 :
#     print("Sayı doğru tahmin edildi.")
# elif sayi== 18:
#     print("Tahmin edilen sayı +-5 aralığındadır.")
# else:
#     print("Yanlış Tahmin edildi.")

#sınav notları ve ort hesaplama

# sinav1=float(input("1.Sınav Notunu giriniz:"))
# sinav2=float(input("2.Sınav Notunu giriniz"))
# sinav3=float(input("3.Sınav Notunu giriniz"))

# ortalama= (sinav1+sinav2+sinav3)/3

# print("Sınavların ortalama = ", ortalama)


# if 0< ortalama<50:
#     print("Sonuc Rezalet")
# elif 50<=ortalama<70:
#     print("Sonuc Ortalama")
# elif 70<=ortalama<=84:
#     print("Sonuc İyi")
# else:
#     print(" Sonuc Mükemmel")


    
# range (baslangıc,bitiş,artış)


# for i in range (5):
#     print(i)


# for i in range (1,11):
#     print(i)


# for n in range (1,11,2):
#     print(n)


# for i in range (10,0,-2):
#     print(i)


# meyveler = ["Elma","Armut","Muz","Çilek","ananas"]

# # print(meyveler[0])
# # print(meyveler[1])

# for meyve in meyveler:
#     print(meyve)


# kelime = "Python"

# for HARF in kelime:
#     print(HARF)


# notlar = {"Ali":85,"Veli":90,"Ayşe":78}

# # for isim in notlar:
# #     print(isim)

# # sözlük yani dictionarylerde key-value değerleri ikili olarak aşağıdaki şekilde dögü halinde ekrana yazdırılır.
# for isim,notu in notlar.items():
#     print(f"{isim}: {notu}")




# # Basit ATM uyglaması


# bakiye = 1000

# print(" 10-B SINIFI ATM'YE HOŞ GELDİNİZ.")
# print("1- Bakiye Sorgula\n2- Para Yatırma\n3- Para Çek\n4- Çıkış")

# for i in range(100):
#     secim= input("Lütfen Bir işlem seçin: (1-4)")

#     if secim == "1":
#         print(f" Güncel Bakiyeniz: {bakiye} TL")
    
#     elif secim == "2":
#         miktar=int(input("Yatırmak istediğiniz miktarı giriniz:"))
#         if miktar >0:
#             bakiye = bakiye+miktar
#             print(f"{miktar} TL yatırıldı. Yeni bakiyeniz {bakiye} TL")
#         else:
#             print("GEçersiz Miktar")

#     elif secim == "3":
#         miktar=int(input("çekmek istediğiniz miktarı giriniz:"))
#         if 0<miktar<=bakiye:
#             bakiye -= miktar
#             print(f"{miktar} TL çekildi. Yeni bakiyeniz : {bakiye} TL")

#         else:
#             print("yetersiz Bakiye veya geçersiz miktar ")
    
#     elif secim == "4":
#         print( "Çıkış Yapılıyor ... İyiy günler dileriz.")
#         break

#     else:
#         print(" Geçersiz işlem secildi. Lütfen 1-4 arası bir seçim yapun")




    #WhİLE DONGÜSÜ


    # while kosul:
    #     #koşul doğru oldugu süre boyunca burası çalışır.

    
# sayi=1

# while sayi <= 5:
#     print(sayi)
#     sayi += 1


# sayi2=1

# while sayi2 <=100:
#     print(sayi2)
#     sayi2 += 2

#kullanıcıdan doğru şifre alınana kadar soran kod
# dogruSifre = "1234"
# girilenSifre= ""

# while girilenSifre != dogruSifre:
#     girilenSifre=input("Şifreyi Girin:")

# print ("Şifre doğru giriş yapılıyor..")



# sayi3= 0

# while sayi3<10:
#     sayi3 +=1

#     if sayi3 == 5:
#         continue
#     print(sayi3)



# sayi4= 1

# while sayi4<=10:
#     if sayi4 %2 != 0:
#         sayi4 +=1
#         continue
#     print(sayi4)
#     sayi4 +=1



# while True:
#     sayi= int(input("Bir sayı girin (çıış için 0 a basınız"))
#     if sayi==0:
#         print("Döngü sona erdi")
#         break
#     print(f"Girdiğiniz sayı : {sayi}")



# #Fonksiyonlar


# #basit fonksiyon tanımlaması
# def selamVer():
#     print("Merhaba")


# selamVer()

# #parametre alan fonksiyon 

# def selamla(isim):
#     print(f"Merhaba , {isim}")


# selamla("ahmet")
# selamla("elif")


# #Değer döndüren Fonksiyon

# def topla(a,b):
#     return a+b #toplamı geri döndürür. return sayesinde

# sonuc=topla(10,21)
# sonuc=topla(3,5)
# print("toplam",sonuc)


# #VARSAYILAN DEĞERLİ PARAMETRE KULLANIMI

# def selamla2(isim="Misafir"):
#     print(f"Merhaba,{isim}")

# selamla2()
# selamla2("Ayşe")


# #Birden fazla parametrealanfoksiyon

# def bilgiler(isim,yas,sehir):
#     print(f"isim= {isim}, Yas: {yas}, Yaşadığı şehir: {sehir}")

# bilgiler("Mehmet",25,"Ankara")


# #fonksiyon içinde fonksiyon çağımra

# def kareAl(x):
#     return x*x

# def kupAl(x):
#     return x*kareAl(x)

# print("5'in karesi:",kareAl(5))
# print("5'im küpü:",kupAl(5))



#HESAP MAKİNESİ FONKSİYON ÖRENĞİ

# def topla(a,b):
#     return a+b

# def cikar(a,b):
#     return a-b

# def carp(a,b):
#     return a*b

# def bol(a,b):
#     if b==0:
#         return "Sıfıra Bölünmez"
#     return a/b
 

# while True:
#     print("işlem seç: \n1- Topla\n2- Çıkar\n3- Çarp\n4- Böl")

#     secim=input("Seçiminizi yapın (1-4):")
#     sayi1=float(input("1.SAyıyı girin:"))
#     sayi2=float(input("2.SAyıyı girin:"))



#     if secim=="1":
#         print("Sonuc:",topla(sayi1,sayi2))
#     elif secim=="2":
#         print("Sonuc",cikar(sayi1,sayi2))
#     elif secim=="3":
#         print("Sonuc",carp(sayi1,sayi2))
#     elif secim=="4":
#         print("Sonuc:",bol(sayi1,sayi2))
#     else:
#         print("Geçersiz giriş yapıldı dikkat edin")



# GÖmülü fonksiyonlar 

#print kullanımı: ekrana yazı yazdırmak için kullanılır.
# print("merhaba")

# len kullanımı: Bir dizinin veya stringin uzunlugunu verir.

# metin="Python1233"
# print(len(metin))

#type kullanımı: Bir değişkenin veri tipini döndürür . Örn(str,int,char,double)

# ornek=20
# ornek2=10.23
# ornek3="onbir"


# print(type(ornek))
# print(type(ornek2))
# print(type(ornek3))


#abs kullanımı: Bir sayının mutlak değierni verir

# negatifSayi= -166
# pozitifSayi= 1212312

# print(abs(negatifSayi))
# print(abs(pozitifSayi))


#sum kullanımı : Bir liste veya demet içerisindeki sayıları toplar.

# sayilar13= [10,20,30,40,50,]
# print(sum(sayilar13))


# # math kütüphanesi yada modülü kullanımı ( mataematiksel işlemler için)
# import math

# print(math.sqrt(25))
# print(math.factorial(6))



#random modülü : Rastgele sayı üretmek için kullnaılır.

# import random
# print(random.randint(1,10)) # 1 ile 10 arasında rasgele bir sayi


#datetime Modülü: tarih ve saat bilgisi yazdırı.

# import datetime
# bugun=datetime.date.today()
# print(bugun)

#os modülü (dosya ve diziin işlemleri için kullanılır.)

# import os
# print(os.getcwd()) #geçerli çalışma dizninii göseteri


#örnekler

# def merhaba10b():
#     print("merhsbs dünya")

# merhaba10b()


# def carpma(a,b):
#     return f" Sonuc: {a}x{b}={a*b}"
# print(carpma(6,9))


#lambda Fonksiyonlar

kup = lambda x:x**3
print(f"4ün küpü {kup(4)}")