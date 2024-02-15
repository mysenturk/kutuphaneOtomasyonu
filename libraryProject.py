class Library:
    def __init__(self, dosya_adi="books.txt"):
        self.dosya_adi = dosya_adi
        self.dosya = open(self.dosya_adi, "a+")

    def __del__(self):
        self.dosya.close()

    def kitap_listesi(self):
        self.dosya.seek(0)
        satirlar = self.dosya.read().splitlines()

        if not satirlar:
              print("Bu kitap kütüphanemizde yok")
        else:
            print("Kitap Listesi")
            for satir in satirlar:
                kitap_bilgisi = satir.split(',')
                print(f"Kitap Adı: {kitap_bilgisi[0]}, Yazar: {kitap_bilgisi[1]}")

    def kitap_ekle(self):
        Kitap_Adı = input("Lütfen Eklemek İstediğiniz Kitabın Adını Giriniz: ")
        Yazar = input("Lütfen Eklemek İstediğiniz Kitabın Yazarını Giriniz: ")
        Basım_Tarihi = input("Lütfen Eklemek İstediğiniz Kitabın Basım Tarihini Giriniz: ")
        Sayfa_Sayısı = input("Lütfen Eklemek İstediğiniz Kitabın Sayfa Sayısını Giriniz: ")

        kitap_bilgisi = f"{Kitap_Adı},{Yazar},{Basım_Tarihi},{Sayfa_Sayısı}\n"
        self.dosya.write(kitap_bilgisi)
        print(f"Kitap '{Kitap_Adı}' Başarıyla Eklendi :) ")

    def kitap_sayisi(self):
        self.dosya.seek(0)
        satirlar = self.dosya.read().splitlines()
        kitap_sayisi = len(satirlar)
        print(f"Kütüphanede Bulunan Kitap Sayısı: {kitap_sayisi}")

    def kitap_sil(self):
        kitap_sil = input("Lütfen Silmek İstediğiniz Kitabın Adını Giriniz: ").strip()

        self.dosya.seek(0)
        satirlar = self.dosya.read().splitlines()

        new_list = []
        found = False
        for satir in satirlar:
            kitap_bilgisi = satir.split(',')
            kitap_adi = kitap_bilgisi[0].strip()
            if kitap_sil.lower() != kitap_adi.lower():
                new_list.append(satir)
            else:
                found = True

        if found:
            self.dosya.truncate(0)
            self.dosya.seek(0)
            for satir in new_list:
                self.dosya.write(satir + '\n')
            print(f"Kitap '{kitap_sil}' Başarıyla Kaldırılmıştır  ")
        else:
            print(f"Kitap '{kitap_sil}' Listede Bulunamamıştır ! ")



lib = Library()

while True:
    print("\033[0m\n *** MENÜ ***")
    print("\033[91m  1) Kitap Listesi")
    print("\033[0m   2) Kitap Ekle")
    print("\033[91m  3) Kitap Sil")
    print("\033[0m   4) Kitap Sayısı")
    print("\033[91m  q) Çıkış Yap ")

    kullanici_girisi = input("\033[0mSeçiminizi Yapınız (1-q): ")

    if kullanici_girisi == "1":
        lib.kitap_listesi()
    elif kullanici_girisi == "2":
        lib.kitap_ekle()
    elif kullanici_girisi == "3":
        lib.kitap_sil()
    elif kullanici_girisi == "4":
        lib.kitap_sayisi()
    elif kullanici_girisi.lower() == "q":
        print("Programdan Başarıyla Çıkış Yapıldı. İyi Günler ")
        break
    else:
        print("! Geçersiz Seçim ! Lütfen 1 ile q Arasında Bir Seçim Yapınız ")