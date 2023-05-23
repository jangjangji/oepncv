import numpy as np
import cv2
from time import sleep

# 메인 함수
def main():
    image = cv2.imread('imgs/little.jpg') # 파일 읽어들이기

    # BGR로 색추출
    bgrLower = np.array([165,166,162])    # 추출할 색의 하한
    bgrUpper = np.array([231,229,228])    # 추출할 색의 상한
    bgrResult = bgrExtraction(image, bgrLower, bgrUpper)
    cv2.imshow('BGR_test1', bgrResult)

    while True:
        # 키 입력을 1ms기다리고, key가「q」이면 break
        key = cv2.waitKey(1)&0xff
        if key == ord('q'):
            break

        cv2.destroyAllWindows()
    



def bgrExtraction(image, bgrLower, bgrUpper):
    img_mask = cv2.inRange(image, bgrLower, bgrUpper) 
    result = cv2.bitwise_and(image, image, mask=img_mask) 
    return result

if __name__ == '__main__':
    main()