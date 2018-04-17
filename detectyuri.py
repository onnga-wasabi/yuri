import numpy as np
import cv2
from pathlib import Path
import sys


def main():
    cascade = cv2.CascadeClassifier('model.xml')
    color = (0, 0, 255)
    p = Path('./data')
    imgs = [fname for fname in p.iterdir() if not fname.name == '.gitkeep']
    for img in imgs:
        image = cv2.imread(str(img), 1)
        if image is not None:
            facerect = cascade.detectMultiScale(image)
            if len(facerect) > 0:
                for rect in facerect:
                    cv2.rectangle(image,
                                  tuple(rect[0:2]),
                                  tuple(rect[0:2] + rect[2:4]),
                                  color)
            out = 'data2/' + img.name
            cv2.imwrite('data2/' + img.name, image)

    return 0


if __name__ == '__main__':
    main()
