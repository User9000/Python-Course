import cv2

img=cv2.imread("Penguins.jpg",0)

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

cv2.imshow("Penguins",img)
cv2.waitKey(2000)
cv2.destroyAllWindows()