import cv2
import matplotlib.pyplot as plt
import os

# 1. Dosya yolu ve parça isimleri
folder_path = r"C:\Users\Casper\Desktop\28_09"
part_files = [
    "part_1_top_left.png",
    "part_2_top_right.png",
    "part_3_bottom_left.png",
    "part_4_bottom_right.png"
]

print("="*50)
print(" HISTOGRAM AND INTENSITY PIXEL ANALYSIS")
print("="*50)

plt.figure(figsize=(12, 8))

for i, filename in enumerate(part_files, 1):
    file_path = os.path.join(folder_path, filename)
    
    if not os.path.exists(file_path):
        print(f"ERROR: File '{file_path}' not found! Please run 'image_splitter.py' first.")
        continue

    # Parçayı gri tonlamalı okuyoruz
    part_img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

    # 0-255 arası parlaklık değerlerinin piksel sayılarını hesaplama
    hist = cv2.calcHist([part_img], [0], None, [256], [0, 256])

    # Terminal çıktısı
    print(f"\n--- Analysis for {filename} ---")
    print(f"Total Pixels               : {part_img.size}")
    print(f" - Black Pixels (Value 0)   : {int(hist[0][0])}")
    print(f" - Mid-Gray Pixels (Value 128): {int(hist[128][0])}")
    print(f" - White Pixels (Value 255) : {int(hist[255][0])}")

    # Grafik Çizimi
    plt.subplot(2, 2, i)
    plt.plot(hist, color='black')
    plt.title(filename)
    plt.xlabel('Brightness Level (0-255)')
    plt.ylabel('Pixel Count')
    plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
output_chart_path = os.path.join(folder_path, "histogram_results.png")
plt.savefig(output_chart_path)
print(f"\nHistogram chart saved to: {output_chart_path}")
plt.show()