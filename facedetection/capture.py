import cv2
import time
"""

VideoCapture() / pass the index  of the camera, or a video file.

"""
video=cv2.VideoCapture(0)

check,frame= video.read()

print(check)
print(frame)

time.sleep(3)
cv2.imshow("Capturing",frame)

cv2.waitKey(0)
video.release()
cv2.destroyAllWindows

