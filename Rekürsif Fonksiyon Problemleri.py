# 1. Faktöriyel Hesaplama Fonksiyonu: Bir sayının faktöriyelini hesaplayan özyinemeli bir fonksiyon yazın.
'''
def fak(sayi,toplam=1):
    if sayi >= 1:
        toplam *= sayi
        return fak(sayi-1,toplam)
    return toplam

sayi = int(input("Sayı giriniz:"))
print("Sayının faktöriyeli:",fak(sayi))
'''
# 2. Fibonacci Serisi Hesaplama Fonksiyonu: Fibonacci serisinin n'inci elemanını hesaplayan özyinemeli bir fonksiyon yazın.
'''
def Fibonacci(n, eleman1=0, eleman2=1, fibonacci=[0, 1]):
    if n > 2:
        yeni_eleman = eleman1 + eleman2
        fibonacci.append(yeni_eleman)
        return Fibonacci(n - 1, eleman2, yeni_eleman, fibonacci)
    return fibonacci

sayi = int(input("N değeri giriniz: "))
print(Fibonacci(sayi))
'''
# 3. Üs Alma Fonksiyonu: Bir sayının üssünü hesaplayan özyinemeli bir fonksiyon yazın.
'''
def üsalma(x,sayi,toplam=1):
    if x > 0:
        toplam *= sayi
        return üsalma(x-1,sayi,toplam)
    return toplam

n = int(input("Sayı giriniz:"))
üs = int(input("Üs giriniz:"))
print(f"{n} nin {üs}. üssü = {üsalma(üs,n)}")
'''
# 4. Dizi Elemanlarının Toplamını Hesaplama Fonksiyonu: Bir dizi içindeki elemanların toplamını hesaplayan özyinemeli bir fonksiyon yazın.
'''
def dizitopla(liste,toplam=0,n=0):
    if n < len(liste):
        toplam += liste[n]
        return dizitopla(liste,toplam,n+1)
    return toplam

sayilar=[]
boyut=int(input("Boyut giriniz:"))
for i in range(boyut):
    sayi = int(input("Sayı giriniz:"))
    sayilar.append(sayi)

print(sayilar)
print("Listenin toplamı:", dizitopla(sayilar))
'''
# 5. Palindrom Kontrolü Fonksiyonu: Verilen bir string'in palindrom olup olmadığını kontrol eden özyinemeli bir fonksiyon yazın. (Palindrom, tersten okunduğunda aynı olan bir kelime, kelime grubu veya cümledir. )
'''
def palindrom(metin,ters_metin="",indeks=-1):
    if len(metin) != len(ters_metin):
        ters_metin += metin[indeks]
        return palindrom(metin,ters_metin,indeks-1)
    else:
        if metin == ters_metin:
            return ("String palindromdur.")
        else:
            return ("String Palindrom değildir.")

metin = input("Metin giriniz:")
print(palindrom(metin))
 '''         
