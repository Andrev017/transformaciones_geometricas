img = cv2.imread('/img1.jpg',0)
rows,cols = img.shape
 
M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
dst = cv2.warpAffine(img,M,(cols,rows))