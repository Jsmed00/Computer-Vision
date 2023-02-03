# Jonathan Smedley
# December 10th 2022
# Computer Vision
# Programming Assignment 2

import cv2
from matplotlib import pyplot as plt

# This shows the Benford law for the first image
image = cv2.imread('image.jpeg', 0)
image1 = image.astype(float)
image1_dct = cv2.dct(image1)
image1float = image1_dct.astype(float)

digitList = []
for i in image1float:
    for x in i:
        digitList.append(str(x)[0])


while '-' in digitList:
    digitList.remove('-')
while '0' in digitList:
    digitList.remove('0')

digitList.sort()

# This shows the Benford law for the second image
image2 = cv2.imread('image (1).jpeg', 0)
image2 = image.astype(float)
image2_dct = cv2.dct(image2)
image2float = image2_dct.astype(float)

digitList2 = []
for i in image2float:
    for x in i:
        digitList2.append(str(x)[0])


while '-' in digitList2:
    digitList2.remove('-')
while '0' in digitList2:
    digitList2.remove('0')

digitList2.sort()

# This shows the Benford law for the third image
image3 = cv2.imread('image (2).jpeg', 0)
image3 = image.astype(float)
image3_dct = cv2.dct(image2)
image3float = image3_dct.astype(float)

digitList3 = []
for i in image3float:
    for x in i:
        digitList3.append(str(x)[0])


while '-' in digitList3:
    digitList3.remove('-')
while '0' in digitList3:
    digitList3.remove('0')

digitList3.sort()

# This shows the Benford law for the fourth image
image4 = cv2.imread('image (3).jpeg', 0)
image4 = image.astype(float)
image4_dct = cv2.dct(image2)
image4float = image4_dct.astype(float)

digitList4 = []
for i in image4float:
    for x in i:
        digitList4.append(str(x)[0])


while '-' in digitList4:
    digitList4.remove('-')
while '0' in digitList4:
    digitList4.remove('0')

digitList4.sort()

# This shows the Benford law for the fifth image
image5 = cv2.imread('image (4).jpeg', 0)
image5 = image.astype(float)
image5_dct = cv2.dct(image2)
image5float = image5_dct.astype(float)

digitList5 = []
for i in image5float:
    for x in i:
        digitList5.append(str(x)[0])


while '-' in digitList5:
    digitList5.remove('-')
while '0' in digitList5:
    digitList5.remove('0')

digitList5.sort()

# This shows the Benford law for the first tampered image.
image1Tampered = cv2.imread('imageTampered.jpeg', 0)
image1_edit = image1Tampered.astype(float)
image1Tampered_dct = cv2.dct(image1_edit)
image1TamperedFloat = image1Tampered_dct.astype(float)

digitListTampered = []
for i in image1TamperedFloat:
    for x in i:
        digitListTampered.append(str(x)[0])

while '-' in digitListTampered:
    digitListTampered.remove('-')
while '0' in digitListTampered:
    digitListTampered.remove('0')

digitListTampered.sort()


# This shows the Benford law for the second tampered image.
image2Tampered = cv2.imread('imageTampered2.jpeg', 0)
image2_edit = image1Tampered.astype(float)
image2Tampered_dct = cv2.dct(image2_edit)
image2TamperedFloat = image2Tampered_dct.astype(float)

digitListTampered2 = []
for i in image2TamperedFloat:
    for x in i:
        digitListTampered2.append(str(x)[0])

while '-' in digitListTampered2:
    digitListTampered2.remove('-')
while '0' in digitListTampered2:
    digitListTampered2.remove('0')

digitListTampered2.sort()

# This shows the Benford law for the third tampered image.
image3Tampered = cv2.imread('imageTampered3.jpeg', 0)
image3_edit = image3Tampered.astype(float)
image3Tampered_dct = cv2.dct(image3_edit)
image3TamperedFloat = image3Tampered_dct.astype(float)

