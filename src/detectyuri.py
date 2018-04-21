import numpy as np
import cv2
from pathlib import Path
import sys


def main():
    cascade = cv2.CascadeClassifier('models/model.xml')
    p = Path('../data/' + DNAME)
    imgs = [fname for fname in p.iterdir() if not fname.name == '.gitkeep']
    i = 0
    for img in imgs:
        image = cv2.imread(str(img), 1)
        facerect = cascade.detectMultiScale(image, minSize=(200, 200))
        if len(facerect) > 0:
            for rect in facerect:
                y = rect[1]
                yy = y + rect[3]
                x = rect[0]
                xx = x + rect[2]
                fname = str(i) + '.png'
                fname = '../cropped/' + DNAME + '/' + fname
                cv2.imwrite(fname, image[y:yy, x:xx])
                i += 1
    return 0


if __name__ == '__main__':
    DNAME = 'fc2'
    main()
