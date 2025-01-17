sektorler = input("sektor giriniz : ")

if sektorler == "tarim":
    def tarimveorman(tarim):
        tarim = float(2.0)
        return f" {tarim}"
    sonuctarim = tarimveorman(sektorler)
    print(sonuctarim)

elif sektorler == "maden":
    def madencilik(maden):
        maden = float(2.0)
        return f"madencilik secildi {maden}"
    sonucmadencilik = madencilik(sektorler)
    print(sonucmadencilik)

elif sektorler == "imalat":
    def imalat(im1):
        im1 = float(3.0)
        return f"imalat secildi {im1}"
    sonucimalat = imalat(sektorler)
    print(sonucimalat)

elif sektorler in ["elektrik","gaz","su","atik yonetimi"]:
    def elektrik(elektrik):
        elektrik = float(4.0)
        return f"elektrik,gaz,su ve atik su yonetimi secildi {elektrik}"
    sonucele = elektrik(sektorler)
    print(sonucele)

elif sektorler == "insaat":
    def insaat(insaat):
        insaat = float(3.0)
        return f"insaat sectiniz {insaat}"
    sonucins = insaat(sektorler)
    print(sonucins)

elif sektorler == "toptan" or sektorler == "perakende":
    def toptanperakende(toptanpr):
        toptanpr = float(2.0)
        return f"{toptanpr}"
    sonuctp = toptanperakende(sektorler)
    print(sonuctp)

elif sektorler == "lojistik":
    def lojistik(lojistik):
        lojistik = float(3.0)
        return f"{lojistik}"
    sonucloji = lojistik(sektorler)
    print(sonucloji)
    
elif sektorler in ["konaklama","yiyecek"]:
    def konaklama(konaklma):
        konaklma = float(2.0)
        return f"{konaklma}"
    sonuckonak = konaklama(sektorler)
    print(sonuckonak)

elif sektorler == "bilgi" or sektorler=="iletisim" :
    def bgilt(bilgi):
        bilgi = float(3.0)
        return f"bilgi  {bilgi}"
    sonucbilgi = bgilt(sektorler)
    print(sonucbilgi)
    
elif sektorler == "finans" or sektorler == "sigorta":
    def fnsgrt(finans):
        finans = float(4.0)
        return f"finansal ve sigorta {finans}"
    sonucfns = fnsgrt(sektorler)
    print(sonucfns)

elif sektorler == "emlak" or sektorler == "kiralama":
    def emlkrlm(emlak):
        emlak = float(1.0)
        return f" {emlak}"
    sonuckmk = emlkrlm(sektorler)
    print(sonuckmk)

elif sektorler == "kamu yönetimi" or sektorler == "savunma":
    def kmysvm(kamu):
        kamu = float(4.0)
        return f"{kamu}"
    sonuckmsvnm = kmysvm(sektorler)
    print(sonuckmsvnm)

elif sektorler == "egitim":
    def egitim(egtm):
        egtm = float(2.0)
        return f"egitim {egtm}"
    sonucegtm = egitim(sektorler)
    print(sonucegtm)

elif sektorler == "saglik" or sektorler == "sosyal hizmetler":
    def saglik(sglk):
        sglk = float(3.0)
        return f"insan sagliği ve sosyal hizmetler {sglk}"
    sonucsglk = saglik(sektorler)
    print(sonucsglk)

elif sektorler == "sanat" or sektorler == "eglence":
    def sanat(snt):
        snt = float(2.0)
        return f" {snt}"
    sonucsnt = sanat(sektorler)
    print(sonucsnt)
    
elif sektorler == "diger":
    def diger(dgr):
        dgr = float(1.0)
        return f"{dgr}"
    sonucdgr = diger(sektorler)
    print(sonucdgr)
    
elif sektorler == "yazilim":
    def yazilim (yzlm):
        yzlm = float(4.0)
        return f"yazilim {yzlm}"
    sonucyzlm = yazilim(sektorler)
    print(sonucyzlm)
else:
    print("tekrar deneyin")