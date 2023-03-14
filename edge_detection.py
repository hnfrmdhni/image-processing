import cv2
import os
import numpy as np

# mendapatkan path direktori saat ini
current_dir = os.path.dirname(os.path.abspath(__file__))

# path direktori resources
resources_dir = os.path.join(current_dir, 'resources')

# daftar nama file gambar yang akan diproses
file_names = ['gambar1.jpg', 'gambar2.jpg', 'gambar3.jpg', 'gambar4.jpg', 'gambar5.jpg',
              'gambar6.jpg', 'gambar7.jpg', 'gambar8.jpg', 'gambar9.jpg', 'gambar10.jpg']

# edge detection dengan Sobel, Canny, dan Gaussian untuk setiap gambar
for name in file_names:
    # membaca gambar
    file_path = os.path.join(resources_dir, name)
    img = cv2.imread(file_path)

    # edge detection dengan Sobel
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
    sobel = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

    # edge detection dengan Canny
    canny = cv2.Canny(gray, 100, 200)

    # edge detection dengan Gaussian
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    gaussian = cv2.Laplacian(blur, cv2.CV_64F)

    # menampilkan hasil
    cv2.imshow('Original', img)
    cv2.imshow('Sobel', sobel)
    cv2.imshow('Canny', canny)
    cv2.imshow('Gaussian', gaussian)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
