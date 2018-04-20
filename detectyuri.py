import numpy as np
import cv2
from pathlib import Path
import sys


def main():
    cascade = cv2.CascadeClassifier('models/model.xml')
    color = (0, 0, 255)
    p = Path('./data')
    imgs = [fname for fname in p.iterdir() if not fname.name == '.gitkeep']
    for img in imgs:
        image = cv2.imread(str(img), 1)
        if image is not None:
            facerect = cascade.detectMultiScale(image, minSize=(200, 200))
            if len(facerect) > 0:
                print(img)
                print(facerect)
                for rect in facerect:
                    print(tuple(rect[0:2]))
                    print(tuple(rect[0:2] + rect[2:4]))
                    print()
                    '''
                    cv2.rectangle(image,
                                  tuple(rect[0:2]),
                                  tuple(rect[0:2] + rect[2:4]),
                                  color)
                    '''
                out = 'data3/' + img.name
                cv2.imwrite('data3/' + img.name, image)
                '''
            y = rect[1]
            yy = y + rect[3]
            x = rect[0]
            xx = x + rect[2]
            cv2.imwrite('cropped/' + img.name, image[y:yy, x:xx])
            '''

    return 0


if __name__ == '__main__':
    main()
