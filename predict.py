import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load trained model
model = load_model("sign_language_model.keras")

# Labels
labels = ['A', 'B', 'C', 'D', 'E']

# Webcam
cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    # ROI Box
    cv2.rectangle(
        frame,
        (300, 100),
        (600, 400),
        (0, 255, 0),
        2
    )

    roi = frame[100:400, 300:600]

    # Preprocessing
    img = cv2.resize(roi, (64, 64))

    img = img.astype("float32") / 255.0

    img = np.expand_dims(img, axis=0)

    # Prediction
    prediction = model.predict(
        img,
        verbose=0
    )

    predicted_class = np.argmax(prediction)

    confidence = np.max(prediction)

    predicted_letter = labels[predicted_class]

    # Show Prediction
    cv2.putText(
        frame,
        f"{predicted_letter} ({confidence:.2f})",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow(
        "Sign Language Recognition",
        frame
    )

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()