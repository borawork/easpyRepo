def main():
    # Sektör seçimi ve puanlama
    print("\n=== SEKTÖR SEÇİMİ ===")
    print("\nGeçerli sektörler:")
    print("tarim, maden, imalat, elektrik, gaz, su, atik yonetimi, insaat, toptan, perakende, ")
    print("lojistik, konaklama, yiyecek, bilgi, iletisim, finans, sigorta, emlak, kiralama, ")
    print("kamu yönetimi, savunma, egitim, saglik, sosyal hizmetler, sanat, eglence, diger, yazilim")
    
    sektorler = input("\nSektör giriniz: ")
    sektor_puan = 0

    # Sektör puanlaması
    if sektorler == "tarim":
        sektor_puan = 2.0
        alt_sektor_listesi = ["bitkisel", "hayvansal"]
    elif sektorler == "maden":
        sektor_puan = 2.0
        alt_sektor_listesi = ["metalik", "inşaat", "değerli", "enerji"]
    elif sektorler == "imalat":
        sektor_puan = 3.0
        alt_sektor_listesi = ["tütün", "gida", "içecek", "diğer", "temel", "tekstil", "deri", "ahşap", "makine", "kimyasal"]
    elif sektorler in ["elektrik", "gaz", "su", "atik yonetimi"]:
        sektor_puan = 4.0
        alt_sektor_listesi = ["atik", "su", "elektrik", "gaz"]
    elif sektorler == "insaat":
        sektor_puan = 3.0
        alt_sektor_listesi = ["bina", "altyapi"]
    elif sektorler in ["toptan", "perakende"]:
        sektor_puan = 2.0
        alt_sektor_listesi = ["perakende", "toptan", "e-ticaret"]
    elif sektorler == "lojistik":
        sektor_puan = 3.0
        alt_sektor_listesi = ["karayolu", "demiryolu", "deniz", "hava", "depolama"]
    elif sektorler in ["konaklama", "yiyecek"]:
        sektor_puan = 2.0
        alt_sektor_listesi = ["yiyecek", "konaklama"]
    elif sektorler in ["bilgi", "iletisim"]:
        sektor_puan = 3.0
        alt_sektor_listesi = ["medya", "telekomünikasyon"]
    elif sektorler in ["finans", "sigorta"]:
        sektor_puan = 4.0
        alt_sektor_listesi = ["diğer finans", "banka", "sigorta"]
    elif sektorler in ["emlak", "kiralama"]:
        sektor_puan = 1.0
        alt_sektor_listesi = ["emlak", "ticari"]
    elif sektorler in ["kamu yönetimi", "savunma"]:
        sektor_puan = 4.0
        alt_sektor_listesi = ["merkezi", "yerel", "savunma"]
    elif sektorler == "egitim":
        sektor_puan = 2.0
        alt_sektor_listesi = ["okul öncesi", "temel", "ortaöğretim", "yükseköğretim", "yetişkin"]
    elif sektorler in ["saglik", "sosyal hizmetler"]:
        sektor_puan = 3.0
        alt_sektor_listesi = ["sosyal", "saglik"]
    elif sektorler in ["sanat", "eglence"]:
        sektor_puan = 2.0
        alt_sektor_listesi = ["eglence", "sanat"]
    elif sektorler == "diger":
        sektor_puan = 1.0
        alt_sektor_listesi = ["kisisel", "diger", "profesyonel"]
    elif sektorler == "yazilim":
        sektor_puan = 4.0
        alt_sektor_listesi = ["yazilim"]
    else:
        print("Geçersiz sektör! Lütfen geçerli bir sektör giriniz.")
        return

    # Alt sektör seçimi ve puanlama
    print(f"\n=== ALT SEKTÖR SEÇİMİ ===")
    print(f"Seçilen sektör için geçerli alt sektörler: {', '.join(alt_sektor_listesi)}")
    altsek = input("\nAlt sektör: ")
    alt_sektor_puan = 0

    if altsek not in alt_sektor_listesi:
        print("Geçersiz alt sektör! Lütfen seçtiğiniz sektöre uygun bir alt sektör giriniz.")
        return

    # Alt sektör puanlaması
    if sektorler == "tarim":
        alt_sektor_puan = 3.0

    elif sektorler == "maden":
        if altsek == "inşaat":
            alt_sektor_puan = 2.0
        elif altsek == "metalik":
            alt_sektor_puan = 3.0
        elif altsek in ["değerli", "enerji"]:
            alt_sektor_puan = 4.0

    elif sektorler == "imalat":
        if altsek == "tütün":
            alt_sektor_puan = 1.0
        elif altsek in ["gida", "içecek", "diğer", "temel"]:
            alt_sektor_puan = 2.0
        elif altsek in ["tekstil", "deri", "ahşap"]:
            alt_sektor_puan = 3.0
        elif altsek in ["makine", "kimyasal"]:
            alt_sektor_puan = 4.0

    elif sektorler in ["elektrik", "gaz", "su", "atik yonetimi"]:
        if altsek == "atik":
            alt_sektor_puan = 2.0
        elif altsek == "su":
            alt_sektor_puan = 3.0
        elif altsek in ["elektrik", "gaz"]:
            alt_sektor_puan = 4.0

    elif sektorler == "insaat":
        if altsek == "bina":
            alt_sektor_puan = 2.0
        elif altsek == "altyapi":
            alt_sektor_puan = 4.0

    elif sektorler in ["toptan", "perakende"]:
        if altsek == "perakende":
            alt_sektor_puan = 2.0
        elif altsek in ["toptan", "e-ticaret"]:
            alt_sektor_puan = 3.0

    elif sektorler == "lojistik":
        if altsek in ["karayolu", "demiryolu", "deniz", "hava", "depolama"]:
            alt_sektor_puan = 3.0

    elif sektorler in ["konaklama", "yiyecek"]:
        if altsek == "yiyecek":
            alt_sektor_puan = 1.0
        elif altsek == "konaklama":
            alt_sektor_puan = 2.0

    elif sektorler in ["bilgi", "iletisim"]:
        if altsek == "medya":
            alt_sektor_puan = 3.0
        elif altsek == "telekomünikasyon":
            alt_sektor_puan = 4.0

    elif sektorler in ["finans", "sigorta"]:
        if altsek == "diğer finans":
            alt_sektor_puan = 3.0
        elif altsek in ["banka", "sigorta"]:
            alt_sektor_puan = 4.0

    elif sektorler in ["emlak", "kiralama"]:
        if altsek == "emlak":
            alt_sektor_puan = 1.0
        elif altsek == "ticari":
            alt_sektor_puan = 2.0

    elif sektorler in ["kamu yönetimi", "savunma"]:
        if altsek in ["merkezi", "yerel"]:
            alt_sektor_puan = 3.0
        elif altsek == "savunma":
            alt_sektor_puan = 4.0

    elif sektorler == "egitim":
        if altsek in ["okul öncesi", "temel", "ortaöğretim", "yükseköğretim", "yetişkin"]:
            alt_sektor_puan = 1.0

    elif sektorler in ["saglik", "sosyal hizmetler"]:
        if altsek == "sosyal":
            alt_sektor_puan = 2.0
        elif altsek == "saglik":
            alt_sektor_puan = 3.0

    elif sektorler in ["sanat", "eglence"]:
        if altsek == "eglence":
            alt_sektor_puan = 2.0
        elif altsek == "sanat":
            alt_sektor_puan = 3.0

    elif sektorler == "diger":
        if altsek in ["kisisel", "diger"]:
            alt_sektor_puan = 1.0
        elif altsek == "profesyonel":
            alt_sektor_puan = 2.0

    elif sektorler == "yazilim":
        if altsek == "yazilim":
            alt_sektor_puan = 4.0

    # Çalışan sayısı girişi ve puanlama
    print("\n=== ÇALIŞAN SAYISI ===")
    while True:
        try:
            eleman = int(input("Çalışan sayısını giriniz: ").strip())
            if eleman > 0:
                break
            print("Lütfen pozitif bir sayı giriniz.")
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")

    calisan_puan = 0
    
    # Sektöre göre çalışan sayısı puanlaması
    if sektorler in ["toptan", "diger", "perakende"]:
        if 1 <= eleman <= 2:
            calisan_puan = 1.0
        elif 3 <= eleman <= 5:
            calisan_puan = 2.0
        elif 6 <= eleman <= 10:
            calisan_puan = 3.0
        elif eleman >= 11:
            calisan_puan = 4.0
            
    elif sektorler in ["insaat", "imalat"]:
        if 1 <= eleman <= 5:
            calisan_puan = 1.0
        elif 6 <= eleman <= 25:
            calisan_puan = 2.0
        elif 26 <= eleman <= 50:
            calisan_puan = 3.0
        elif eleman >= 51:
            calisan_puan = 4.0
            
    elif sektorler == "yazilim":
        if 1 <= eleman <= 10:
            calisan_puan = 1.0
        elif 11 <= eleman <= 50:
            calisan_puan = 2.0
        elif 51 <= eleman <= 200:
            calisan_puan = 3.0
        elif eleman >= 201:
            calisan_puan = 4.0
            
    elif sektorler in ["tarim", "maden", "imalat", "elektrik", "sanat"]:
        if 1 <= eleman <= 15:
            calisan_puan = 1.0
        elif 16 <= eleman <= 40:
            calisan_puan = 2.0
        elif 41 <= eleman <= 80:
            calisan_puan = 3.0
        elif eleman >= 81:
            calisan_puan = 4.0
            
    elif sektorler in ["lojistik", "konaklama", "yiyecek"]:
        if 1 <= eleman <= 10:
            calisan_puan = 1.0
        elif 11 <= eleman <= 50:
            calisan_puan = 2.0
        elif 51 <= eleman <= 200:
            calisan_puan = 3.0
        elif eleman >= 201:
            calisan_puan = 4.0
            
    elif sektorler in ["egitim", "saglik"]:
        if 1 <= eleman <= 50:
            calisan_puan = 1.0
        elif 51 <= eleman <= 300:
            calisan_puan = 2.0
        elif 301 <= eleman <= 500:
            calisan_puan = 3.0
        elif eleman >= 501:
            calisan_puan = 4.0
            
    elif sektorler in ["iletisim", "bilgi"]:
        if 1 <= eleman <= 200:
            calisan_puan = 1.0
        elif 201 <= eleman <= 1000:
            calisan_puan = 2.0
        elif 1001 <= eleman <= 2000:
            calisan_puan = 3.0
        elif eleman >= 2001:
            calisan_puan = 4.0
            
    elif sektorler in ["kamu yönetimi", "savunma"]:
        if 1 <= eleman <= 1000:
            calisan_puan = 1.0
        elif 1001 <= eleman <= 5000:
            calisan_puan = 2.0
        elif 5001 <= eleman <= 10000:
            calisan_puan = 3.0
        elif eleman >= 10001:
            calisan_puan = 4.0
            
    elif sektorler in ["finans", "sigorta"]:
        if 1 <= eleman <= 100:
            calisan_puan = 1.0
        elif 101 <= eleman <= 500:
            calisan_puan = 2.0
        elif 501 <= eleman <= 1000:
            calisan_puan = 3.0
        elif eleman >= 1001:
            calisan_puan = 4.0

    # Şirket yaşı girişi ve puanlama
    print("\n=== ŞİRKET YAŞI ===")
    yil = float(input("Şirket yaşını giriniz: "))
    yas_puan = 0
    
    if 0 < yil <= 3:
        yas_puan = 1.0
    elif 3 < yil <= 10:
        yas_puan = 2.0
    elif 10 < yil <= 30:
        yas_puan = 3.0
    elif yil > 30:
        yas_puan = 4.0

    # Ülke güvenilirliği skoru
    print("\n=== ÜLKE GÜVENİLİRLİK SKORU ===")
    print("\nÜlke grupları:")

    print("Australia | Canada | Denmark | Germany | Liechtenstein | Luxembourg | Switzerland | Norway | Sweden |")
    print("European Union | Singapore | United States | Austria | Finland | New Zealand | France | Taiwan |") 
    print("United Arab Emirates | Hong Kong | Qatar | Belgium | Isle of Man | Macau | United Kingdom | South Korea |")
    print("Cayman Islands | Czech Republic | Estonia | Ireland | Kuwait | Israel | Bermuda | China | Japan | Lithuania | Saudi Arabia")
    

    print("Iceland | Malta | Slovakia | Slovenia | Chile | Latvia | Poland | Spain | Portugal | Malaysia | Botswana |")
    print("Andorra | Thailand | Croatia | Italy | Bulgaria | Peru | Philippines | Uruguay | Cyprus | Hungary |") 
    print("Indonesia | Mexico | Kazakhstan | India | Panama | Aruba | Colombia | Mauritius | Montserrat | Romania | Greece")
    

    print("Azerbaijan | Morocco | Oman | Trinidad and Tobago | Paraguay | Serbia | Guatemala | Vietnam | Brazil |")
    print("Georgia | Macedonia | San Marino | Dominican Republic | Ivory Coast | South Africa | Seychelles |")
    print("Armenia | Bangladesh | Costa Rica | Uzbekistan | Albania | Bahamas | Honduras | Namibia | Senegal |")
    print("Jamaica | Jordan | Benin | Fiji | Turkmenistan | Bahrain | Rwanda | Montenegro | Tanzania | Cambodia |")
    print("Lesotho | Turkey | Uganda | Zambia | Kenya | Mongolia | Nicaragua | Bosnia and Herzegovina |")
    print("Kyrgyzstan | Papua New Guinea | Togo | Barbados")
    

    print("Angola | Cape Verde | Gabon | Madagascar | Moldova | Solomon Islands | St Vincent and Grenadines |")
    print("Swaziland | Tajikistan | Cameroon | Egypt | Iraq | Nigeria | Congo | Maldives | Tunisia | Bolivia |")
    print("Burkina Faso | Ecuador | El Salvador | Mozambique | Pakistan | Republic of the Congo | Belize |")
    print("Ethiopia | Laos | Mali | Niger | Suriname | Russia | Ukraine | Argentina | Belarus | Ghana |")
    print("Sri Lanka | Venezuela | Lebanon | Cuba | Puerto Rico | Grenada | Kosovo")

    ulkeler = input("\nÜlke giriniz: ")
    ulke_puan = 0

    # 4 puanlık ülkeler
    if ulkeler in ["Australia", "Canada", "Denmark", "Germany", "Liechtenstein", "Luxembourg", "Switzerland", 
                   "Norway", "Sweden", "European Union", "Singapore", "United States", "Austria", "Finland", 
                   "New Zealand", "France", "Taiwan", "United Arab Emirates", "Hong Kong", "Qatar", "Belgium", 
                   "Isle of Man", "Macau", "United Kingdom", "South Korea", "Cayman Islands", "Czech Republic", 
                   "Estonia", "Ireland", "Kuwait", "Israel", "Bermuda", "China", "Japan", "Lithuania", "Saudi Arabia"]:
        ulke_puan = 4.0
    
    # 3 puanlık ülkeler
    elif ulkeler in ["Iceland", "Malta", "Slovakia", "Slovenia", "Chile", "Latvia", "Poland", "Spain", "Portugal", 
                     "Malaysia", "Botswana", "Andorra", "Thailand", "Croatia", "Italy", "Bulgaria", "Peru", 
                     "Philippines", "Uruguay", "Cyprus", "Hungary", "Indonesia", "Mexico", "Kazakhstan", "India", 
                     "Panama", "Aruba", "Colombia", "Mauritius", "Montserrat", "Romania", "Greece"]:
        ulke_puan = 3.0
    
    # 2 puanlık ülkeler
    elif ulkeler in ["Azerbaijan", "Morocco", "Oman", "Trinidad and Tobago", "Paraguay", "Serbia", "Guatemala", 
                     "Vietnam", "Brazil", "Georgia", "Macedonia", "San Marino", "Dominican Republic", "Ivory Coast", 
                     "South Africa", "Seychelles", "Armenia", "Bangladesh", "Costa Rica", "Uzbekistan", "Albania", 
                     "Bahamas", "Honduras", "Namibia", "Senegal", "Jamaica", "Jordan", "Benin", "Fiji", 
                     "Turkmenistan", "Bahrain", "Rwanda", "Montenegro", "Tanzania", "Cambodia", "Lesotho", 
                     "Turkey", "Uganda", "Zambia", "Kenya", "Mongolia", "Nicaragua", "Bosnia and Herzegovina", 
                     "Kyrgyzstan", "Papua New Guinea", "Togo", "Barbados"]:
        ulke_puan = 2.0
    
    # 1 puanlık ülkeler
    elif ulkeler in ["Angola", "Cape Verde", "Gabon", "Madagascar", "Moldova", "Solomon Islands", 
                     "St Vincent and the Grenadines", "Swaziland", "Tajikistan", "Cameroon", "Egypt", "Iraq", 
                     "Nigeria", "Congo", "Maldives", "Tunisia", "Bolivia", "Burkina Faso", "Ecuador", 
                     "El Salvador", "Mozambique", "Pakistan", "Republic of the Congo", "Belize", "Ethiopia", 
                     "Laos", "Mali", "Niger", "Suriname", "Russia", "Ukraine", "Argentina", "Belarus", "Ghana", 
                     "Sri Lanka", "Venezuela", "Lebanon", "Cuba", "Puerto Rico", "Grenada", "Kosovo"]:
        ulke_puan = 1.0
    else:
        print("Geçersiz ülke! Lütfen listeden bir ülke seçiniz.")
        return

    # Müşteri durumu kontrolü
    print("\n=== MÜŞTERİ DURUMU ===")
    kullaniyormu = input("Bizi kullanıyor mu (evet/hayir): ")
    musteri_puan = 1.0 if kullaniyormu.lower() == "evet" else 0.0

    # Sabit sektör büyüme puanı
    buyume_puan = 2.5

    # Finansal veriler
    print("\n=== FİNANSAL VERİLER ===")
    toplamVarlik = float(input("Toplam varlık: "))
    netSermaye = float(input("Net sermaye: "))
    dagitilmamisKar = float(input("Dağıtılmamış kar: "))
    satislar = float(input("Satışlar: "))
    calismaSermayesi = float(input("Çalışma sermayesi: "))
    faizOncesiKar = float(input("Faiz öncesi kar: "))
    vergiOncesiKar = float(input("Vergi öncesi kar: "))
    kisaVadeliYukumlulukler = float(input("Kısa vadeli yükümlülükler: "))

    # Finansal oranların hesaplanması
    degisken1 = ((netSermaye / toplamVarlik) * 1.2)
    degisken2 = ((dagitilmamisKar / toplamVarlik) * 1.4)
    degisken3 = ((satislar / toplamVarlik) * 1.21)
    degisken4 = ((calismaSermayesi / toplamVarlik) * 1.05)
    degisken5 = ((faizOncesiKar / toplamVarlik) * 2.33)
    degisken6 = ((vergiOncesiKar / kisaVadeliYukumlulukler) * 0.66)

    finansal_skor = (degisken1 + degisken2 + degisken3 + degisken4 + degisken5 + degisken6) * 25

    # Diğer parametrelerin toplamı
    diger_parametreler = (sektor_puan + alt_sektor_puan + calisan_puan + yas_puan + ulke_puan + musteri_puan + buyume_puan)

    # Toplam skor hesaplama
    toplam_skor = finansal_skor + diger_parametreler

    # Sonuçların gösterilmesi
    print("\n=== SONUÇLAR ===")
    print(f"Finansal Skor: {finansal_skor:.2f}")
    print(f"Diğer Parametreler Skoru: {diger_parametreler:.2f}")
    print(f"TOPLAM SKOR: {toplam_skor:.2f}/100")

if __name__ == "__main__":
    main() 