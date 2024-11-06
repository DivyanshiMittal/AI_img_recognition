# Code to capture images (need to install OpenCV)
import cv2

# Initialize the camera
camera = cv2.VideoCapture(0)

while True:
    # Capture a frame from the camera
    ret, frame = camera.read()

    # Display the frame for user to capture a signature
    cv2.imshow("Capture Signature", frame)

    # Press 'q' to capture the signature
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("signature.jpg", frame)
        break

# Release the camera
camera.release()
cv2.destroyAllWindows()
