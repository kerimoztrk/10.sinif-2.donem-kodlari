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
#     print(sayi**2)
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

# kup = lambda x:x**3
# print(f"4ün küpü {kup(4)}")


# 2.dönem 1. sınav sonu



# Tarih ve string metin işlemleri

#pythonda  tarih saaat bilgileri ile çalımak için datetime modulü kullanılır.


#Tarih ve saat bilgisi alma

import datetime

# simdi=datetime.datetime.now()

# print("Şuanki tarih ve saat:",simdi)


#datetime.datetime.now() fonksiyonu, sistemin o anki tarih ve saat bilgisini döndürür.


#Belirli bir Tarih tanımlama


# tarih=datetime.datetime(2015,3,15,14,30)

# print("Tanımlanan tarih ve saat: ", tarih)


#String (Metin) olarak girilen değerlerin tarih bilgisinin biçimlendirilmesi

#Tarihi metinden dönültürme(strpTime())

#Bir metin(string) olarak girilen tarih, strptime() fonksiyonu ile datetime nesnesine dönüştürülebilir.

# tarih_metin="11/03/2024 13:56"

# tarih_nesnesi= datetime.datetime.strptime(tarih_metin,"%d/%m/%Y %H:%M")

# print("Donuşstürülen değer:",tarih_nesnesi)


#  %d   ifadesi Gün değerini ifade eder

#  %m  ifadesi Ay değerini ifade eder

#  %Y  ifadesi Yıl değerini ifade eder

#  %H  ifadesi Saat değerini ifade eder

#  %M   ifadesi Dakika değerini ifade eder.


#Tarihi metin olarak formatlama (strftime)

#bir datetime nesnesini metibsel olarak belirli bir formatta yazırdırmak iöçin kullanılır.


# simdi2=datetime.datetime.now()

# tarih_metinsel=simdi2.strftime("%d %B %Y , %A")

# print("biçimlendirilmiş tarih",tarih_metinsel)

#  %d   ifadesi Gün değerini ifade eder

#  %B   ifadesi ayın adını ifade eder

#  %Y  ifadesi Yıl değerini ifade eder

#  %A  ifadesi günün adını verir ( Salı ) gibi


# String verileri Birleştirme

#+ operatörü .format() ve f-string yontemi kllanılır.



#1 Birleştirme örenği + kullnaarak

# ad= "Elif"
# soyad="Öztürk"

# tamAd= ad + " " + soyad

# print(tamAd)

#f-string yöntemi 

# ad1="Mert"
# yas=18

# print(f"{ad1} adlı kişi {yas} yaşındadır.")


#.format() yöntemi ile birleştirme

# okul= "Yazılım Lisesi"
# sehir= "İstanbul"

# print(" Okul : {}, Şehir :{}".format(okul,sehir))



#String veri içerisindeki bir karaktere erişme

# isim = "Ayşe"
 
# print(isim[0])  # 'A'

# print(isim[2])  # 'ş'


# Sondan erişim(negatif indeks(dizin) )

# isim2="Kemal"

# print(isim2[-1])

# print(isim2[-3])

## örnek

# email= "213124@gmail.com" 

# if "@" in email:
#     print("Geçerli Bir eposta adresi girildi")
# else:
#     print("geçersiz eposta")


# isim="Fırat"
# soyadı="küçük"

# tamAd=isim+" "+soyadı
# print("Tam Ad: ",tamAd)

# ilkHarf=isim[0]
# print("Adının ilk harfi:",ilkHarf)

# ogrenciEtiketi=f"{ilkHarf}.{soyadı}"
# print("Etiket:",ogrenciEtiketi)


#Strin verinin uzunlugu

# Bir string ifadenin uzunlugu yani kaç karakterden oluştuğunu öğrenmek için len() fonksiyonunu kullanıyoruz


# mesaj= "Merhaba Dünya "

# uzunluk= len(mesaj)

# print("Mesaj Uzunluğu =", uzunluk)



#sTring Veriyi Paraçamala (slice) ve bölne(split)


#bir stringin belirli kısmını almak için kullanılır : metin[başlangıç:Bitiş]


# metin="Python programlama"

# parca=metin[0:6]

# print(parca)


# #Split(Bölme)

# #Belirli ayırıcılara göre parçalara ayırmak için split kullanılır   split("ayırıxı")


# ad_Soyad="Ali.Veli.Demir"

# liste=ad_Soyad.split(".") #Nokta ifadadelerine göre ayırır.

# print(liste)


# #String veri içinde kararkter değiştirme, ekleme ,ve çıkarm


# #replace() metodu karakter değiştirme işlemine yarar

# # metin2="Merhaba Dunya"

# # metin2=metin2.replace("u","ü")

# # print(metin2)

# #replace( ) ifadesi ile bir karakter veya kelime başka bir şeyle yer değiştirebilir.


# #karakter ekleme 

# #stringler değiştirelemez old için yeni bir string oluşturarark ifade eklenir.

# kelime="Kitap"

# kelime=kelime+"lık"  #kitaplık

# print(kelime)



#karakter çıkarma 

# metin3="2023-10-29"

# yeniMetin=metin3.replace("-","")

# print(yeniMetin)



#Senaryo Kullanıcıdan alınan ad soyad bilgisini işleyip temizleme

#uzunluk ölçümü
#ismini ve soyisimni ayırma
#küçük hharfle yazılmış olan soyadını büyük harfe çevire
#gereksiz boşluk dtemizleme




