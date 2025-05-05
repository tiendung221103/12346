import cv2

cam = cv2.VideoCapture(0)
cam.set(3, 1920)  # Set width
cam.set(4, 1080)  # Set height

while True:
    ret, frame = cam.read()
    if not ret:
        break

    cv2.imshow("Camera Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()

