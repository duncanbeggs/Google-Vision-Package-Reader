import io
import os

#In order for the google.cloud.vision function calls to operate correctly
#user credentials must be set in json file pointed to by ENV VAR GOOGLE_APPLICATION_CREDENTIALS
import google.cloud.vision
from google.cloud import storage
from google.cloud import vision
from google.protobuf import json_format


def detect_text(path):
    """Detects text in the file."""
    client = google.cloud.vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    #print(type(texts))
    #print(texts)

    for imgLine in texts:
        s = imgLine.description
        #print(imgLine.description)
        if s.find("1407C028[AA]") != -1:
            print("FOUND COMPLETE: " + imgLine.description)
        elif s.find("1407C028") != -1:
            print("FOUND PARTIAL: " + imgLine.description)
        else:
            print("Failure on " + path)


# Instantiates a Vision client.
vision_client = google.cloud.vision.ImageAnnotatorClient()

i = 0 #temp counter to prevent us from overloading google cloud with too many files
filePathList = []
for root, dirs, files in os.walk('pics__andSSD'):
    for file in files:
        if file.endswith(".jpg"):
             f = os.path.join(root, file)
             filePathList.append(f)
             if i > 40:
                 break
             else:
                 i += 1

for f in filePathList:
    detect_text(f)
#with io.open(image_file_name, 'rb') as image_file:
#        content = image_file.read()
# Use Vision to label the image based on content.
#image = google.cloud.vision.types.Image(content=content)
#response = vision_client.text_detection(image=image)
#print('JSON:')
#for label in response.label_annotations:
#    print(label.description)
