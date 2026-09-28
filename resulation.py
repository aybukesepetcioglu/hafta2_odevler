import cv2

# Seninkine göre ayarlanan bilgiler
DOSYA_YOLU = r"C:\Users\Casper\Desktop\WhatsApp Image 2026-09-28 at 09.32.49.jpeg"
GENISLIK   = 1600
YUKSEKLIK  = 1066

# Resmi Yükle
img = cv2.imread(DOSYA_YOLU)

if img is None:
    print("HATA: Görsel belirtilen yolda bulunamadı! Dosya yolunu veya adını kontrol et.")
else:
    carpanlar = {
        "x0.25": 0.25,
        "x0.5":  0.5,
        "x2":    2.0,
        "x4":    4.0
    }

    print("İşlem başlatılıyor...\n")

    for etiket, carpan in carpanlar.items():
        # Yeni boyutları hesapla
        yeni_w = int(GENISLIK * carpan)
        yeni_h = int(YUKSEKLIK * carpan)

        # Küçültürken INTER_AREA, büyütürken INTER_CUBIC
        yontem = cv2.INTER_AREA if carpan < 1.0 else cv2.INTER_CUBIC

        # Boyutlandır
        yeni_resim = cv2.resize(img, (yeni_w, yeni_h), interpolation=yontem)

        # Masaüstüne kaydetmek üzere dosya adı oluştur
        kayit_adi = f"C:\\Users\\Casper\\Desktop\\sonuc_{etiket}_{yeni_w}x{yeni_h}.jpg"
        cv2.imwrite(kayit_adi, yeni_resim)

        print(f"-> {etiket} boyutu tamamlandı: {yeni_w}x{yeni_h} px")

    print("\n[BAŞARILI] Tüm çözünürlükler Masaüstüne kaydedildi!")


    #bu hafta istenilen rasbery pi'm yok eski bilgisayarların kamerası  