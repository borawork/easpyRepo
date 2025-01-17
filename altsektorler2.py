import sektorler
altsek = input("alt sektor : ")

if altsek in ["bitkisel" , "hayvansal"]:
    def altTarimsek(tarim):
            tarim2=float(3.0)
            return f"alt tarim {tarim2}"
    sonucAltTarim = altTarimsek(altsek)
    print(sonucAltTarim)

elif altsek in["metalik","inşaat","değerli","enerji"]:
    def altsekmaden(maden):
        if altsek == "inşaat":
            maden2=float(2.0)
            return(f"alt maden {maden2}")
        elif altsek == "metalik":
            maden3=float(3.0)
            return(f"alt maden {maden3}")
        elif altsek in ["değerli","enerji"]:
            maden4=float(4.0)
            return(f"alt maden {maden4}")
    sonucaltsekcilik= altsekmaden(altsek)
    print(sonucaltsekcilik)



elif altsek in ["tütün","gida","içecek" , "diğer" , "temel","tekstil" ,"deri" , "ahşap","makine","kimyasal"]:
    def altsekimalat(imalat):
        if altsek == "tütün":
                im2=float(1.0)
                return(f"alt imalat {im2}" )
        elif altsek in ["gida" , "içecek" , "diğer" , "temel" ]:
                im3=float(2.0)
                return(f"alt imalat {im3}" )
        elif altsek in ["tekstil" ,"deri" , "ahşap"]:
                im4=float(3.0)
                return(f"alt imalat {im4}")
        elif altsek in ["makine","kimyasal" ]:
                im5=float(4.0)
                return(f"alt imalat {im5}" )
    sonucaltsek= altsekimalat(altsek)
    print(sonucaltsek)
        

elif altsek in["atik","su","elektrik","gaz"]:
    def altsekelektrik(elektrik_su_gaz_atikyonetimi):
        if altsek == "atik":
                ele2=float(2.0)
                return(f"alt elektrik {ele2}")                     
        elif altsek in "su":
                ele3=float(3.0)
                return(f"alt elektrik {ele3}")
        elif altsek in ["elektrik" , "gaz"]:
                ele4=float(4.0)
                return(f"alt elektrik {ele4}")
    sonucElektrik=altsekelektrik(altsek)
    print(sonucElektrik)


elif altsek in["bina","altyapi"]:
     def altsekinsaat(insaat):
          if altsek in "bina":
               ins2=float(2.0)
               return(f"alt insaat {ins2}")
          elif altsek in "altyapi":
               ins3=float(4.0)
               return(f"alt insaat {ins3}")
     sonucİnsaat=altsekinsaat(altsek)
     print(sonucİnsaat)


elif altsek in["perakende","toptan","e-ticaret"]:
     def altToptanPerakendeSek(toptan_perakende):
          if altsek in "perakende":
               tp2=float(2.0)
               return(f"alt toptan perakende {tp2}")                                       
          elif altsek in ["toptan" , "e-ticaret"]:
               tp3=float(3.0)
               return(f"alt toptan perakende {tp3}")
     sonucToptanPerakende=altToptanPerakendeSek(altsek)
     print(sonucToptanPerakende)
               

elif altsek in["karayolu" , "demiryolu" , "deniz" , "hava" , "depolama"]:
     def altLojistikSek(lojistik):
          if altsek in ["karayolu" , "demiryolu" , "deniz" , "hava" , "depolama"]:
               loj2=float(3.0)
               return(f"alt lojistik {loj2}")
     sonucLojistik = altLojistikSek(altsek)
     print(sonucLojistik)


elif altsek in["yiyecek" , "konaklama"]:
    def altKonaklamaYiyecekSek(konaklama_yiyecek):
        if altsek in "yiyecek":
            konyi2=float(1.0)
            return(f"alt konaklama yiyecek {konyi2}")                           
        elif altsek in "konaklama":
            konyi3=float(2.0)
            return(f"alt konaklama yiyecek {konyi3}")
    sonucKonaklamaYiyecek = altKonaklamaYiyecekSek(altsek)
    print(sonucKonaklamaYiyecek)


