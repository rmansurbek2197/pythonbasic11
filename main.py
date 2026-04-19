def soz_top():
    sozlar = {}
    with open('matn.txt', 'r') as f:
        matn = f.read()
        sozlar_list = matn.split()
        for soz in sozlar_list:
            soz = soz.lower()
            if soz in sozlar:
                sozlar[soz] += 1
            else:
                sozlar[soz] = 1
    eng_ko_p_uchragan_soz = max(sozlar, key=sozlar.get)
    return eng_ko_p_uchragan_soz, sozlar[eng_ko_p_uchragan_soz]

def asosiy():
    print("Matn fayldan o'qilmoqda...")
    eng_ko_p_uchragan_soz, miqdor = soz_top()
    print(f"Eng ko'p uchraydigan so'z: {eng_ko_p_uchragan_soz}")
    print(f"Uchraydigan miqdori: {miqdor}")
    print("Boshqa ishlar uchun quyidagi variantlardan birini tanlang:")
    print("1. So'zlar sonini chiqarish")
    print("2. So'zlar ro'yxatini chiqarish")
    print("3. So'zlar miqdorini chiqarish")
    tanlov = int(input("Tanlang: "))
    if tanlov == 1:
        print(len(eng_ko_p_uchragan_soz))
    elif tanlov == 2:
        soz_top()
        print(eng_ko_p_uchragan_soz)
    elif tanlov == 3:
        print(miqdor)

def sozlar_soni():
    with open('matn.txt', 'r') as f:
        matn = f.read()
        sozlar_list = matn.split()
        return len(sozlar_list)

def sozlar_ro_yxati():
    with open('matn.txt', 'r') as f:
        matn = f.read()
        sozlar_list = matn.split()
        return sozlar_list

def sozlar_miqdori():
    sozlar = {}
    with open('matn.txt', 'r') as f:
        matn = f.read()
        sozlar_list = matn.split()
        for soz in sozlar_list:
            soz = soz.lower()
            if soz in sozlar:
                sozlar[soz] += 1
            else:
                sozlar[soz] = 1
        return sozlar

def soz_topish():
    with open('matn.txt', 'r') as f:
        matn = f.read()
        sozlar_list = matn.split()
        soz = input("So'z kiriting: ")
        soz = soz.lower()
        if soz in sozlar_list:
            print(f"{soz} so'zi {sozlar_list.count(soz)} marta uchraydi")
        else:
            print(f"{soz} so'zi uchramadi")

def barcha_so_zlar():
    sozlar = {}
    with open('matn.txt', 'r') as f:
        matn = f.read()
        sozlar_list = matn.split()
        for soz in sozlar_list:
            soz = soz.lower()
            if soz in sozlar:
                sozlar[soz] += 1
            else:
                sozlar[soz] = 1
        return sozlar

asosiy()