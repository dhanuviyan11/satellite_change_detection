import cv2
import numpy as np
import matplotlib.pyplot as plt

def align_images(reference, target):
    gray_ref=cv2.cvtColor(reference, cv2.COLOR_BGR2GRAY)
    gray_target=cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)

    orb=cv2.ORB_create(5000)

    kp1, des1=orb.detectAndCompute(gray_ref, None)
    kp2, des2=orb.detectAndCompute(gray_target, None)

    matcher=cv2.BFMatcher(cv2.NORM_HAMMING)
    matches = matcher.knnMatch(des1, des2, k=2)

    good_matches = []

    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    print("Good Matches:", len(good_matches))

    points_ref=np.zeros((len(good_matches), 2), dtype=np.float32)
    points_target=np.zeros((len(good_matches), 2), dtype=np.float32)

    for i, match in enumerate(good_matches):
        points_ref[i]=kp1[match.queryIdx].pt
        points_target[i]=kp2[match.trainIdx].pt

    H, _=cv2.findHomography(points_target, points_ref, cv2.RANSAC)
    height, width=reference.shape[:2]
    aligned=cv2.warpPerspective(target, H, (width, height))
    return aligned