elif altsek in["medya" , "telekomünikasyon"]:
    def altBilgiLtSek(bilgi_iletisim):
        if altsek == "medya":
            bilgilt2=float(3.0)
            return(f"alt bilgi iletişim {bilgilt2}")             
        elif altsek == "telekomünikasyon":
            bilgilt3=float(4.0)
            return(f"alt bilgi iletişim {bilgilt3}")
    sonucBilgiİletişim = altBilgiLtSek(altsek)
    print(sonucBilgiİletişim)


elif altsek in["diğer finans" , "banka" , "sigorta" ]:
     def altFinansSigortaSek(finans_sigorta):
          if altsek == "diğer finans":
               fns2=float(3.0)
               return(f"alt finans sigorta {fns2}")                
          elif altsek in ["banka" , "sigorta"]:
               fns3=float(4.0)
               return(f"alt finans sigorta {fns3}")
     sonucFinansSigorta = altFinansSigortaSek(altsek)
     print(sonucFinansSigorta)


elif altsek in["emlak","ticari"]:
     def altEmlakKiralamaSek(emlak_kiralama):
          if altsek in "emlak":
                mlkrlm2=float(1.0)
                return(f"alt emlak kiralama {mlkrlm2}")           
          elif altsek in "ticari":
                mlkrlm3=float(2.0)
                return(f"alt emlak kiralama {mlkrlm3}")
     sonucEmlakKiralama = altEmlakKiralamaSek(altsek)
     print(sonucEmlakKiralama)


elif altsek in["merkezi" , "yerel", "savunma"]:
     def altKamuyönetimSavunmaSek(kamuyönetimi_savunma):
          if altsek in ["merkezi" , "yerel"]:
               kamusvm2=float(3.0)
               return(f"alt kamu yönetim ve savunma {kamusvm2}")   
          elif altsek in "savunma":
               kamusvm3=float(4.0)
               return(f"alt kamu yönetim ve savunma {kamusvm3}")
     sonucKamuyönetimSavunma = altKamuyönetimSavunmaSek(altsek)
     print(sonucKamuyönetimSavunma)


elif altsek in["okul öncesi" , "temel" , "ortaöğretim" ,"yükseköğretim" , "yetişkin"]:
     def altEgitimSek(egitim):
          if altsek in ["okul öncesi" , "temel" , "ortaöğretim" ,"yükseköğretim" , "yetişkin"]:
               egtm2=float(1.0)
               return(f"alt egitim {egtm2}")
     sonucEgitim = altEgitimSek(altsek)
     print(sonucEgitim)


elif altsek in["sosyal" , "saglik"]:
     def altSagliksek(saglik_sosyalhizmetler):
          if altsek in "sosyal":
               sglk2=float(2.0)
               return(f"alt saglik sosyal {sglk2}")                        
          elif altsek in "saglik":
               sglk3=float(3.0)
               return(f"alt saglik sosyal {sglk3}")
     sonucSaglik = altSagliksek(altsek)
     print(sonucSaglik)


elif altsek in["eglence","sanat"]:
     def altSanatSek(sanat_eglence):
          if altsek in "eglence":
               sanat2=float(2.0)
               return(f"alt sanat eglence {sanat2}")
          elif altsek in "sanat":
               sanat3=float(3.0)
               return(f"alt sanat eglence {sanat3}")
     sonucSanat = altSanatSek(altsek)
     print(sonucSanat)


elif altsek in["kisisel" ,  "diger" , "profesyonel"]:
     def altDigerSek(diger):
          if altsek in ["kisisel" ,  "diger"]:
               dgr2=float(1.0)
               return(f"alt diğer {dgr2}")
          elif altsek in "profesyonel":
               dgr3=float(2.0)
               return(f"alt diğer {dgr3}")
     sonucDiger = altDigerSek(altsek)
     print(sonucDiger)


elif altsek in["yazilim"]:
     def altYazilimSek(yazilim):
          if altsek in "yazilim":
               yzlm2=float(4.0)
               return(f"alt yazilim {yzlm2}")
     sonucYazilim = altYazilimSek(altsek)
     print(sonucYazilim)