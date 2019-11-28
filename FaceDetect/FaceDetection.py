# FACE DETECTION
#Author: Pawan Verma (2108211004)
import cv2
import cvlib as cv
import matplotlib.pyplot as plt
from cvlib.object_detection import draw_bbox
from PIL import Image

group_img = Image.open('image3.jpg')
img = cv2.imread('image3.jpg')
#plt.imshow(img)
#plt.show()
#Detect the faces in the image
faces, confid = cv.detect_face(img)

if(len(faces) > 0):
    print("Faces Found!!")

i = int(1)
for item in faces:
    (Xcomp_s,Ycomp_s) = item[0],item[1]
    (Xcomp_e,Ycomp_e) = item[2],item[3]

    cv2.rectangle(img, (Xcomp_s,Ycomp_s),
    (Xcomp_e, Ycomp_e), (255,0,0,255), 2)

    #Crop detected images and save as jpg files
    cropIm = group_img.crop((Xcomp_s, Ycomp_s, Xcomp_e, Ycomp_e))
    cropIm.save('image_'+str(i)+'.jpg')
     
    i = int(i+1)

plt.imshow(img)
plt.show()
'''from pdf2image import convert_from_path
#Using the pdf form, convert it to jpg. This form can now
# be used to autofill the image from the detected faces
# For now we can choose any one image and use it to fill out our form
form = convert_from_path('SAMPLE_FORM.pdf')
for page in form:
    page.save('form.jpg', 'JPEG')

#Read the form
form_img_cv = cv2.imread('form.jpg')
form_img = Image.open('form.jpg')
image_1 = Image.open('image_1.jpg')

width, height = image_1.size
image_1 = image_1.resize((width + 70, height + 70))

form_img.paste(image_1, (3000, 1500))
form_img.save('complete_form.png')'''



