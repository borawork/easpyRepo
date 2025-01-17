

kullaniyormu = input("bizi kullaniyor mu :")

if kullaniyormu in ["evet","hayir"]:
    def altkullanma(evethayir):
        if kullaniyormu in "evet":
            evet=float(1.0)
            return(f"bizi kullaniyor !  + {evet} puan")
        elif kullaniyormu in "hayir":
            return("bizi kullanmiyor")
    sonucKullaniyormu=altkullanma(kullaniyormu)
    print(sonucKullaniyormu)
        