# 6. En Büyük Ortak Bölen (GCD) Hesaplama Fonksiyonu: İki sayının en büyük ortak bölenini hesaplayan özyinemeli bir fonksiyon yazın.
'''
def ebob(sayi1, sayi2, bölen=1, en_büyük=None):
    if sayi1 < sayi2:
        sayi1, sayi2 = sayi2, sayi1

    if bölen <= sayi1:
        if sayi1 % bölen == 0 and sayi2 % bölen == 0:
            en_büyük = bölen
        return ebob(sayi1, sayi2, bölen + 1, en_büyük)

    return en_büyük

x = int(input("1. sayıyı giriniz: "))
y = int(input("2. sayıyı giriniz: "))

print(ebob(x, y))
'''
# 7. Eleman Sayısını Bulma Fonksiyonu: Bir dizinin eleman sayısını hesaplayan özyinemeli bir fonksiyon yazın.
'''
def elemansayi(liste,sayac=0):
    if sayac != len(liste):
        return elemansayi(liste,sayac+1)
    return sayac

sayilar =[1,2,3,4,5,6,7,8,9,0]

print(elemansayi(sayilar))
'''
# 8. Dizi Elemanlarını Ters Çevirme Fonksiyonu: Bir dizinin elemanlarını ters çeviren özyinemeli bir fonksiyon yazın.
'''
def diziterscevir(liste,yeniliste=[],indeks=-1):
    if len(liste) != len(yeniliste):
        yeniliste.append(liste[indeks])
        return diziterscevir(liste,yeniliste,indeks-1)
    print(liste)
    return yeniliste
    
sayilar=[1,2,3,4,5,6,7,8,9,0]

print(diziterscevir(sayilar))
'''
# 9. Dizi Elemanlarını Sıralama Fonksiyonu: Bir diziyi sıralayan özyinemeli bir sıralama algoritması fonksiyonu yazın.
'''
def dizisırala(liste, indeks1=0, indeks2=1):
    if indeks1 < len(liste) - 1:
        if indeks2 < len(liste):
            if liste[indeks1] > liste[indeks2]:
                liste[indeks2], liste[indeks1] = liste[indeks1], liste[indeks2]
            return dizisırala(liste, indeks1, indeks2 + 1)
        else:
            return dizisırala(liste, indeks1 + 1, indeks1 + 2)
    return liste

sayilar = [2, 6, 4, 8, 3, 7, 9, 0]

print(dizisırala(sayilar))
'''
# 10. Dizi Elemanlarını Birleştirme Fonksiyonu: İki diziyi birleştiren özyinemeli bir fonksiyon yazın.
'''
def dizibirlestir(liste1,liste2,sayac=0):
    if len(liste1)+len(liste2) != len(liste1)+sayac:
        liste1.append(liste2[sayac])
        return dizibirlestir(liste1,liste2,sayac+1)
    return liste1

x=[1,2,3,4,5]
y=['a','b','c','d','e']

print(dizibirlestir(x,y))
'''
# 11. Dizi Elemanlarını Filtreleme Fonksiyonu: Bir dizi içinde belirli bir kriteri sağlayan elemanları filtreleyen özyinemeli bir fonksiyon yazın.
'''
#Kriter= Verilen dizideki 10 dan küçük sayılar ile yeni bir liste oluşturulacak.
def dizifiltrele(liste,yeniliste=[],x=10,sayac=0):
    if sayac < len(liste):
        if liste[sayac]<x:
            yeniliste.append(liste[sayac])
        return dizifiltrele(liste,yeniliste,x,sayac+1)
    return yeniliste

sayilar=[10,4,13,45,23,76,7,8,43,78,9,0]

print(dizifiltrele(sayilar))
'''
# 12. Dizi Elemanlarının Ortalamasını Hesaplama Fonksiyonu: Bir dizinin elemanlarının ortalamasını hesaplayan özyinemeli bir fonksiyon yazın.
'''
def diziortalama(liste,toplam=0,sayac=0):
    if sayac < len(liste):
        toplam+=liste[sayac]
        return diziortalama(liste,toplam,sayac+1)
    return toplam/len(liste)

sayilar =[2,3,4,6,23,12,67,9]

print(f"{sayilar} listesinin ortalaması = {diziortalama(sayilar)}")
'''
# 13. Dizi Elemanlarının Standart Sapmasını Hesaplama Fonksiyonu: Bir dizinin elemanlarının standart sapmasını hesaplayan özyinemeli bir fonksiyon yazın.
'''
def diziortalama(liste,toplam=0,sayac=0):
    if sayac < len(liste):
        toplam+=liste[sayac]
        return diziortalama(liste,toplam,sayac+1)
    return toplam/len(liste)


def standartsapma(ortalama,liste,toplamkare=0,indeks=0):
    if indeks < len(liste):
        toplamkare += (ortalama-liste[indeks])**2
        return standartsapma(ortalama,liste,toplamkare,indeks+1)
    return (toplamkare/len(liste))**0.5

sayilar =[1,2,3,4,5,6,7,8,9,10]
aritmetikortalama = diziortalama(sayilar)
print(f"{sayilar} listesinin standart sapması = {standartsapma(aritmetikortalama,sayilar)}")
'''
# 14. Asal Sayı Kontrolü Fonksiyonu: Bir sayının asal olup olmadığını kontrol eden özyinemeli bir fonksiyon yazın.
'''
def asalmi(sayi, sayac=2):
    if sayac < sayi:
        if sayi % sayac == 0:
            print("Sayı asal değildir.")
            return
        return asalmi(sayi, sayac + 1)

    print("Sayı asaldır.")

sayi = int(input("Sayı giriniz: "))
asalmi(sayi)
'''
# 15. Elemanları Belirli Bir Değere Kadar Olan Toplamları Bulma Fonksiyonu: Belirli bir değere kadar olan sayıların toplamlarını hesaplayan özyinemeli bir fonksiyon yazın.
'''
def toplama(sınır,sayac=0,toplam=0):
    if sayac < sınır:
        toplam += sayac
        return toplama(sınır,sayac+1,toplam)
    return toplam

sayi = int(input("Sayı giriniz:"))
print(f"{sayi} a kadar olan sayıların toplamı = {toplama(sayi)}")
'''
# 16. Dizi Elemanlarını Belirli Bir Değere Kadar Olan Tek Sayıları Toplama Fonksiyonu: Belirli bir değere kadar olan tek sayıların toplamını hesaplayan özyinemeli bir fonksiyon yazın.
'''
def teksayitop(n,toplam=0,sayac=0):
    if sayac < n:
        if sayac % 2 == 1:
            toplam += sayac
        return teksayitop(n,toplam,sayac+1)
    return toplam


sayi = int(input("Sayı giriniz:"))
print(f"{sayi} e kadar olan tek sayıların toplamı = {teksayitop(sayi)}")
 '''       

