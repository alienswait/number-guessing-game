import random
import time

print("""
*********************************

Sayı Tahmin Oyununa Hoşgeldiniz..

*********************************
""")

print("Lütfen 1 ve 100 arasında bir sayı tahmin ediniz.")

rastgele_sayı = random.randint(1,100)

tahmin_hakkı=10

while True:

    tahmin = int(input("lütfen sayı giriniz."))

    if tahmin < rastgele_sayı:
        print("Lütfen bekleyin...")
        time.sleep(1)

        print("Lütfen daha büyük bir sayı giriniz.")
        tahmin_hakkı -=1

    elif tahmin > rastgele_sayı:
        print("Lütfen bekleyin...")
        time.sleep(1)

        print("lütfen daha küçük bir sayı giriniz.")
        tahmin_hakkı -=1

    else:
        print("Tebrikler.. Kazandınız :)) ")
        exit()

    if tahmin_hakkı ==0:
        print("Üzgünüz, kaybettiniz :( ")
        break
