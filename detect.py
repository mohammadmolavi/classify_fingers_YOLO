from ultralytics import YOLO
import cv2


model = YOLO('best (1).pt')

cap = cv2.VideoCapture(0)

for i in range(100000):
    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray,(128,128))
    cv2.imwrite('1.jpg', gray)
    class_pred = model.predict('1.jpg')[0].boxes.cls.tolist()

    print(img.shape)
    start_point = (37, 32)

    # Ending coordinate, here (220, 220)
    # represents the bottom right corner of rectangle
    end_point = (93, 95)

    # Blue color in BGR
    color = (255, 0, 0)

    # Line thickness of 2 px
    thickness = 2

    # Using cv2.rectangle() method
    # Draw a rectangle with blue line borders of thickness of 2 px
    img = cv2.resize(img, (128,128))
    img = cv2.rectangle(img, start_point, end_point, color, thickness)


    font = cv2.FONT_HERSHEY_SIMPLEX

    org = (50, 50)

    fontScale = 1

    color = (255, 0, 0)

    thickness = 2
    try:
        for j in class_pred:
            img = cv2.putText(img, str(j%6), org, font, fontScale, color, thickness, cv2.LINE_AA)
    except:
        pass

    cv2.imshow('live', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break