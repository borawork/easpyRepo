// Sektör ve alt sektör verilerini tanımlayalım
const sektorData = {
    tarim: {
        name: "Tarım",
        puan: 2.0,
        altSektorler: ["bitkisel", "hayvansal"],
        altSektorPuanlar: {
            "bitkisel": 3.0,
            "hayvansal": 3.0
        }
    },
    maden: {
        name: "Maden",
        puan: 2.0,
        altSektorler: ["metalik", "inşaat", "değerli", "enerji"],
        altSektorPuanlar: {
            "inşaat": 2.0,
            "metalik": 3.0,
            "değerli": 4.0,
            "enerji": 4.0
        }
    },
    imalat: {
        name: "İmalat",
        puan: 3.0,
        altSektorler: ["tütün", "gida", "içecek", "diğer", "temel", "tekstil", "deri", "ahşap", "makine", "kimyasal"],
        altSektorPuanlar: {
            "tütün": 1.0,
            "gida": 2.0,
            "içecek": 2.0,
            "diğer": 2.0,
            "temel": 2.0,
            "tekstil": 3.0,
            "deri": 3.0,
            "ahşap": 3.0,
            "makine": 4.0,
            "kimyasal": 4.0
        }
    },
    elektrik: {
        name: "Elektrik, Gaz, Su ve Atık Yönetimi",
        puan: 4.0,
        altSektorler: ["atik", "su", "elektrik", "gaz"],
        altSektorPuanlar: {
            "atik": 2.0,
            "su": 3.0,
            "elektrik": 4.0,
            "gaz": 4.0
        }
    },
    insaat: {
        name: "İnşaat",
        puan: 3.0,
        altSektorler: ["bina", "altyapi"],
        altSektorPuanlar: {
            "bina": 2.0,
            "altyapi": 4.0
        }
    },
    toptan_perakende: {
        name: "Toptan ve Perakende",
        puan: 2.0,
        altSektorler: ["perakende", "toptan", "e-ticaret"],
        altSektorPuanlar: {
            "perakende": 2.0,
            "toptan": 3.0,
            "e-ticaret": 3.0
        }
    },
    lojistik: {
        name: "Lojistik",
        puan: 3.0,
        altSektorler: ["karayolu", "demiryolu", "deniz", "hava", "depolama"],
        altSektorPuanlar: {
            "karayolu": 3.0,
            "demiryolu": 3.0,
            "deniz": 3.0,
            "hava": 3.0,
            "depolama": 3.0
        }
    },
    konaklama: {
        name: "Konaklama ve Yiyecek",
        puan: 2.0,
        altSektorler: ["yiyecek", "konaklama"],
        altSektorPuanlar: {
            "yiyecek": 1.0,
            "konaklama": 2.0
        }
    },
    bilgi_iletisim: {
        name: "Bilgi ve İletişim",
        puan: 3.0,
        altSektorler: ["medya", "telekomünikasyon"],
        altSektorPuanlar: {
            "medya": 3.0,
            "telekomünikasyon": 4.0
        }
    },
    finans: {
        name: "Finans ve Sigorta",
        puan: 4.0,
        altSektorler: ["diğer finans", "banka", "sigorta"],
        altSektorPuanlar: {
            "diğer finans": 3.0,
            "banka": 4.0,
            "sigorta": 4.0
        }
    },
    emlak: {
        name: "Emlak ve Kiralama",
        puan: 1.0,
        altSektorler: ["emlak", "ticari"],
        altSektorPuanlar: {
            "emlak": 1.0,
            "ticari": 2.0
        }
    },
    kamu: {
        name: "Kamu Yönetimi ve Savunma",
        puan: 4.0,
        altSektorler: ["merkezi", "yerel", "savunma"],
        altSektorPuanlar: {
            "merkezi": 3.0,
            "yerel": 3.0,
            "savunma": 4.0
        }
    },
    egitim: {
        name: "Eğitim",
        puan: 2.0,
        altSektorler: ["okul öncesi", "temel", "ortaöğretim", "yükseköğretim", "yetişkin"],
        altSektorPuanlar: {
            "okul öncesi": 1.0,
            "temel": 1.0,
            "ortaöğretim": 1.0,
            "yükseköğretim": 1.0,
            "yetişkin": 1.0
        }
    },
    saglik: {
        name: "Sağlık ve Sosyal Hizmetler",
        puan: 3.0,
        altSektorler: ["sosyal", "saglik"],
        altSektorPuanlar: {
            "sosyal": 2.0,
            "saglik": 3.0
        }
    },
    sanat: {
        name: "Sanat ve Eğlence",
        puan: 2.0,
        altSektorler: ["eglence", "sanat"],
        altSektorPuanlar: {
            "eglence": 2.0,
            "sanat": 3.0
        }
    },
    diger: {
        name: "Diğer",
        puan: 1.0,
        altSektorler: ["kisisel", "diger", "profesyonel"],
        altSektorPuanlar: {
            "kisisel": 1.0,
            "diger": 1.0,
            "profesyonel": 2.0
        }
    },
    yazilim: {
        name: "Yazılım",
        puan: 4.0,
        altSektorler: ["yazilim"],
        altSektorPuanlar: {
            "yazilim": 4.0
        }
    }
};

