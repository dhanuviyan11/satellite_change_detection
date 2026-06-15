try:
    import cv2
except ModuleNotFoundError as e:
    raise ImportError(
        "OpenCV (cv2) is not installed. Install it with `pip install opencv-python` or `pip install opencv-python-headless`"
    ) from e
from src.config import THRESHOLD_VALUE, MIN_CONTOUR_AREA
import numpy as np

def compute_difference(img1, img2):
    return cv2.absdiff(img1, img2)
def threshold_difference(diff, threshold=THRESHOLD_VALUE):
    _, binary=cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)
    return binary
def find_change_contours(binary_image):
    contours, _=cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours
def remove_noise(binary_image):
    kernel = np.ones((9, 9), np.uint8)
    # Morphological opening followed by closing to remove small noise and fill small holes
    cleaned = cv2.morphologyEx(binary_image, cv2.MORPH_OPEN, kernel)
    return cleaned
def draw_change_boxes(image, contours):
    output=image.copy()
    for contour in contours:
        if cv2.contourArea(contour) > MIN_CONTOUR_AREA:
            x, y, w, h=cv2.boundingRect(contour)
            cv2.rectangle(output, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return output
def calculate_change_percentage(binary_image):
    changed_pixels=cv2.countNonZero(binary_image)
    total_pixels=(binary_image.shape[0]*binary_image.shape[1])
    percentage=(changed_pixels/total_pixels)*100
    return percentage