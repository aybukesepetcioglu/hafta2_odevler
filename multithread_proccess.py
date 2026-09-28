import cv2
import numpy as np
import time
from concurrent.futures import ThreadPoolExecutor

# Thread'lerin (İş parçacıklarının) çalıştıracağı fonksiyon
def parcayi_islemden_gecir(img_chunk):
    # Siyah-beyaz dönüşümü
    return cv2.cvtColor(img_chunk, cv2.COLOR_BGR2GRAY)

if __name__ == '__main__':
    # 1. BÜYÜK BİR TEST RESMİ OLUŞTUR (Veya var olan resmi yükle: img = cv2.imread('foto.jpg'))
    print("Test resmi oluşturuluyor (4000x4000 piksellik büyük bir resim)...")
    img = np.random.randint(0, 256, (4000, 4000, 3), dtype=np.uint8)
    
    # N = Bölünecek parça ve oluşturulacak Thread sayısı
    N = 4  # Örneğin 4 parçaya bölüp 4 thread'e veriyoruz
    print(f"Parça ve Thread Sayısı (N): {N}\n")

    # ==========================================
    # 1. YÖNTEM: TEK THREAD (NORMAL) İŞLEME
    # ==========================================
    start_time = time.time()
    
    # Tek seferde resmi dönüştür
    _ = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    tek_thread_suresi = time.time() - start_time
    print(f"[TEK THREAD / NORMAL] Süre: {tek_thread_suresi:.4f} saniye")

    # ==========================================
    # 2. YÖNTEM: N PARÇAYA BÖLÜP N THREAD İLE İŞLEME
    # ==========================================
    start_time = time.time()

    # Resmi yatay olarak N eşit parçaya böl
    img_chunks = np.array_split(img, N, axis=0)

    # N tane Thread'den oluşan havuz oluştur
    with ThreadPoolExecutor(max_workers=N) as executor:
        # Parçaları eş zamanlı (parallel/concurrent) olarak Thread'lere dağıt
        processed_chunks = list(executor.map(parcayi_islemden_gecir, img_chunks))

    # İşlenen N parçayı dikey olarak birleştirip orijinal resmi oluştur
    islenmis_resim = np.vstack(processed_chunks)

    coklu_thread_suresi = time.time() - start_time
    print(f"[{N} THREAD İLE PARALEL] Süre: {coklu_thread_suresi:.4f} saniye")

    # ==========================================
    # SONUÇ VE PERFORMANS FARKIDIR
    # ==========================================
    fark = tek_thread_suresi - coklu_thread_suresi
    print(f"\nSonuç: {N} Thread kullanıldığında işlem {fark:.4f} saniye daha hızlı bitti.")