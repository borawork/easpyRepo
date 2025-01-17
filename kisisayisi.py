import altsektorler2


while True:
        eleman = int(input("Lütfen eleman sayisini giriniz: ").strip())
        if eleman > 0:
            break

if altsektorler2.sektorler.sektorler in [ "toptan", "diger" , "perakende"]:
    def Apuan(eleman):
        if (1<=eleman<=2):
            a1=float(1.0)
            return f"{a1}"
        elif (3<=eleman<=5):
            a2=float(2.0)
            return f"{a2}"
        elif (6<=eleman<=10):
            a3=float(3.0)
            return f"{a3}"
        elif (eleman >=11):
            a4=float(4.0)
            return f"{a4}"
    sonucA=Apuan(eleman)
    print(sonucA)

elif altsektorler2.sektorler.sektorler in["insaat","imalat"] :
    def Bpuan(eleman):
        if (1>=eleman<=5):
            b1=float(1.0)
            return f"{b1}"
        elif (6<=eleman<=25):
            b2=float(2.0)
            return f"{b2}"
        elif (26<=eleman<=50):
            b3=float(3.0)
            return f"{b3}"
        elif (eleman>=51):
            b4=float(4.0)
            return f"{b4}"
    sonucB=Bpuan(eleman)
    print(sonucB)

elif altsektorler2.sektorler.sektorler in ["yazilim"]:
    def Cpuan(eleman):
            if (1>=eleman<=10):
                c1=float(1.0)
                return f"{c1}"
            elif (11<=eleman<=50):
                c2=float(2.0)
                return f"{c2}"
            elif (51<=eleman<=200):
                c3=float(3.0)
                return f"{c3}"
            elif (eleman >= 201):
                c4=float(4.0)
                return f"{c4}"
    sonucC=Cpuan(eleman)
    print(sonucC)
    
elif altsektorler2.sektorler.sektorler in ["tarim","maden","imalat","elektrik", "sanat"] :
    def Dpuan(eleman):
                if (1<=eleman<=15):
                    d1=float(1.0)
                    return f"{d1}"
                elif (16<=eleman<=40):
                    d2=float(2.0)
                    return f"{d2}"
                elif (41<=eleman<=80):
                    d3=float(3.0)
                    return f"{d3}"
                elif (eleman >=81):
                    d4=float(4.0)
                    return f"{d4}"
    sonucD=Dpuan(eleman)
    print(sonucD)

elif altsektorler2.sektorler.sektorler in ["lojistik","konaklama","yiyecek"]:
    def Epuan(eleman):
            if (1>=eleman<=10):
                e1=float(1.0)
                return f"{e1}"
            elif (11>=eleman<=50):
                e2=float(2.0)
                return f"{e2}"
            elif (51>=eleman<=200):
                e3=float(3.0)
                return f"{e3}"
            elif (eleman>=201):
                e4=float(4.0)
                return f"{e4}"
    sonucE=Epuan(eleman)
    print(sonucE)

elif altsektorler2.sektorler.sektorler in ["egitim","saglik"]: 
    def Fpuan(eleman):
            if (1>=eleman<=50):
                f1=float(1.0)
                return f"{f1}"
            elif (51>=eleman<=300):
                f2=float(2.0)
                return f"{f2}"
            elif (301>=eleman<=500):
                f3=float(3.0)
                return f"{f3}"
            elif (eleman>=501):
                f4=float(4.0)
                return f"{f4}"
    sonucF=Fpuan(eleman)
    print(sonucF)
       
elif altsektorler2.sektorler.sektorler in ["iletisim" , "bilgi"]:
    def Gpuan(eleman):
            if (1>=eleman<=200):
                g1=float(1.0)
                return f"{g1}"
            elif (201>=eleman<=1000):
                g2=float(2.0)
                return f"{g2}"
            elif (1001>=eleman<=2000):
                g3=float(3.0)
                return f"{g3}"
            elif (eleman>=2001):
                g4=float(4.0)
                return f"{g4}"
    sonucG=Gpuan(eleman) 
    print(sonucG)

elif altsektorler2.sektorler.sektorler in ["kamu yönetimi","savunma"]:           
    def Hpuan(eleman):
            if (1>=eleman<=1000):
                h1=float(1.0)
                return f"{h1}"
            elif (1001>=eleman<=5000):
                h2=float(2.0)
                return f"{h2}"
            elif (5001>=eleman<=10000):
                h3=float(3.0)
                return f"{h3}"
            elif (eleman>=10001):
                h4=float(4.0)
                return f"{h4}"
    sonucH=Hpuan(eleman) 
    print(sonucH)