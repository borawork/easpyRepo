import pandas as pd
import numpy as np
from collections import defaultdict

def benford_analizi():
    print("\n=== FİNANSAL TABLO BENFORD ANALİZİ ===")
    
    try:
        # Excel dosyasını oku
        dosya_adi = input("Excel dosyasının adını giriniz (örn: 1000yatirimlar.xls): ")
        df = pd.read_excel(dosya_adi)
        
        # Sayısal sütunları seç
        sayisal_sutunlar = df.select_dtypes(include=[np.number]).columns
        
        # Her hane için sayaç oluştur (1-5. haneler için)
        haneler = {1: defaultdict(int), 
                  2: defaultdict(int),
                  3: defaultdict(int),
                  4: defaultdict(int),
                  5: defaultdict(int)}
        
        # Toplam geçerli sayı sayısı
        toplam_sayi = 0
        
        # Her sayısal sütunu işle
        for sutun in sayisal_sutunlar:
            for deger in df[sutun]:
                # NaN değerleri ve 0'ları atla
                if pd.isna(deger) or deger == 0:
                    continue
                    
                # Sayıyı mutlak değere çevir ve string'e dönüştür
                sayi_str = str(abs(float(deger)))
                # Noktayı kaldır
                sayi_str = sayi_str.replace('.', '')
                
                # En az 1 haneli sayıları işle
                if len(sayi_str) > 0:
                    toplam_sayi += 1
                    
                    # Her hane için sayımı yap
                    for hane in range(1, 6):
                        if len(sayi_str) >= hane:
                            rakam = int(sayi_str[hane-1])
                            haneler[hane][rakam] += 1
        
        # Sonuçları yazdır
        print("\n=== SONUÇLAR ===")
        print("-" * 50)
        
        for hane in range(1, 6):
            print(f"\n{hane}. HANE DAĞILIMI:")
            print("-" * 20)
            toplam_hane = sum(haneler[hane].values())
            
            if toplam_hane > 0:  # Eğer bu hane için veri varsa
                for rakam in range(10):
                    sayi = haneler[hane][rakam]
                    yuzde = (sayi / toplam_hane) * 100
                    print(f"Rakam {rakam}: %{yuzde:.2f} ({sayi} adet)")
            else:
                print("Bu hane için yeterli veri yok.")
        
        print("\n" + "-" * 50)
        print(f"Toplam işlenen sayı adedi: {toplam_sayi}")
        
    except FileNotFoundError:
        print("Hata: Excel dosyası bulunamadı!")
    except Exception as e:
        print(f"Hata oluştu: {str(e)}")

if __name__ == "__main__":
    benford_analizi()
