import os
import cv2


for i in os.listdir():
	if ".jpg" in i:
		img=cv2.imread(i,0)
		resized_image=cv2.resize(img,(100,100))
		cv2.imwrite(str(os.path.splitext(i)[0]+"_resized.jpg"), resized_image)
		