// Ülke verilerini tanımlayalım
const ulkeData = {
    ulkeler: [
        "Albania", "Algeria", "Andorra", "Angola", "Argentina", "Armenia", "Aruba", "Australia", "Austria", "Azerbaijan",
        "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin", "Bermuda", "Bolivia",
        "Bosnia and Herzegovina", "Botswana", "Brazil", "Bulgaria", "Burkina Faso",
        "Cambodia", "Cameroon", "Canada", "Cape Verde", "Cayman Islands", "Chile", "China", "Colombia", "Congo",
        "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic",
        "Denmark", "Dominican Republic",
        "Ecuador", "Egypt", "El Salvador", "Estonia", "Ethiopia", "European Union",
        "Fiji", "Finland", "France",
        "Gabon", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala",
        "Honduras", "Hong Kong", "Hungary",
        "Iceland", "India", "Indonesia", "Iraq", "Ireland", "Isle of Man", "Israel", "Italy", "Ivory Coast",
        "Jamaica", "Japan", "Jordan",
        "Kazakhstan", "Kenya", "Kosovo", "Kuwait", "Kyrgyzstan",
        "Laos", "Latvia", "Lebanon", "Lesotho", "Liechtenstein", "Lithuania", "Luxembourg",
        "Macau", "Macedonia", "Madagascar", "Maldives", "Mali", "Malta", "Mauritius", "Mexico", "Moldova", "Mongolia",
        "Montenegro", "Morocco", "Mozambique", "Montserrat",
        "Namibia", "New Zealand", "Nicaragua", "Niger", "Nigeria", "Norway",
        "Oman",
        "Pakistan", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Puerto Rico",
        "Qatar",
        "Republic of the Congo", "Romania", "Russia", "Rwanda",
        "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Singapore", "Slovakia", "Slovenia", "Solomon Islands",
        "South Africa", "South Korea", "Spain", "Sri Lanka", "St Vincent and Grenadines", "Suriname", "Swaziland", "Sweden",
        "Switzerland",
        "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan",
        "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan",
        "Venezuela", "Vietnam",
        "Zambia"
    ]
};

