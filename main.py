import cv2
from src.image_loader import load_image
from src.preprocessing import to_grayscale, gaussian_blur, equalize
import matplotlib.pyplot as plt
import src.change_detector as cd
from src.config import MIN_CONTOUR_AREA
from src.alignment import align_images

before_path="data/before/vizhinjam_2018.jpg"
after_path="data/after/vizhinjam_2025.jpg"

before=load_image(before_path)
after=load_image(after_path)
after=align_images(before, after)

if before.shape != after.shape:
    raise ValueError("The two images must have the same dimensions")

print("Before shape:", before.shape)
print("After shape:", after.shape)

gray_before=to_grayscale(before)
gray_after=to_grayscale(after)

gray_before=gaussian_blur(gray_before)
gray_after=gaussian_blur(gray_after)

gray_before=equalize(gray_before)
gray_after=equalize(gray_after)

difference=cd.compute_difference(gray_before, gray_after)
binary_change=cd.threshold_difference(difference)

cleaned_change=cd.remove_noise(binary_change)
percentage=cd.calculate_change_percentage(cleaned_change)
print(f'Area Changed: {percentage:.2f}%')

contours=cd.find_change_contours(cleaned_change)
print(f"Total Contours: {len(contours)}")
significant_regions=0
for contour in contours:
    if cv2.contourArea(contour) > MIN_CONTOUR_AREA:
        significant_regions+=1
print("Significant Regions: ", significant_regions)
boxed_image=cd.draw_change_boxes(after, contours)
cv2.putText(boxed_image, f'Changed:{percentage}%', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
boxed_image_rgb=cv2.cvtColor(boxed_image, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(18, 5))
plt.subplot(1, 5, 1)
plt.imshow(gray_before, cmap='gray')
plt.title('Before')
plt.axis('off')

plt.subplot(1, 5, 2)
plt.imshow(gray_after, cmap='gray')
plt.title('After')
plt.axis('off')

plt.subplot(1, 5, 3)
plt.imshow(difference, cmap='gray')
plt.title('Difference Map')
plt.axis('off')

plt.subplot(1, 5, 4)
plt.imshow(binary_change, cmap='gray')
plt.title('Detected Changes')
plt.axis('off')

plt.subplot(1, 5, 5)
plt.imshow(boxed_image_rgb)
plt.title('Detected Regions')
plt.axis('off')

plt.tight_layout()
plt.show()