# 17. Dizi İçindeki En Büyük Elemanı Bulma Fonksiyonu: Bir dizinin içindeki en büyük elemanı bulan özyinemeli bir fonksiyon yazın.
'''
def enbüyükbul(liste,enbüyük=None,indeks=0):
    if indeks < len(liste):
        if enbüyük == None or liste[indeks] > enbüyük:
            enbüyük = liste[indeks]
        return enbüyükbul(liste,enbüyük,indeks+1)
    return enbüyük

sayilar = [1,2,5,7,88,9,23,6,34,65]

print(f"{sayilar} listesindeki en büyük sayı {enbüyükbul(sayilar)}")
'''
# 18. Dizi İçindeki En Küçük Elemanı Bulma Fonksiyonu: Bir dizinin içindeki en küçük elemanı bulan özyinemeli bir fonksiyon yazın.
'''
def enkücükbul(liste,enkücük=None,indeks=0):
    if indeks < len(liste):
        if enkücük == None or liste[indeks] < enkücük:
            enkücük = liste[indeks]
        return enkücükbul(liste,enkücük,indeks+1)
    return enkücük

sayilar = [1,2,5,7,88,9,23,6,34,65,0]

print(f"{sayilar} listesindeki en küçük sayı {enkücükbul(sayilar)}")
'''
# 19. Elemanları Belirli Bir Değere Kadar Olan Sayıları Çarpan Fonksiyon: Belirli bir değere kadar olan sayıların çarpımını hesaplayan özyinemeli bir fonksiyon yazın.
'''
def sayicarp(n,toplam=1,sayac=1):
    if sayac < n :
        toplam *= sayac
        return sayicarp(n,toplam,sayac+1)
    return toplam

sayi = int(input("Sayı giriniz:"))
print(f"{sayi} a kadar olan sayıların çarpımı = {sayicarp(sayi)} ")
'''

# 20. Dizi Elemanlarını Tek ve Çift Sayılara Ayırma Fonksiyonu: Bir diziyi içindeki elemanları tek ve çift sayılara ayıran özyinemeli bir fonksiyon yazın.
'''
def tekciftayir(liste,teklist=[],ciftlist=[],indeks = 0 ):
    if indeks < len(liste):
        if liste[indeks] % 2 == 1:
            teklist.append(liste[indeks])
        else:
            ciftlist.append(liste[indeks])
        return tekciftayir(liste,teklist,ciftlist,indeks+1)
    return 'Tek liste = ',teklist,'Çift liste = ',ciftlist

sayilar = [1,2,3,4,5,6,7,8,9,10]

print(f"{sayilar} listesindeki sayıların tek ve çift şekilde ayrılmış hali =>" ,tekciftayir(sayilar))
'''
# 21. Dizi Elemanlarını Toplamak İçin Özyinemeli Fonksiyon: Bir dizinin elemanlarını toplamak için özyinemeli bir fonksiyon yazın.
'''
def dizitopla(liste,toplam=0,indeks=0):
    if indeks < len(liste):
        toplam += liste[indeks]
        return dizitopla(liste,toplam,indeks + 1 )
    return toplam

sayilar = [1,2,3,4,5,6,7,8,9,10]

print(f"{sayilar} listesindeki sayıların toplamı = {dizitopla(sayilar)}")
'''