# veri="   Ayşe Yıldız  "

# veri=veri.strip() #baştaki ve sondaki boşlukları temizleme

# print("Uzunluk:",len(veri))

# #bölme örneği

# ad,soyad=veri.split()
# soyad=soyad.upper() #büyük harfe çevirir.

# print(f"Ad:{ad},  Soyad:{soyad}")





# String veri içinde Bir karakterin yerini veya 
# metnin karakteri içerip içermedğini bulma    KONU


# metin="Python programlama"

# print(" ython " in metin)

# print("java" in metin)

# in operatörü ile bir kelime yada karakterin string içinde olup olmadığını hzılıca kontrol ediyoruz.



#find() metodu -  Bir karakterin Yerini bulmak


# metin2="Merhaba Dünya"

# print(metin2.find("a"))
# print(metin2.find("z"))
# print(metin2.find("x"))


#ornek


# email=input("Eposta adresi giriniz:")

# if "@" in email:
#     print("Geçerli bir eposta adresi girdiniz.")
# else:
#     print("Geçersiz bir eposta girdiniz içerisinde @ karakteri yoktur.")



#String ver ile büyük ve küçük harf değişimi Yapma

#lower() fonksiyonu = tüm harfleri küçük yapmaya yarar.


# metin3= "Python ÖĞreniyorum"

# kucuk= metin3.lower()

# print(kucuk)


# #upper()  fonsiyonu - Tüm harfleri büyük harfle yazar.

# metin4= " nazmi şen"
# buyuk=metin4.upper()

# print(buyuk)


#örnek kullanıcadan gelen veriyi standartlaştırma

# sehir= input("Lütfen ŞEhrin adını giriniz:")
# sehir=sehir.upper()
# print(f"Kayıt edilen şehrin adı: {sehir}")



# email=input("Eposta adresi giriniz:")
# sehir= input("Yaşadığınız şehri giriniz:")


# #epostayı kontrol et @ ifadesi varmı ykmu
# if "@" in email:
#     print("Geçerli bir eposta adresi girdiniz.")
# else:
#     print("Geçersiz bir eposta girdiniz içerisinde @ karakteri yoktur.")

# index=email.find("@")

# if index != -1:
#     print(f"'@' karakteri {index}. sırada yer alıyor.")

# else:
#     print("Eposta içerisinde '@' ifadesi bulunamadı.")

# sehir_buyuk=sehir.upper()
# print(f"Kayıt edilen şehir adı : {sehir_buyuk}")


#HATA YAKALAMA İŞLEMLERİ


#Hata kavramı ve hata türleri



#Hata nedir ?

#Pythonda program çalışırken oluşan  beklenmedik sorunlara hata (error) denir.
#Hatalar, programın durmasına vehya çalışmasına neden olabilir.
#
# Bazı hatalar program yazılıreken (söz dizimi yani  syntax hataları) , bazıları ise çalışırken çalışma zamanı hataları) olabilir.


#hata Türleri

# 1.hATA ( SYNTAXeRRO))- yAZIM hATASI == KODLAMA KURALLARINA UYULMAZSA OLUŞUR

#PARANTEZİN EKSİK OLMASI SYNTAX HATASI MEYDANA GETİRİR.

# print("MRHABA DÜNYA"


#2. HATA Türü (Name Error)- Tanımsız değişken
#Bu hata türü tanımlanmamış bir değişkene erişilmek istenirse meydana gelir.


# print(sayi32)

# 3.hata Türü TypeError- Tip hatası = Uyumsuz veri tipleriyle işlem yapılırsa olulşur.

# print("Yaşınız :"+25) #Typeerror : str ile int toplanmaz dolayısıyla runtime hatası verir.

# Value Error - Geçersiz değeer
#uygun veri tipinde ancak geçersiz bir değer verilirse oluşur.

# sayi=int("on") #valueError : "on" metnini sayıya dönüştürremez.


# # ZeroDivisionError - Sıfıra bölme hatasıı

# print(19/0)


try:
    a=int (input("Birinci Sayıyı giriniz:"))
    b=int (input("ikinci Sayıyı giriniz:"))

    sonuc=a/b
    print("Sonuc: ",sonuc)

except ValueError:
    print("Lütfen sadece sayısal değer girn")
except ZeroDivisionError:
    print("Bir sayı sıfıra bölünemez")
except Exception as e:
    print("Beklenmyen bir hata meydana geldi")


#try: Hata oluşabilecek kodların yazıldığı blok.

#except Hata olışursa devreye giren blok.

#valueError: Sayıya dönüştürülmeyen girişler için hata .

#ZeroDivisionError: 0 bölme hatası sayı sıfıra bölünemez.

#exception: Diğer tüm beklenmeten hatalar için genel blok.

try: 
    adet=int(input("Kaç adet ürün aldınız:"))
    fiyat=int(input("Fiyatını giriniz"))

    if fiyat<=0:
        raise ValueError("Ürüm fiyatı 0 dan küçük olamaz")
    
    toplam=adet*fiyat
    print(f"Toplam Tutar : {toplam} TL")

except ValueError as hata :
    print("Hatalı giriş",hata)

except Exception as e:
    print("Beklenmeyen bir hata oluştu",e)


#raise ValueError : Bizim manuel olarak hata fırlatmamıza yarar.