boy = float(input("Boyunuzu giriniz: "))
kilo = int(input("Kilonuzu giriniz: "))
bmi = kilo/(boy*boy)
print("bmi: " , round(bmi,2))

if bmi<18.5:
    print("durum: zayıf")
elif 18.5<bmi<24.9:
    print("durum: normal")
elif 25<bmi<29.9:
    print("durum: kilolu")
elif 30<bmi<34.9:
    print("durum: 1.derece obez")
elif 35<bmi<39.9:
    print("durum: 2.derece obez")
elif 40<bmi:
    print("morbid obez")
