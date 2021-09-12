import cv2
import dlib

# Load detector
detector = dlib.get_frontal_face_detector()

# Read video capture
camera_id = 0

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:

    ret, frame = capture.read()

    if ret:
        # Convert video capture to gray
        gray_image = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)

        # Use detector
        faces = detector(gray_image)

        # Loop through all faces
        for face in faces:
            x1 = face.left()
            y1 = face.top()
            x2 = face.right()
            y2 = face.bottom()

            # Draw a rectagle
            cv2.rectangle(img=frame, pt1=(x1, y1), pt2=(
                x2, y2), color=(0, 255, 0), thickness=3)

        cv2.imshow(winname='Detector faces realtime', mat=frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
