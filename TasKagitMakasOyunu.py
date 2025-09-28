import random

def tas_kagit_makas():
    options = ["taş", "kağıt", "makas"]
    user = input("Taş, Kağıt, Makas? ").lower()
    comp = random.choice(options)

    print(f"Bilgisayar: {comp}")

    if user == comp:
        print("Berabere!")
    elif (user == "taş" and comp == "makas") or \
         (user == "kağıt" and comp == "taş") or \
         (user == "makas" and comp == "kağıt"):
        print("Kazandınız!")
    else:
        print("Kaybettiniz!")

tas_kagit_makas()
