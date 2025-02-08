def karbon_hesapla():
    print("\n=== KARBON AYAK İZİ HESAPLAMA ===")
    print("\n1. İLETİŞİM KAYNAKLARI")
    print("-" * 50)
    degisken1 = float(input("Telefon konuşması (dakika/ay): "))
    degisken2 = float(input("E-mail sayısı (adet/ay): "))

    print("\n2. TÜKETİM MALZEMELERİ") 
    print("-" * 50)
    degisken3 = float(input("Plastik kullanımı (kg/ay): "))
    degisken4 = float(input("Kağıt kullanımı (kg/ay): "))

    print("\n3. KARASAL ULAŞIM")
    print("-" * 50)
    degisken5 = float(input("Araba kullanımı (km/ay): "))
    degisken6 = float(input("Motosiklet kullanımı (km/ay): "))
    degisken7 = float(input("Otobüs/Toplu taşıma kullanımı (km/ay): "))
    degisken8 = float(input("Tren kullanımı (km/ay): "))

    print("\n4. HAVA YOLU ULAŞIMI")
    print("-" * 50)
    degisken9 = float(input("Ekonomi sınıfı uçuş (km/ay): "))
    degisken10 = float(input("Business sınıfı uçuş (km/ay): "))

    print("\n5. ENERJİ TÜKETİMİ")
    print("-" * 50)
    degisken11 = float(input("Elektrik tüketimi (kWh/ay): "))
    degisken12 = float(input("Doğalgaz tüketimi (m³/ay): "))
    degisken13 = float(input("Diğer ısınma kaynakları (kg/ay): "))

    # Karbon ayak izi hesaplamaları
    sonuclar = {
        "Telefon": degisken1 * 0.19,
        "E-mail": degisken2 * 0.05,
        "Plastik": degisken3 * 0.0218,
        "Kağıt": degisken4 * 0.0218,
        "Araba": degisken5 * 1.052,
        "Motosiklet": degisken6 * 1.1949,
        "Toplu Taşıma": degisken7 * 0.12259,
        "Tren": degisken8 * 0.246698,
        "Ekonomi Uçuş": degisken9 * 0.08378,
        "Business Uçuş": degisken10 * 0.12565,
        "Elektrik": degisken11 * 0.39,
        "Doğalgaz": degisken12 * 2.09672,
        "Diğer Isınma": degisken13 * 0.215
    }

    toplam_karbon = sum(sonuclar.values())

    # Sonuçların gösterilmesi
    print("\n=== KARBON AYAK İZİ SONUÇLARI ===")
    print("-" * 50)
    print("Kategori bazlı CO2 salınımı (kg/ay):")
    print("-" * 50)
    
    for kaynak, deger in sonuclar.items():
        if deger > 0:  # Sadece kullanılan kaynakları göster
            print(f"{kaynak:<15}: {deger:.2f} kg CO2")

    print("-" * 50)
    print(f"TOPLAM KARBON AYAK İZİ: {toplam_karbon:.2f} kg CO2/ay")
    
    # Karbon ayak izi değerlendirmesi
    if toplam_karbon < 100:
        print("\nDeğerlendirme: Düşük karbon ayak izi 🌱")
    elif toplam_karbon < 500:
        print("\nDeğerlendirme: Orta düzey karbon ayak izi 🌿")
    else:
        print("\nDeğerlendirme: Yüksek karbon ayak izi ⚠️")
        print("Karbon ayak izinizi düşürmek için önlemler alabilirsiniz.")

if __name__ == "__main__":
    karbon_hesapla()
