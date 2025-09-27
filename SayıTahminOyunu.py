import random
import time
tutulan_sayi = random.randint(1,100)
tahmin_hakki = 10
sayaç = 0
cevap1 = "evet"
cevap2 = "hayir"
metin = "oyun basliyor!!!!"
for i in metin:
    print(i, end="", flush=True)
    time.sleep(0.2)
print(" ")
while True:
    tahmin = int(input("tahmininizi giriniz: "))
    tahmin_hakki -= 1
    sayaç += 1
    if tahmin == tutulan_sayi:
        print("sayiyi doğru tahmin ettiniz.")
        print(f"sayiyi {sayaç}'inci denemede buldunuz.")
        break
    elif tahmin < tutulan_sayi:
        print(f"tahmininiz doğru sayidan küçük. kalan hakkiniz: {tahmin_hakki}")
        if tahmin_hakki == 0:
            print(f"tahmin hakkiniz bitti. doğru sayi: {tutulan_sayi}")
            break
    elif tahmin > tutulan_sayi:
        print(f"tahmininiz doğru sayidan büyük. kalan hakkiniz: {tahmin_hakki}")
        if tahmin_hakki == 0:
            cevap = input("tahmin hakkiniz kalmadi. oyuna tekrar baslamak ister misiniz: ")
            if cevap == cevap1:
                tahmin_hakki = 10
            elif cevap == cevap2:
                print("oyun bitti")
                break
