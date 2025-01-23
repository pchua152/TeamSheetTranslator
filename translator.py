#The main file

import cv2 as cv
import numpy as np
import pytesseract
import abilities
import mons
import moves

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
def translate_team():
    #r'C:\Users\Paul\Desktop\otherprojects\opencv_projects\photos\test1.jpg'
    img = cv.imread(r'C:\Users\Paul\Desktop\otherprojects\opencv_projects\photos\pokecon_eng.jpg')
    
    #Should be 1280 width 720 height
    shape_check = img.shape
    
    if shape_check != (720,1280,3):
        img = cv.resize(img, (1280,720))
    
    
    
    
    #Next steps - draw rectangles around the 6 spots with the mons(should be fixed points)
    #y,x
    mon_1 = img[100:265, 45:245]
    move_1 = img[100:265, 400:630]
    # mon_2 = img[100:265, 650:1240]
    mon_2 = img[100:265, 650: 850]
    move_2 = img[100:265, 1005:1235]
    # mon_3 = img[280:445, 56:245]
    mon_3 = img[280:445, 45:245]
    move_3 = img[280:445, 400:630]
    # mon_4 = img[280:445, 650:1240]
    mon_4 = img[280:445, 650:850]
    move_4 = img[280:445,1005:1235]
    # mon_5 = img[455:620, 40:630]
    mon_5 = img[455:620, 45:245]
    move_5 = img[455:620, 400:630]
    # mon_6 = img[455:620, 650:1240]
    mon_6 = img[455:620, 650:850]
    move_6 = img[455:620, 1005:1235]
        
    # Grab the text from the rectangles
    # cv.imshow("Mon 1", mon_1)
    # cv.imshow("Move 1", move_1)
    # cv.imshow("Mon 2", mon_2)
    # cv.imshow("Move 2", move_2)
    # cv.imshow("Mon 3", mon_3)
    # cv.imshow("Move 3", move_3)
    # cv.imshow("Mon 4", mon_4)
    # cv.imshow("Move 4", move_4)
    # cv.imshow("Mon 5", mon_5)
    # cv.imshow("Move 5", move_5)
    # cv.imshow("Mon 6", mon_6)
    # cv.imshow("Move 6", move_6)
    # cv.imshow("Mon 3", mon_3)
    # cv.imshow("Mon 4", mon_4)
    # cv.imshow("Mon 5", mon_5)
    # cv.imshow("Mon 6", mon_6)

    # print(pytesseract.image_to_string(mon_5))
    # print(pytesseract.image_to_string(move_5))
    # print(pytesseract.image_to_string(mon_6))
    text = pytesseract.image_to_string(move_5)
    text = text.split("\n")
    print(text)
    
    text = [moves[x] for x in text if x in moves.moves]
            
    
    # cv.waitKey(0)
    # cv.destroyAllWindows()
    
    

translate_team()