// Ülke puanlama sistemi (gizli)
const ulkePuanlari = {
    // 4.0 Puanlık Ülkeler
    "Australia": 4.0, "Canada": 4.0, "Denmark": 4.0, "Germany": 4.0, "Liechtenstein": 4.0, "Luxembourg": 4.0, 
    "Switzerland": 4.0, "Norway": 4.0, "Sweden": 4.0, "European Union": 4.0, "Singapore": 4.0, "United States": 4.0, 
    "Austria": 4.0, "Finland": 4.0, "New Zealand": 4.0, "France": 4.0, "Taiwan": 4.0, "United Arab Emirates": 4.0, 
    "Hong Kong": 4.0, "Qatar": 4.0, "Belgium": 4.0, "Isle of Man": 4.0, "Macau": 4.0, "United Kingdom": 4.0, 
    "South Korea": 4.0, "Cayman Islands": 4.0, "Czech Republic": 4.0, "Estonia": 4.0, "Ireland": 4.0, "Kuwait": 4.0, 
    "Israel": 4.0, "Bermuda": 4.0, "China": 4.0, "Japan": 4.0, "Lithuania": 4.0, "Saudi Arabia": 4.0,

    // 3.0 Puanlık Ülkeler
    "Iceland": 3.0, "Malta": 3.0, "Slovakia": 3.0, "Slovenia": 3.0, "Chile": 3.0, "Latvia": 3.0, "Poland": 3.0, 
    "Spain": 3.0, "Portugal": 3.0, "Malaysia": 3.0, "Botswana": 3.0, "Andorra": 3.0, "Thailand": 3.0, "Croatia": 3.0, 
    "Italy": 3.0, "Bulgaria": 3.0, "Peru": 3.0, "Philippines": 3.0, "Uruguay": 3.0, "Cyprus": 3.0, "Hungary": 3.0, 
    "Indonesia": 3.0, "Mexico": 3.0, "Kazakhstan": 3.0, "India": 3.0, "Panama": 3.0, "Aruba": 3.0, "Colombia": 3.0, 
    "Mauritius": 3.0, "Montserrat": 3.0, "Romania": 3.0, "Greece": 3.0,

    // 2.0 Puanlık Ülkeler
    "Azerbaijan": 2.0, "Morocco": 2.0, "Oman": 2.0, "Trinidad and Tobago": 2.0, "Paraguay": 2.0, "Serbia": 2.0, 
    "Guatemala": 2.0, "Vietnam": 2.0, "Brazil": 2.0, "Georgia": 2.0, "Macedonia": 2.0, "San Marino": 2.0, 
    "Dominican Republic": 2.0, "Ivory Coast": 2.0, "South Africa": 2.0, "Seychelles": 2.0, "Armenia": 2.0, 
    "Bangladesh": 2.0, "Costa Rica": 2.0, "Uzbekistan": 2.0, "Albania": 2.0, "Bahamas": 2.0, "Honduras": 2.0, 
    "Namibia": 2.0, "Senegal": 2.0, "Jamaica": 2.0, "Jordan": 2.0, "Benin": 2.0, "Fiji": 2.0, "Turkmenistan": 2.0, 
    "Bahrain": 2.0, "Rwanda": 2.0, "Montenegro": 2.0, "Tanzania": 2.0, "Cambodia": 2.0, "Lesotho": 2.0, "Turkey": 2.0, 
    "Uganda": 2.0, "Zambia": 2.0, "Kenya": 2.0, "Mongolia": 2.0, "Nicaragua": 2.0, "Bosnia and Herzegovina": 2.0, 
    "Kyrgyzstan": 2.0, "Papua New Guinea": 2.0, "Togo": 2.0, "Barbados": 2.0,

    // 1.0 Puanlık Ülkeler
    "Angola": 1.0, "Cape Verde": 1.0, "Gabon": 1.0, "Madagascar": 1.0, "Moldova": 1.0, "Solomon Islands": 1.0, 
    "St Vincent and Grenadines": 1.0, "Swaziland": 1.0, "Tajikistan": 1.0, "Cameroon": 1.0, "Egypt": 1.0, 
    "Iraq": 1.0, "Nigeria": 1.0, "Congo": 1.0, "Maldives": 1.0, "Tunisia": 1.0, "Bolivia": 1.0, "Burkina Faso": 1.0, 
    "Ecuador": 1.0, "El Salvador": 1.0, "Mozambique": 1.0, "Pakistan": 1.0, "Republic of the Congo": 1.0, 
    "Belize": 1.0, "Ethiopia": 1.0, "Laos": 1.0, "Mali": 1.0, "Niger": 1.0, "Suriname": 1.0, "Russia": 1.0, 
    "Ukraine": 1.0, "Argentina": 1.0, "Belarus": 1.0, "Ghana": 1.0, "Sri Lanka": 1.0, "Venezuela": 1.0, 
    "Lebanon": 1.0, "Cuba": 1.0, "Puerto Rico": 1.0, "Grenada": 1.0, "Kosovo": 1.0
};

// Ülke puanını getiren fonksiyon
function getUlkePuani(ulke) {
    return ulkePuanlari[ulke] || 0.0; // Eğer ülke bulunamazsa 0.0 puan döner
}

