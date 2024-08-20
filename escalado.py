import numpy as np
import matplotlib.pyplot as plt #carga la librería para graficar
import cv2

 
img = cv2.imread('/img1.jpg')
rows,cols,ch = img.shape

pts1 = np.float32([[100,400],[400,100],[100,100]])
pts2 = np.float32([[50,300],[400,200],[80,150]])

M = cv2.getAffineTransform(pts1,pts2)
dst = cv2.warpAffine(img,M,(cols,rows))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()