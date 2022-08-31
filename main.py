import utility_fun
import cv2
import os

if __name__ == '__main__':
    image_path = 'images/Original-Form-1.jpg'
    scanned_dir_path = 'scanned'
    image = cv2.imread(image_path)
    scanned_image = utility_fun.scan(image)
    cv2.imshow('scanned', scanned_image)
    cv2.waitKey()
    cv2.destroyWindow('scanned')
    cv2.imwrite(os.path.join(scanned_dir_path, 'scanned.jpg'), scanned_image)