// Sayfa yüklendiğinde çalışacak fonksiyonlar
document.addEventListener('DOMContentLoaded', function() {
    // Sektörleri doldur
    populateSektorler();
    // Ülkeleri doldur
    populateUlkeler();

    // Event listener'ları ekle
    document.getElementById('sektor').addEventListener('change', function() {
        updateAltSektor(this.value);
        updateCalisanAraliklari(this.value);
    });

    document.getElementById('hesapla').addEventListener('click', hesapla);
});

function populateSektorler() {
    const sektorSelect = document.getElementById('sektor');
    sektorSelect.innerHTML = '<option value="">Sektör Seçiniz</option>';
    
    for (const [key, value] of Object.entries(sektorData)) {
        const option = document.createElement('option');
        option.value = key;
        option.textContent = value.name;
        sektorSelect.appendChild(option);
    }
}

function populateUlkeler() {
    const ulkeSelect = document.getElementById('ulke');
    ulkeSelect.innerHTML = '<option value="">Ülke Seçiniz</option>';
    
    ulkeData.ulkeler.forEach(ulke => {
        const option = document.createElement('option');
        option.value = ulke;
        option.textContent = ulke;
        ulkeSelect.appendChild(option);
    });
}

function updateAltSektor(sektor) {
    const altSektorSelect = document.getElementById('altsektor');
    altSektorSelect.innerHTML = '<option value="">Alt Sektör Seçiniz</option>';

    if (sektor && sektorData[sektor]) {
        sektorData[sektor].altSektorler.forEach(altSektor => {
            const option = document.createElement('option');
            option.value = altSektor;
            option.textContent = altSektor.charAt(0).toUpperCase() + altSektor.slice(1);
            altSektorSelect.appendChild(option);
        });
    }
}

function getCalisanPuani(sektor, calisanSayisi) {
    if (["toptan", "diger", "perakende"].includes(sektor)) {
        if (calisanSayisi >= 1 && calisanSayisi <= 2) return 1.0;
        if (calisanSayisi >= 3 && calisanSayisi <= 5) return 2.0;
        if (calisanSayisi >= 6 && calisanSayisi <= 10) return 3.0;
        if (calisanSayisi >= 11) return 4.0;
    }
    else if (["tarim", "maden", "imalat", "elektrik", "sanat"].includes(sektor)) {
        if (calisanSayisi >= 1 && calisanSayisi <= 15) return 1.0;
        if (calisanSayisi >= 16 && calisanSayisi <= 40) return 2.0;
        if (calisanSayisi >= 41 && calisanSayisi <= 80) return 3.0;
        if (calisanSayisi >= 81) return 4.0;
    }
    else if (["lojistik", "konaklama", "yiyecek"].includes(sektor)) {
        if (calisanSayisi >= 1 && calisanSayisi <= 10) return 1.0;
        if (calisanSayisi >= 11 && calisanSayisi <= 50) return 2.0;
        if (calisanSayisi >= 51 && calisanSayisi <= 200) return 3.0;
        if (calisanSayisi >= 201) return 4.0;
    }
    else if (["egitim", "saglik"].includes(sektor)) {
        if (calisanSayisi >= 1 && calisanSayisi <= 50) return 1.0;
        if (calisanSayisi >= 51 && calisanSayisi <= 300) return 2.0;
        if (calisanSayisi >= 301 && calisanSayisi <= 500) return 3.0;
        if (calisanSayisi >= 501) return 4.0;
    }
    else if (["iletisim", "bilgi"].includes(sektor)) {
        if (calisanSayisi >= 1 && calisanSayisi <= 200) return 1.0;
        if (calisanSayisi >= 201 && calisanSayisi <= 1000) return 2.0;
        if (calisanSayisi >= 1001 && calisanSayisi <= 2000) return 3.0;
        if (calisanSayisi >= 2001) return 4.0;
    }
    else if (["kamu", "savunma"].includes(sektor)) {
        if (calisanSayisi >= 1 && calisanSayisi <= 1000) return 1.0;
        if (calisanSayisi >= 1001 && calisanSayisi <= 5000) return 2.0;
        if (calisanSayisi >= 5001 && calisanSayisi <= 10000) return 3.0;
        if (calisanSayisi >= 10001) return 4.0;
    }
    else if (["finans", "sigorta"].includes(sektor)) {
        if (calisanSayisi >= 1 && calisanSayisi <= 100) return 1.0;
        if (calisanSayisi >= 101 && calisanSayisi <= 500) return 2.0;
        if (calisanSayisi >= 501 && calisanSayisi <= 1000) return 3.0;
        if (calisanSayisi >= 1001) return 4.0;
    }
    return 1.0; // Varsayılan puan
}

