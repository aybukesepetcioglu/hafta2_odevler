import cv2
import numpy as np
import time
from concurrent.futures import ThreadPoolExecutor

# Ağır bir görüntü işleme fonksiyonu (Örn: Ağır Gaussian Blur)
def agir_islem(img_chunk):
    # Ağır bir filtre uyguluyoruz ki Thread'lerin farkı ortaya çıksın
    return cv2.GaussianBlur(img_chunk, (51, 51), 0)

if __name__ == '__main__':
    # 1. DEVASA RESİM OLUŞTUR (8000x8000 piksel)
    print("Çok büyük test resmi oluşturuluyor (8000x8000)...")
    img = np.random.randint(0, 256, (8000, 8000, 3), dtype=np.uint8)
    
    N = 4 # Thread / Parça sayısı

    # TEK THREAD
    t0 = time.time()
    _ = agir_islem(img)
    tek_süre = time.time() - t0
    print(f"Tek Thread Süresi    : {tek_süre:.4f} saniye")

    # ÇOKLU THREAD (N PARÇA)
    t0 = time.time()
    img_chunks = np.array_split(img, N, axis=0)
    
    with ThreadPoolExecutor(max_workers=N) as executor:
        processed_chunks = list(executor.map(agir_islem, img_chunks))
        
    _ = np.vstack(processed_chunks)
    coklu_süre = time.time() - t0
    print(f"{N} Thread (Paralel)    : {coklu_süre:.4f} saniye")