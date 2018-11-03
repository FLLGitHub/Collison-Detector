import cv2
import numpy as np
import Image
from matplotlib import pyplot as plt

#lightens the image for better edges
original = Image.open("diff1.png")
lightened = original.point(lambda p: p * 0.9)
im2.save("lightened_difference.png")

img = cv2.imread('lightened_difference.png',0)
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'white')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'white')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
