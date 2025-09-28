import random
import string

def strong_password(length):
    if length < 4:
        raise ValueError("Şifre uzunluğu en az 4 olmalı (her karakter tipinden biri için).")

    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    symbol = random.choice(string.punctuation)

    remaining = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) 
                        for _ in range(length - 4))

    password_list = list(lowercase + uppercase + digit + symbol + remaining)
    random.shuffle(password_list) 

    return ''.join(password_list)


try:
    length = int(input("Şifre uzunluğunu giriniz: "))
    print("Oluşturulan güçlü şifre:", strong_password(length))
except ValueError as e:
    print("Hata:", e)
