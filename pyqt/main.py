import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QImage
import cv2 as cv
import qimage2ndarray
import numpy as np
file_name_ui = 'untitled.ui'
form_class = uic.loadUiType(file_name_ui)[0]


class MyApp(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_file_path.clicked.connect(self.load_image)

    def load_image(self):
        self.qPixmapVar = QPixmap()
        file_path = self.text_file_path.text()
        self.qPixmapVar.load(file_path)
        self.qPixmapVar = self.qPixmapVar.scaledToWidth(self.label_image_real.width())
        self.label_image_real.setPixmap(self.qPixmapVar)
        print(self.qPixmapVar)

        img = cv.imread(file_path)
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        img_R = img.copy()
        img_G = img.copy()
        img_B = img.copy()
        img_R = img_R[:, :, 0]
        img_G = img_G[:, :, 1]
        img_B = img_B[:, :, 2]

        img_bgr = img.astype(np.float64) / 255.0
        img_K = 1 - np.max(img_bgr, axis=2)
        img_C = (1 - img_bgr[..., 2] - img_K) / (1 - img_K)
        img_M = (1 - img_bgr[..., 1] - img_K) / (1 - img_K)
        img_Y = (1 - img_bgr[..., 0] - img_K) / (1 - img_K)

        # img_K = (np.dstack(img_K) * 255).astype(np.uint8)
        img_K = img_K * 255
        img_C = img_C * 255
        img_M = img_M * 255
        img_Y = img_Y * 255


        qimage_RGB = qimage2ndarray.array2qimage(img, normalize=False)

        qimage_B = qimage2ndarray.array2qimage(img_B, normalize=False)
        qimage_G = qimage2ndarray.array2qimage(img_G, normalize=False)
        qimage_R = qimage2ndarray.array2qimage(img_R, normalize=False)

        qimage_K = qimage2ndarray.array2qimage(img_K, normalize=False)
        qimage_C = qimage2ndarray.array2qimage(img_C, normalize=False)
        qimage_M = qimage2ndarray.array2qimage(img_M, normalize=False)
        qimage_Y = qimage2ndarray.array2qimage(img_Y, normalize=False)


        # h, w, c = img.shape
        # qImg = QImage(img.data, w, h, w * c, QImage.Format_RGB888)
        # qImg = QImage(img.data, w, h, w * c, QImage.Format_RGB888)
        # pixmap = QPixmap.fromImage(qImg).scaledToWidth(600)
        pixmap_R = QPixmap.fromImage(qimage_R).scaledToWidth(self.label_image_R.width())
        pixmap_G = QPixmap.fromImage(qimage_G).scaledToWidth(self.label_image_G.width())
        pixmap_B = QPixmap.fromImage(qimage_B).scaledToWidth(self.label_image_B.width())

        pixmap_K = QPixmap.fromImage(qimage_K).scaledToWidth(self.label_image_K.width())
        pixmap_C = QPixmap.fromImage(qimage_C).scaledToWidth(self.label_image_C.width())
        pixmap_M = QPixmap.fromImage(qimage_M).scaledToWidth(self.label_image_M.width())
        pixmap_Y = QPixmap.fromImage(qimage_Y).scaledToWidth(self.label_image_Y.width())

        self.label_image_R.setPixmap(pixmap_R)
        self.label_image_G.setPixmap(pixmap_G)
        self.label_image_B.setPixmap(pixmap_B)

        self.label_image_C.setPixmap(pixmap_C)
        self.label_image_M.setPixmap(pixmap_M)
        self.label_image_Y.setPixmap(pixmap_Y)
        self.label_image_K.setPixmap(pixmap_K)
        # self.label_image_real.resize(label_image_K.width, pixmap.height())
        # self.label_image_real.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    firstWindow = MyApp()
    firstWindow.show()

    app.exec_()
