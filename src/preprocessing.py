import cv2

def to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
def gaussian_blur(image):
    return cv2.GaussianBlur(image, (5, 5), 0)
def equalize(image):
    return cv2.equalizeHist(image)