# 22. Dizi Elemanlarının Faktöriyelini Hesaplama Fonksiyonu: Bir dizinin elemanlarının faktöriyelini hesaplayan özyinemeli bir fonksiyon yazın.
'''
def dizifak(liste,faklist=[],indeks=0,toplam=1):
    if indeks < len(liste):
        toplam = 1
        for i in range(1,liste[indeks]+1):
            toplam *= i
        faklist.append(f"{liste[indeks]}! = {toplam}")
        return dizifak(liste,faklist,indeks+1,toplam)
    return faklist

sayilar =[1,2,3,4,5,6,8,9]
faktöriyel = dizifak(sayilar)

for i in faktöriyel:
    print(i)
'''
# 23. Dizi Elemanlarını Ters Sıralama Fonksiyonu: Bir diziyi sıralayıp elemanlarını ters çeviren özyinemeli bir fonksiyon yazın.
'''
def ters_siralama(dizi, indeks=0):
    if indeks < len(dizi):
        for i in range(indeks + 1, len(dizi)):
            if dizi[indeks] < dizi[i]:
                dizi[indeks], dizi[i] = dizi[i], dizi[indeks]
        return ters_siralama(dizi, indeks + 1)
    return dizi

sayilar = [2, 3, 5, 12, 65, 11, 45, 8, 23, 6]
print(f"Orjinal dizi: {sayilar}")
print(f"Ters sıralanmış dizi: {ters_siralama(sayilar)}")
'''
# 24. Dizi Elemanlarını Belirli Bir Değere Kadar Olan Çift Sayıları Toplama Fonksiyonu: Belirli bir değere kadar olan çift sayıların toplamını hesaplayan özyinemeli bir fonksiyon yazın.
'''
#Dizi içindeki 100 e kadar olan çift sayıların toplamı:

def cifttopla(liste,sinir=100,toplam=0,indeks=0):
    if indeks < len(liste):
        if liste[indeks] % 2 == 0 and liste[indeks] < sinir:
            toplam += liste[indeks]
        return cifttopla(liste,sinir,toplam,indeks+1)
    return toplam

sayilar = [12,3,5,7,8,45,22,47,34,453,20,16]

print(f"{sayilar} listesindeki 100 den küçük çift sayiların toplamı = {cifttopla(sayilar)}")
'''
# 25. Elemanları Belirli Bir Değere Kadar Olan Fibonacci Serisi Fonksiyonu: Fibonacci serisinin belirli bir değere kadar olan elemanlarını hesaplayan özyinemeli bir fonksiyon yazın.
'''
def Fibonacci(n, eleman1=0, eleman2=1, fibonacci=[0, 1]):
    if fibonacci[-1]<n:
        yeni_eleman = eleman1 + eleman2
        if yeni_eleman<n:
            fibonacci.append(yeni_eleman)
            return Fibonacci(n, eleman2, yeni_eleman, fibonacci)
    return fibonacci

sınır = int(input("Fibonacci serisi için sınır belirleyin:"))

print(f"{sınır} a kadar olan fibonacci serisinin elemanları= {Fibonacci(sınır)}")
'''

# 26.Elemanları Belirli Bir Değere Kadar Olan Asal Sayıları Bulma Fonksiyonu: Belirli bir değere kadar olan asal sayıları bulan özyinemeli bir fonksiyon yazın.
'''
def asalbul(n, asalliste=[], sayac=2):
    if sayac < n:
        for i in range(2, sayac):
            if sayac % i == 0:
                break
        else:
            asalliste.append(sayac)
        return asalbul(n, asalliste, sayac + 1)
    return asalliste

sinir = int(input("Asal sayılar için sınır giriniz:"))

print(f"{sinir} a kadar olan asal sayılar = {asalbul(sinir)}")
'''
# 27. Dizi İçinde Belirli Bir Değeri Arama Fonksiyonu: Bir dizinin içinde belirli bir değeri arayan özyinemeli bir fonksiyon yazın.
'''
def degeriara(dizi, deger, indeks=0):
    if indeks < len(dizi):
        if dizi[indeks] == deger:
            return f"{deger} değeri listenin {indeks+1}. indeksinde bulundu."
        else:
            return degeriara(dizi, deger, indeks + 1)
    else:
        return f"{deger} değeri listede bulunamadı."
    
sayilar = [2, 3, 5, 12, 65, 11, 45, 8, 23, 6]
aranandeger = 11
print(f"{sayilar} listesinde {aranandeger} değeri aranıyor...\n{degeriara(sayilar, aranandeger)}")
'''

