import cv2
import os
import numpy as np

# loop over all images in the resources directory
for filename in os.listdir("resources"):
    if filename.endswith(".jpg"):
        img_path = os.path.join("resources", filename)

        # membaca gambar
        img = cv2.imread(img_path)

        # thresholding
        thresh_value = 100
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, thresh_value, 255, cv2.THRESH_BINARY)

        # grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # image brightening
        bright = cv2.addWeighted(img, 1.5, np.zeros(img.shape, img.dtype), 0, 0)

        # operasi aritmatik
        img1 = cv2.imread('resources/gambar1.jpg')
        img2 = cv2.imread('resources/gambar2.jpg')
        add = cv2.add(img1, img2)
        subtract = cv2.subtract(img1, img2)
        multiply = cv2.multiply(img1, img2)
        divide = cv2.divide(img1, img2)

        # operasi boolean
        img1 = cv2.imread('resources/gambar1.jpg')
        img2 = cv2.imread('resources/gambar2.jpg')
        and_op = cv2.bitwise_and(img1, img2)
        or_op = cv2.bitwise_or(img1, img2)
        xor_op = cv2.bitwise_xor(img1, img2)
        not_op = cv2.bitwise_not(img1)

        # operasi geometri
        rows, cols = img.shape[:2]
        M = cv2.getRotationMatrix2D((cols/2,rows/2), 45, 1)
        rotate = cv2.warpAffine(img, M, (cols, rows))
        flip_hor = cv2.flip(img, 1)
        flip_ver = cv2.flip(img, 0)

        # menampilkan hasil
        cv2.imshow('Original', img)
        cv2.imshow('Thresholding', thresh)
        cv2.imshow('Grayscale', gray)
        cv2.imshow('Brightening', bright)
        cv2.imshow('Addition', add)
        cv2.imshow('Subtraction', subtract)
        cv2.imshow('Multiplication', multiply)
        cv2.imshow('Division', divide)
        cv2.imshow('AND', and_op)
        cv2.imshow('OR', or_op)
        cv2.imshow('XOR', xor_op)
        cv2.imshow('NOT', not_op)
        cv2.imshow('Rotation', rotate)
        cv2.imshow('Horizontal Flip', flip_hor)
        cv2.imshow('Vertical Flip', flip_ver)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
