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

    response = client.document_text_detection(image=image)
    texts = response.text_annotations
    #print(type(texts))
    #print(texts)

    complete = 0
    completeStr = ''
    partial = 0
    partialStr = ''
    for imgLine in texts:
        s = imgLine.description
        #print(imgLine.description)
        if s.find("1407C028[AA]") != -1:
            complete += 1
            completeStr = imgLine.description
            completeStr.encode('ascii',errors='ignore')
            #print("FOUND COMPLETE: " + imgLine.description)
        elif s.find("1407C028") != -1:
            partial += 1
            partialStr = imgLine.description
            partialStr.encode('ascii',errors='ignore')
            #print("FOUND PARTIAL: " + imgLine.description + " on " + path)

    #print("On " + os.path.basename(path) + "-> ", end='')

    path = path.replace('pics__andSSD', '')
    print("On " + path + "-> ", end='')

    if complete > 0:
        # Since there was a complete match no need to print out the entire string as it may contain endline chars
        print("FOUND COMPLETE: " + "1407C028[AA]")
    elif partial > 0:
        print("FOUND PARTIAL: " + partialStr)
    else:
        print("FAILURE")


# Instantiates a Vision client.
vision_client = google.cloud.vision.ImageAnnotatorClient()

i = 0 #temp counter to prevent us from overloading google cloud with too many files
filePathList = []
for root, dirs, files in os.walk('pics__andSSD'):
    for file in files:
        if file.endswith(".jpg"):
             f = os.path.join(root, file)
             filePathList.append(f)
             if i > 400:
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
