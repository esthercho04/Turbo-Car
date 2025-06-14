import cv2

cap = cv2.VideoCapture(0, cv2.CAP_V4L2)  # <== FORCES V4L2 backend

if not cap.isOpened():
    print("? Camera failed to open.")
else:
    ret, frame = cap.read()
    if ret:
        print("? Camera test successful. Frame captured.")
    else:
        print("? Failed to capture frame.")

cap.release()
