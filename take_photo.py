import sys
import os

print("\n--- PROGRAM BASLATILDI ---")
print("[1/4] Moduller kontrol ediliyor...")

try:
    import cv2
    print(f" -> OpenCV yüklü. (Sürüm: {cv2.__version__})")
except ImportError:
    print(" HATA: 'opencv-python' yüklü değil! Terminale 'pip install opencv-python' yazın.")
    sys.exit(1)

print("[2/4] Kamera başlatılıyor...")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print(" HATA: Kamera açılamadı! Başka bir uygulamanın kamerayı kullanmadığından emin olun.")
    sys.exit(1)

print("[3/4] Kamera açıldı, test görüntüsü alınıyor...")
ret, frame = cap.read()

if not ret or frame is None:
    print(" HATA: Kameradan görüntü alınamıyor!")
    cap.release()
    sys.exit(1)

print("[4/4] Görüntü alma başarılı! Pencere açılıyor...")
print("\n" + "="*45)
print("  FOTOĞRAF ÇEKMEK İÇİN : [SPACE / BOŞLUK]")
print("  ÇIKIŞ YAPMAK İÇİN    : [Q]")
print("="*45 + "\n")

img_counter = 0

try:
    while True:
        ret, frame = cap.read()
        if not ret or frame is None:
            continue

        # Siyah-beyaz yap
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Pencerede göster
        cv2.imshow("Siyah Beyaz Kamera", gray_frame)

        key = cv2.waitKey(1) & 0xFF

        # 'q' ile çık
        if key == ord('q'):
            print("Çıkış yapılıyor...")
            break
        
        # Space ile kaydet
        elif key == 32:
            img_name = f"siyah_beyaz_foto_{img_counter}.png"
            cv2.imwrite(img_name, gray_frame)
            tam_yol = os.path.abspath(img_name)
            print(f"[KAYDEDİLDİ]: {tam_yol}")
            img_counter += 1

except Exception as e:
    print(f"Bir çalışma hatası oluştu: {e}")

finally:
    cap.release()
    cv2.destroyAllWindows()
    print("Program kapatıldı.")