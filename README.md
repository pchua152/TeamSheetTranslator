# Teamsheet Translator
This project takes in an image of a rental team from Pokemon Scarlet and Violet that is orignally in Japanese and then translates all relevant data into English. The output provided are accurate to what the English translations are compared to running the image through another translating app such as Google Translate.

## Getting Started
Before running, there are a few dependencies you will need to download.
Use the following commands to install the necessary libraries:

`pip install opencv-python pytesseract thefuzz`

With the following libraries installed, you will also need to download [Tesseract OCR](https://tesseract-ocr.github.io/tessdoc/Downloads.html). **Be sure to download the other language packs, specifically Japanese, for this to work properly**.

In the translator.py file, edit the following lines to the correct values:
  * `image = path_to_your_image_here`
  * `pytesseract.pytesseract.tesseract_cmd = path_to_tesseract`

Make sure the image you are using is **1280 x 720**. This can easily be done by taking a screenshot on your Switch and then transfering the photo to your smart phone. 

Once you are in the directory with all these files, to run the code use the command `python translator.py`. The translated image will be output to a jpg named Translated_Image.jpg.

## Examples
### Example 1
![Example_1_Before](https://github.com/user-attachments/assets/cac3cea0-6c44-4d87-8322-ca466730acf0)
![Translated_Image](https://github.com/user-attachments/assets/85ddc58c-7a8c-4989-98a7-22b9ae57ad1e)

### Example 2
![test2](https://github.com/user-attachments/assets/12325a22-7979-462a-8add-8dc642a1ab06)
![Translated_Image](https://github.com/user-attachments/assets/3f0ac222-5613-4762-9e4f-b036ca22eef3)


## Known Issues
The program translates images with ~95% accuracy. This means that there is a slight chance that one or two things on the translated image is incorrect, however the mistakes are pretty easy to spot such as a Pokemon name being off which can be verified with the picture and attacks being ones it cannot naturally learn.



