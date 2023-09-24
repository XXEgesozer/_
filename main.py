import random
while True:
    karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    sayi = int(input("kac karakakterli sifre olusturlsun? "))

    sifre = ""
    for i in range(sayi):
        sifre += random.choice(karakterler)

    print(sifre)
