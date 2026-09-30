import cv2
import os
import time

cap = cv2.VideoCapture(0)

labels = {
    ord('1'): 'A',
    ord('2'): 'B',
    ord('3'): 'C',
    ord('4'): 'D',
    ord('5'): 'E'
}

current_label = 'A'

capturing = False
last_capture_time = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    cv2.rectangle(frame, (300,100), (600,400), (0,255,0), 2)

    folder = f"dataset/{current_label}"
    count = len(os.listdir(folder))

    cv2.putText(
        frame,
        f"Label: {current_label}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    cv2.putText(
        frame,
        f"Images: {count}",
        (20,80),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    status = "ON" if capturing else "OFF"

    cv2.putText(
        frame,
        f"Capture: {status}",
        (20,120),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    if capturing:

        current_time = time.time()

        if current_time - last_capture_time > 0.2:

            roi = frame[100:400, 300:600]

            filename = os.path.join(
                folder,
                f"{count}.jpg"
            )

            cv2.imwrite(filename, roi)

            last_capture_time = current_time

    cv2.imshow("Dataset Collection", frame)

    key = cv2.waitKey(1)
    print(key)
    

    if key in labels:
        current_label = labels[key]

    elif key == ord('c'):
        capturing = not capturing

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()