function hesapla() {
    // Form verilerini al
    const sektor = document.getElementById('sektor').value;
    const altSektor = document.getElementById('altsektor').value;
    const calisanSayisi = parseInt(document.getElementById('calisan').value);
    const sirketYasi = parseFloat(document.getElementById('yas').value);
    const ulke = document.getElementById('ulke').value;
    const musteriDurumu = document.querySelector('input[name="musteri"]:checked').value;

    // Diğer parametreleri hesapla
    const sektorPuan = sektorData[sektor].puan;
    const altSektorPuan = sektorData[sektor].altSektorPuanlar[altSektor];
    const calisanPuan = getCalisanPuani(sektor, calisanSayisi);
    const yasPuan = getYasPuani(sirketYasi);
    const ulkePuan = getUlkePuani(ulke);
    const musteriPuan = musteriDurumu === 'evet' ? 1.0 : 0.0;
    const buyumePuan = 2.5;

    // Diğer parametreler toplamı (maksimum 25 puan)
    const digerParametreler = (sektorPuan + altSektorPuan + calisanPuan + yasPuan + ulkePuan + musteriPuan + buyumePuan);

    // Finansal veriler
    const toplamVarlik = parseFloat(document.getElementById('toplamVarlik').value);
    const netSermaye = parseFloat(document.getElementById('netSermaye').value);
    const dagitilmamisKar = parseFloat(document.getElementById('dagitilmamisKar').value);
    const satislar = parseFloat(document.getElementById('satislar').value);
    const calismaSermayesi = parseFloat(document.getElementById('calismaSermayesi').value);
    const faizOncesiKar = parseFloat(document.getElementById('faizOncesiKar').value);
    const vergiOncesiKar = parseFloat(document.getElementById('vergiOncesiKar').value);
    const kisaVadeliYukumlulukler = parseFloat(document.getElementById('kisaVadeliYukumlulukler').value);

    // Finansal hesaplamalar
    const degisken1 = ((netSermaye / toplamVarlik) * 1.2);
    const degisken2 = ((dagitilmamisKar / toplamVarlik) * 1.4);
    const degisken3 = ((satislar / toplamVarlik) * 1.21);
    const degisken4 = ((calismaSermayesi / toplamVarlik) * 1.05);
    const degisken5 = ((faizOncesiKar / toplamVarlik) * 2.33);
    const degisken6 = ((vergiOncesiKar / kisaVadeliYukumlulukler) * 0.66);

    const finansalSkor = (degisken1 + degisken2 + degisken3 + degisken4 + degisken5 + degisken6);
    const toplamSkor = finansalSkor * digerParametreler;

    // Sonuç metnini oluştur
    let sonucMetni = `
        <div class="sonuc-baslik">ŞİRKET SKOR SONUCU</div>
        <div class="sonuc-detay">
            <div class="sonuc-grup">
                <h3>Şirket Bilgileri</h3>
                <p>Sektör: ${sektorData[sektor].name}</p>
                <p>Alt Sektör: ${altSektor}</p>
                <p>Çalışan Sayısı: ${calisanSayisi}</p>
                <p>Şirket Yaşı: ${sirketYasi} yıl</p>
                <p>Ülke: ${ulke}</p>
                <p>Müşteri Durumu: ${musteriDurumu}</p>
            </div>
            
            <div class="sonuc-grup">
                <h3>Hesaplanan Puanlar</h3>
                <p>Sektör Puanı: ${sektorPuan.toFixed(2)}</p>
                <p>Alt Sektör Puanı: ${altSektorPuan.toFixed(2)}</p>
                <p>Çalışan Puanı: ${calisanPuan.toFixed(2)}</p>
                <p>Yaş Puanı: ${yasPuan.toFixed(2)}</p>
                <p>Ülke Puanı: ${ulkePuan.toFixed(2)}</p>
                <p>Müşteri Puanı: ${musteriPuan.toFixed(2)}</p>
                <p>Büyüme Puanı: ${buyumePuan.toFixed(2)}</p>
            </div>

            <div class="sonuc-grup">
                <h3>Nihai Sonuçlar</h3>
                <p>Diğer Parametreler Toplamı: ${digerParametreler.toFixed(2)}</p>
                <p>Finansal Skor: ${finansalSkor.toFixed(2)}</p>
                <p class="toplam-skor">TOPLAM SKOR: ${toplamSkor.toFixed(2)}</p>
            </div>
        </div>
    `;

    // Sonuçları göster
    const sonuclarDiv = document.getElementById('sonuclar');
    sonuclarDiv.style.display = 'block';
    sonuclarDiv.innerHTML = sonucMetni;
}

