import cv2 as cv
import pytesseract
import abilities
import items
import mons
import moves
import os
from thefuzz import fuzz
from dotenv import load_dotenv

load_dotenv()
path_to_tesseract = os.getenv('TessURL')

image = os.getenv('image3')


pytesseract.pytesseract.tesseract_cmd = path_to_tesseract
def translate_team():
    blue_color = (116,85,36)
    font = cv.FONT_HERSHEY_SIMPLEX
    name_locations = [(45,110, 245, 150), (650, 110, 850, 150), (40, 280, 230, 330), (650,280, 850,330), (40,460, 230, 510), (650, 470, 850, 510)]
    ability_locations = [(53,180, 240,220) , (660,180, 835, 220), (53,360,240,400), (660, 360, 835, 400), (53, 540, 240, 580), (660, 540, 835, 580)]
    item_y_regions = [(220,260), (400,440), (580,620)]
    item_x_regions = [(90,260), (695,865)]
    move_y_regions = [[(100,141), (141,182), (182,223), (223,265)],  [(290,325) , (325, 362), (362,403), (403,445)], [(465,506), (506,547), (547,578), (578, 620)]]
    move_x_regions = [(390,620), (1000,1235)]
    
    
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

    
    
    
    for x1,y1, x2,y2 in name_locations:
        midpoint = (y1+y2) // 2
        name = img1[y1:y2, x1:x2]
        image_read = pytesseract.image_to_string(name, lang= "jpn")
        cv.rectangle(img, (x1,y1) , (x2,y2), blue_color, -1)
        translated_text = closest_pokemon_name(image_read)
        cv.putText(img, translated_text, (x1, midpoint), font, 1, (255,255,255), 1)

    
    for x1,y1,x2,y2 in ability_locations:
        midpoint = (y1+ y2) // 2
        ability = img1[y1:y2, x1:x2]
        image_read = pytesseract.image_to_string(ability, lang= "jpn")
        cv.rectangle(img, (x1,y1), (x2,y2), blue_color, -1)
        translated_text = closest_ability(image_read)
        cv.putText(img, translated_text, (x1,midpoint), font, .85, (255,255,255), 1)
    
    for x1,x2 in item_x_regions:
        for y1,y2 in item_y_regions:
            item = img1[y1:y2, x1:x2]
            midpoint = (y1+ y2) // 2
            image_read = pytesseract.image_to_string(item,lang= "jpn")
            cv.rectangle(img, (x1,y1), (x2,y2), blue_color, -1)
            translated_text = closest_item(image_read)
            cv.putText(img, translated_text, (x1, midpoint), font, .75, (255,255,255), 1)
    
    for x1, x2 in move_x_regions:
        for y in move_y_regions:
            for y1,y2 in y:
                move = img1[y1:y2,x1:x2]
                midpoint = (y1 + y2) // 2
                image_read = pytesseract.image_to_string(move, lang="jpn")
                cv.rectangle(img, (x1,y1), (x2,y2), blue_color, -1)
                translated_text = closest_move(image_read)
                cv.putText(img, translated_text, (x1, midpoint), font, .5 ,(255,255,255), 1)
    
    cv.imwrite('Translated_Image.jpg', img)
    print('Translated image, check file named Translated_Image.jpg')
    
    

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

def closest_item(text):
    if text == "" or text == "なし":
        return "None"
    if text in items.items:
        return items.items[text]
    else:
        max = 0
        value = ""
        for key in items.items:
            fuzz_ratio = fuzz.ratio(ascii(text), ascii(key))
            if fuzz_ratio > max:
                max = fuzz_ratio
                value = items.items[key]
        return value
    


if __name__ == "__main__":
    translate_team()