digitListTampered3 = []
for i in image3TamperedFloat:
    for x in i:
        digitListTampered3.append(str(x)[0])

while '-' in digitListTampered3:
    digitListTampered3.remove('-')
while '0' in digitListTampered3:
    digitListTampered3.remove('0')

digitListTampered3.sort()

# This shows the Benford law for the fourth tampered image.
image4Tampered = cv2.imread('imageTampered4.jpeg', 0)
image4_edit = image1Tampered.astype(float)
image4Tampered_dct = cv2.dct(image4_edit)
image4TamperedFloat = image4Tampered_dct.astype(float)

digitListTampered4 = []
for i in image4TamperedFloat:
    for x in i:
        digitListTampered4.append(str(x)[0])

while '-' in digitListTampered4:
    digitListTampered4.remove('-')
while '0' in digitListTampered4:
    digitListTampered4.remove('0')

digitListTampered4.sort()

# This shows the Benford law for the fifth tampered image.
image5Tampered = cv2.imread('imageTampered.jpeg', 0)
image5_edit = image1Tampered.astype(float)
image5Tampered_dct = cv2.dct(image5_edit)
image5TamperedFloat = image5Tampered_dct.astype(float)

digitListTampered5 = []
for i in image5TamperedFloat:
    for x in i:
        digitListTampered5.append(str(x)[0])

while '-' in digitListTampered5:
    digitListTampered5.remove('-')
while '0' in digitListTampered5:
    digitListTampered5.remove('0')

digitListTampered5.sort()

# Shows the graph for the first image.
plt.hist(digitList, bins=len(set(digitList)))

plt.title('Image 1 benford law')
plt.xlabel('Digit')
plt.ylabel('Occurrences')
plt.show()

# Shows the Tampered graph for the first image.
plt.hist(digitListTampered, bins=len(set(digitListTampered)))

plt.title('Tampered Image 1 Benford Law')
plt.xlabel('Digit')
plt.ylabel('Occurrences')
plt.show()

# Shows the graph for the second image.
plt.hist(digitList2, bins=len(set(digitList2)))

plt.title('Image 2 Benford Law')
plt.xlabel('Digit')
plt.ylabel('Occurrences')
plt.show()

# Shows the Tampered graph for the second image.
plt.hist(digitListTampered2, bins=len(set(digitListTampered2)))

plt.title('Tampered Image 2 Benford Law')
plt.xlabel('Digit')
plt.ylabel('Occurrences')
plt.show()

# Shows the graph for the third image.
plt.hist(digitList3, bins=len(set(digitList3)))

plt.title('Image 3 Benford Law')
plt.xlabel('Digit')
plt.ylabel('Occurrences')
plt.show()

# Shows the Tampered graph for the third image.
plt.hist(digitListTampered3, bins=len(set(digitListTampered3)))

plt.title('Tampered Image 3 Benford Law')
plt.xlabel('Digit')
plt.ylabel('Occurrences')
plt.show()

# Shows the graph for the fourth image.
plt.hist(digitList4, bins=len(set(digitList4)))

plt.title('Image 4 Benford Law')
plt.xlabel('Digit')
plt.ylabel('Occurrences')
plt.show()

# Shows the Tampered graph for the fourth image.
plt.hist(digitListTampered4, bins=len(set(digitListTampered4)))

plt.title('Tampered Image 4 Benford Law')
plt.xlabel('Digit')
plt.ylabel('Occurrences')
plt.show()

# Shows the graph for the fifth image.
plt.hist(digitList5, bins=len(set(digitList5)))

plt.title('Image 5 Benford Law')
plt.xlabel('Digit')
plt.ylabel('Occurrences')
plt.show()

# Shows the Tampered graph for the fifth image.
plt.hist(digitListTampered5, bins=len(set(digitListTampered5)))

plt.title('Tampered Image 5 Benford Law')
plt.xlabel('Digit')
plt.ylabel('Occurrences')
plt.show()
