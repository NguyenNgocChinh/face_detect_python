from genericpath import exists
import cv2
import numpy as np
import os
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()

path = 'dataset'


def getImageWithId(path):
    user_path = [os.path.join(path, f) for f in os.listdir(path)]
    IDs = []
    faces = []

    for user in user_path:
        image_paths = [os.path.join(user, f) for f in os.listdir(user)]
        for image_path in image_paths:
            faceImg = Image.open(image_path).convert('L')
            faceNp = np.array(faceImg, 'uint8')
            id = int(os.path.split(user)[1])
            faces.append(faceNp)
            IDs.append(id)
            cv2.imshow('Training', faceNp)
            cv2.waitKey(10)
    return IDs, faces


print("\n [INFO] Training faces. It will take a few  seconds. Wait ...")
Ids, faces = getImageWithId(path)

recognizer.train(faces, np.array(Ids))

if not os.path.exists('recognizer'):
    os.makedirs('recognizer')

recognizer.save('recognizer/model.yml')

cv2.destroyAllWindows()

print("\n [INFO] {0} faces trained. Exiting Program".format(
    len(np.unique(Ids))))
