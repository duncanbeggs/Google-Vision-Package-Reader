import io
import os

s = os.listdir('pics__andSSD')

print (s)

i = 0
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
    print(f)