# 29. Dizi Elemanlarını Birleştirip Ters Çevirme Fonksiyonu: İki diziyi birleştiren ve elde edilen diziyi ters çeviren özyinemeli bir fonksiyon yazın.
'''
def dizibirlestir(liste1, liste2, tersliste=[], indeks=0):
    if len(liste1) + len(liste2) != len(tersliste):
        if indeks < len(liste2):
            liste1.append(liste2[indeks])
            return dizibirlestir(liste1, liste2, tersliste, indeks + 1)
    for i in range(len(liste1) - 1, -1, -1):
        tersliste.append(liste1[i])
    return "Birleştirilmiş liste=", liste1, "Listenin ters çevrilmiş hali=", tersliste

sayilar = [0, 1, 2, 3, 4, 5]
harfler = ['a', 'b', 'c', 'd', 'e', 'f']

print(dizibirlestir(sayilar, harfler))
'''
# 30. Dizi Elemanlarını Belirli Bir Değere Kadar Olan Üslerini Hesaplama Fonksiyonu: Belirli bir değere kadar olan üslerini hesaplayan özyinemeli bir fonksiyon yazın.
'''
def ushesapla(x, n, sonuc=1, us=1):
    if us <= n:
        sonuc *= x
        print(f"{x} in {us}. üssü = {sonuc}")
        return ushesapla(x, n, sonuc, us + 1)
    else:
        return sonuc

sınır= int(input("Sınır giriniz:"))
sayilar=[1,2,3,4,5,6]
for i in sayilar:
    ushesapla(i, sınır)
    print()
'''
# 31. Dizi Elemanlarını Belirli Bir Değere Kadar Olan Çift Sayıları Bulma Fonksiyonu: Belirli bir değere kadar olan çift sayıları bulan özyinemeli bir fonksiyon yazın.
'''
def ciftsayilaribul(deger,liste,ciftliste=[],indeks=0):
    if liste[indeks] <= deger:
        if liste[indeks] % 2 == 0:
            ciftliste.append(liste[indeks])
        return ciftsayilaribul(deger,liste,ciftliste,indeks + 1)
    return ciftliste


sinir = int(input("Bir değer girin: "))
sayilar = [2,5,7,8,10,14,24,38]
print(f"{sayilar} listesindeki {sinir} a kadar olan çift sayılar = {ciftsayilaribul(sinir,sayilar)}")
'''
# 32. Dizi Elemanlarını Belirli Bir Değere Kadar Olan Üslerinin Toplamını Hesaplama Fonksiyonu: Belirli bir değere kadar olan üslerinin toplamını hesaplayan özyinemeli bir fonksiyon yazın.
'''
def üstoplamvehesapla(liste, n, üs=1, toplam=0, indeks=0):
    if indeks < len(liste):
        if üs <= n:
            taban = liste[indeks]
            üs_degeri = 1
            for i in range(üs):
                üs_degeri *= taban
            toplam += üs_degeri
            print(f"{taban} sayısının {üs}. üssü = {üs_degeri}")
            return üstoplamvehesapla(liste, n, üs + 1, toplam, indeks)
        else:
            print(f"{liste[indeks]} sayısının {n} e kadar olan üslerinin toplamı = {toplam}")
            return üstoplamvehesapla(liste, n, 1 , 0 , indeks + 1)
    else:
        return

sayilar = [1,2,3]
sinir=int(input("Sınır giriniz:"))
üstoplamvehesapla(sayilar, sinir)
'''
# 33. Dizi Elemanlarını Belirli Bir Değere Kadar Olan Asal Sayıların Karesini Hesaplama Fonksiyonu: Belirli bir değere kadar olan asal sayıların karesini hesaplayan özyinemeli bir fonksiyon yazın.
'''
def asalsayikareleri(toplam, n=2, asalkareler=None):
    if asalkareler is None:
        asalkareler = []

    if n > toplam:
        return asalkareler

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            break
    else:
        asalkareler.append(n**2)

    return asalsayikareleri(toplam, n+1, asalkareler)


sinir = int(input("Sınır giriniz:"))
print(f"{sinir}'ye kadar olan asal sayıların kareleri: {asalsayikareleri(sinir)}")
'''