// Şirket yaşı puanı hesaplama
function getYasPuani(yas) {
    if (yas <= 3) return 1.0;
    if (yas <= 10) return 2.0;
    if (yas <= 30) return 3.0;
    return 4.0;
}

// Çalışan sayısı puanı hesaplama
function getCalisanPuani(sektor, calisanSayisi) {
    if (["toptan", "diger", "perakende"].includes(sektor)) {
        if (calisanSayisi >= 1 && calisanSayisi <= 2) return 1.0;
        if (calisanSayisi >= 3 && calisanSayisi <= 5) return 2.0;
        if (calisanSayisi >= 6 && calisanSayisi <= 10) return 3.0;
        if (calisanSayisi >= 11) return 4.0;
    }
    else if (["tarim", "maden", "imalat", "elektrik", "sanat"].includes(sektor)) {
        if (calisanSayisi >= 1 && calisanSayisi <= 15) return 1.0;
        if (calisanSayisi >= 16 && calisanSayisi <= 40) return 2.0;
        if (calisanSayisi >= 41 && calisanSayisi <= 80) return 3.0;
        if (calisanSayisi >= 81) return 4.0;
    }
    else if (["lojistik", "konaklama", "yiyecek"].includes(sektor)) {
        if (calisanSayisi >= 1 && calisanSayisi <= 10) return 1.0;
        if (calisanSayisi >= 11 && calisanSayisi <= 50) return 2.0;
        if (calisanSayisi >= 51 && calisanSayisi <= 200) return 3.0;
        if (calisanSayisi >= 201) return 4.0;
    }
    else if (["egitim", "saglik"].includes(sektor)) {
        if (calisanSayisi >= 1 && calisanSayisi <= 50) return 1.0;
        if (calisanSayisi >= 51 && calisanSayisi <= 300) return 2.0;
        if (calisanSayisi >= 301 && calisanSayisi <= 500) return 3.0;
        if (calisanSayisi >= 501) return 4.0;
    }
    else if (["iletisim", "bilgi"].includes(sektor)) {
        if (calisanSayisi >= 1 && calisanSayisi <= 200) return 1.0;
        if (calisanSayisi >= 201 && calisanSayisi <= 1000) return 2.0;
        if (calisanSayisi >= 1001 && calisanSayisi <= 2000) return 3.0;
        if (calisanSayisi >= 2001) return 4.0;
    }
    else if (["kamu", "savunma"].includes(sektor)) {
        if (calisanSayisi >= 1 && calisanSayisi <= 1000) return 1.0;
        if (calisanSayisi >= 1001 && calisanSayisi <= 5000) return 2.0;
        if (calisanSayisi >= 5001 && calisanSayisi <= 10000) return 3.0;
        if (calisanSayisi >= 10001) return 4.0;
    }
    else if (["finans", "sigorta"].includes(sektor)) {
        if (calisanSayisi >= 1 && calisanSayisi <= 100) return 1.0;
        if (calisanSayisi >= 101 && calisanSayisi <= 500) return 2.0;
        if (calisanSayisi >= 501 && calisanSayisi <= 1000) return 3.0;
        if (calisanSayisi >= 1001) return 4.0;
    }
    return 1.0; // Varsayılan puan
} 