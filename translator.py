import cv2 as cv
import numpy as np
import pytesseract
import abilities as abilities
import mons
import moves
import os
from thefuzz import fuzz
from dotenv import load_dotenv

load_dotenv()
path_to_tesseract = os.getenv('TessURL')

image = os.getenv('image2')


pytesseract.pytesseract.tesseract_cmd = path_to_tesseract
def translate_team():
    
    img = cv.imread(image)
    img = img.copy()
    
    #Should be 1280 width 720 height
    shape_check = img.shape
    
    if shape_check != (720,1280,3):
        print("Image is invalid size, must be 1280 x 720")
        return 0
        
    #Preprocess image to read the text better
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret, thresh1 = cv.threshold(gray,0,255, cv.THRESH_OTSU | cv.THRESH_BINARY_INV)
    
    img1 = thresh1
    
    mon_names = []
    mon_abilities = []
    mon_moves = []
    
    #y,x
    #Everything has a fixed point
    mon_name_1 = img1[110:150, 45:245]
    mon_ability_1 = img1[180:220, 45:245]

    mon_name_2 = img1[110:150, 650:850]
    mon_ability_2 = img1[180:220, 650:850]
   

    mon_name_3 = img1[280:330, 40:230]
    mon_ability_3 = img1[360:400, 40:230]
 
 
    mon_name_4 = img1[280:330, 650:850]
    mon_ability_4 = img1[360:400, 650:850]
  
    mon_name_5 = img1[460:510, 40:230]
    mon_ability_5 = img1[545:585, 40:230]

    mon_name_6 = img1[470:510, 650:850]
    mon_ability_6 = img1[545:585, 650:850]

    
    name = pytesseract.image_to_string(mon_name_1, lang= "jpn").strip()
    text  = closest_pokemon_name(name)

    mon_names.append(text)
    
    ability = pytesseract.image_to_string(mon_ability_1, lang="jpn").strip()
    mon_abilities.append(closest_ability(ability))
    
    name = pytesseract.image_to_string(mon_name_2, lang= "jpn").strip()
    mon_names.append(closest_pokemon_name(name))
    
    ability = pytesseract.image_to_string(mon_ability_2, lang="jpn").strip()
    mon_abilities.append(closest_ability(ability))
    
    name = pytesseract.image_to_string(mon_name_3, lang= "jpn").strip()
    mon_names.append(closest_pokemon_name(name))
    
    ability = pytesseract.image_to_string(mon_ability_3, lang="jpn").strip()
    mon_abilities.append(closest_ability(ability))
    
    name = pytesseract.image_to_string(mon_name_4, lang= "jpn").strip()
    mon_names.append(closest_pokemon_name(name))
    
    ability = pytesseract.image_to_string(mon_ability_4, lang="jpn").strip()
    mon_abilities.append(closest_ability(ability))
    

    name = pytesseract.image_to_string(mon_name_5, lang= "jpn").strip()
    mon_names.append(closest_pokemon_name(name))
    
    
    name = pytesseract.image_to_string(mon_name_6, lang= "jpn").strip()
    mon_names.append(closest_pokemon_name(name))
 
    
    ability = pytesseract.image_to_string(mon_ability_5, lang="jpn").strip()
    mon_abilities.append(closest_ability(ability))
    
    
    ability = pytesseract.image_to_string(mon_ability_6, lang="jpn").strip()
    mon_abilities.append(closest_ability(ability))

    blue_color = (116,85,36)
    font = cv.FONT_HERSHEY_SIMPLEX
    
    name_locations = [(53,110, 240, 150), (660, 110, 808, 150), (53, 290, 240, 330), (660,290, 808,330), (53,470, 240, 510), (660, 470, 808, 510)]
    ability_locations = [(53,180, 240,220) , (660,180, 835, 220), (53,360,240,400), (660, 360, 835, 400), (53, 540, 240, 580), (660, 540, 835, 580)]
    #A rental might not have 6 in the picture
    total_mons = len(mon_names)
    
    
    move_y_regions = [[(100,141), (141,182), (182,223), (223,265)],  [(290,325) , (325, 362), (362,403), (403,445)], [(465,506), (506,547), (547,578), (578, 620)]]
    move_x_regions = [(390,620), (1000,1235)]
    for x1, x2 in move_x_regions:
        for y in move_y_regions:
            for y1,y2 in y:
                move = img1[y1:y2,x1:x2]
                midpoint = (y1 + y2) // 2
                image_read = pytesseract.image_to_string(move, lang="jpn")
                cv.rectangle(img, (x1,y1), (x2,y2), blue_color, -1)
                add_this = closest_move(image_read)
                cv.putText(img, add_this, (x1, midpoint), font, .5 ,(255,255,255), 1)
    
    for i in range(total_mons):
        x1,y1,x2,y2 = name_locations[i]
        ax1,ay1,ax2,ay2 = ability_locations[i]
        ability_midpoint = (ay1 + ay2) // 2
        midpoint = (y1+y2)//2
        cv.rectangle(img,(x1,y1), (x2,y2) , blue_color, -1)
        cv.rectangle(img, (ax1, ay1), (ax2,ay2), blue_color, -1)
        cv.putText(img, mon_names[i], (x1, midpoint), font,  1, (255,255,255), 1)
        cv.putText(img,mon_abilities[i], (x1,ability_midpoint), font, .85, (255,255,255), 1)
    
    
    cv.imwrite('Translated_Image.jpg', img)
    
    

#Failsafes included for when error happens in image reading
def closest_move(text):
    #it can be possible a pokemon does not have 4 moves
    if text == "":
        return
    if text in moves.moves:
        return moves.moves[text]
    else:
        max = 0
        value = ""
        ascii_text = ascii(text)
        for key in moves.moves:
            #Fuzz ratio the ascii to compare the Japanese text
            fuzz_ratio = fuzz.ratio(ascii_text, ascii(key))
            if fuzz_ratio > max:
                max = fuzz_ratio
                value = moves.moves[key]
        return value

def closest_ability(text):
    if text == " ":
        return
    if text in abilities.abilities:
        return abilities.abilities[text]
    else:
        max = 0
        value = ""
        ascii_text = ascii(text)
        for key in abilities.abilities:
            #Fuzz ratio the ascii to compare the Japanese text
            fuzz_ratio = fuzz.ratio(ascii_text, ascii(key))
            if fuzz_ratio > max:
                max = fuzz_ratio
                value = abilities.abilities[key]
        return value

def closest_pokemon_name(text):
    if text == "":
        return 
    if text in mons.mons:
        return mons.mons[text]
    
    else:
        max = 0
        value = ""
        for key in mons.mons:
            fuzz_ratio = fuzz.ratio(ascii(text), ascii(key))
            if fuzz_ratio > max:
                max = fuzz_ratio
                value = mons.mons[key]
        return value


if __name__ == "__main__":
    translate_team()