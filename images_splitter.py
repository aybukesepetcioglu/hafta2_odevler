import cv2
import os

# 1. Dosya yolu ve dosya adı tanımlamaları
folder_path = r"C:\Users\Casper\Desktop\28_09"
file_name = "images.jpg"
full_image_path = os.path.join(folder_path, file_name)

print(f"Loading image from: {full_image_path}")

# 2. Fotoğrafı Yükle
img = cv2.imread(full_image_path)

if img is None:
    print(f"ERROR: Could not find or open the image at '{full_image_path}'.")
    print("Please make sure 'images.jpg' exists in 'C:\\Users\\Casper\\Desktop\\28_09'.")
    exit(1)

# 3. Siyah-Beyaz (Gri Tonlama) Dönüşümü
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grayscale_save_path = os.path.join(folder_path, "grayscale_full.png")
cv2.imwrite(grayscale_save_path, gray_img)
print(f"Grayscale full image saved to: {grayscale_save_path}")

# 4. Resmi 4 Eşit Parçaya Böl (2x2 Izgara)
height, width = gray_img.shape
mid_y = height // 2
mid_x = width // 2

part1 = gray_img[0:mid_y, 0:mid_x]          # Top-Left
part2 = gray_img[0:mid_y, mid_x:width]      # Top-Right
part3 = gray_img[mid_y:height, 0:mid_x]      # Bottom-Left
part4 = gray_img[mid_y:height, mid_x:width]  # Bottom-Right

# 5. Parçaları Klasöre Kaydet
parts = [
    ("part_1_top_left.png", part1),
    ("part_2_top_right.png", part2),
    ("part_3_bottom_left.png", part3),
    ("part_4_bottom_right.png", part4)
]

print("\nSplitting image into 4 equal parts...")
for file_title, part_data in parts:
    save_path = os.path.join(folder_path, file_title)
    cv2.imwrite(save_path, part_data)
    print(f" -> Saved: {save_path}")

print("\nProcess completed successfully!")