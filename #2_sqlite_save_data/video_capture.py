from os import path
import cv2
import dlib
from dir_worker import check_or_make_fir
from repositories import DB


class VideoCapture:

    detector = None
    camera_id = 0
    capture = None
    db = None

    def __init__(self, camera_id=0):
        # Load detector
        self.detector = dlib.get_frontal_face_detector()
        # Load database
        self.db = DB('people.db')
        # Read video capture
        self.camera_id = camera_id
        self.capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    def video_capture(self):
        id = input('Nhập vào ID: ')
        name = input('Nhập vào tên: ')
        birthday = input('Nhập vào năm sinh: ')
        if len(self.db.select('id', id)) < 1:
            self.db.insert(id, name, birthday)
        else:
            self.db.update(id, name, birthday)
        sample_num = 1
        while True:

            ret, frame = self.capture.read()
            if ret:
                # Convert video capture to gray
                gray_image = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)

                # Use detector
                faces = self.detector(gray_image)

                # Loop through all faces
                for face in faces:
                    x1 = face.left()
                    y1 = face.top()
                    x2 = face.right()
                    y2 = face.bottom()

                    self.save_face(
                        image=frame[y1: y2, x1: x2], path=f'dataset/{id}', sample_num=sample_num)

                    # Draw a rectagle
                    cv2.rectangle(img=frame, pt1=(x1, y1), pt2=(
                        x2, y2), color=(0, 255, 0), thickness=3)

                cv2.imshow(winname='Detector faces realtime', mat=frame)

            key = cv2.waitKey(1)
            if key == ord('q'):
                break

            if sample_num > 100:
                break

            sample_num += 1

        self.capture.release()
        cv2.destroyAllWindows()

    def save_face(self, image, path, sample_num):
        check_or_make_fir(path)
        path_img = path + '/' + str(sample_num) + '.png'
        cv2.imwrite(path_img, image)


if __name__ == '__main__':
    capture = VideoCapture(0)
    capture.video_capture()
