import cv2
import matplotlib.pyplot as plt
import numpy as np
img=cv2.imread("image.png")
print(img.shape)
print(img)
"""np.save("image_data.npy",img)
load_img=np.load("image_data.npy")
cv2.imwrite("recreate.png",load_img)"""
