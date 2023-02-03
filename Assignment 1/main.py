# Jonathan Smedley
# CSCI 4150
# September 30th 2022

import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats

psum1 = 0
psum2 = 0
psum3 = 0
psum4 = 0
psum5 = 0
# Sets the variables imgX to different image files.
img1 = cv2.imread('northern-lights-7.jpg', 0)
img2 = cv2.imread('northern-lights-11.jpg', 0)
img3 = cv2.imread('northern-lights-16.jpg', 0)
img4 = cv2.imread('northern-lights-20.jpg', 0)
img5 = cv2.imread('northern-lights-21.jpg', 0)

# cv2.imshow('image', img)

# Creates a histogram for each img file.
histogram1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
histogram2 = cv2.calcHist([img2], [0], None, [256], [0, 256])
histogram3 = cv2.calcHist([img3], [0], None, [256], [0, 256])
histogram4 = cv2.calcHist([img4], [0], None, [256], [0, 256])
histogram5 = cv2.calcHist([img5], [0], None, [256], [0, 256])

plt.plot(histogram1)
plt.plot(histogram2)
plt.plot(histogram3)
plt.plot(histogram4)
plt.plot(histogram5)

for i in histogram1:
    p1 = float(i / (880 * 1095))
    psum1 = p1 + psum1

for i in histogram2:
    p2 = float(i / (880 * 587))
    psum2 = p2 + psum2

for i in histogram3:
    p3 = float(i / (880 * 1100))
    psum3 = p3 + psum3

for i in histogram4:
    p4 = float(i / (880 * 1304))
    psum4 = p4 + psum4

for i in histogram5:
    p5 = float(i / (880 * 587))
    psum5 = p5 + psum5


print("The sum of probabilities for the first image is: ", psum1)
print("The mean for the first image is: ", np.mean(histogram1))
print("The variance for the first image is: ", np.var(histogram1) / 256)
print("The Third Central Moment for the first image is: ", float(stats.skew(histogram1)))
print("The Fourth Central Moment for the first image is: ", float(stats.kurtosis(histogram1)), '\n')

print("The sum of probabilities for the second image is: ", psum2)
print("The mean for the second image is: ", np.mean(histogram2))
print("The variance for the second image is: ", np.var(histogram2) / 256)
print("The Third Central Moment for the second image is: ", float(stats.skew(histogram2)))
print("The Fourth Central Moment for the second image is: ", float(stats.kurtosis(histogram2)), '\n')

print("The sum of probabilities for the third image is: ", psum3)
print("The mean for the third image is: ", np.mean(histogram3))
print("The variance for the third image is: ", np.var(histogram3) / 256)
print("The Third Central Moment for the third image is: ", float(stats.skew(histogram3)))
print("The Fourth Central Moment for the third image is: ", float(stats.kurtosis(histogram3)), '\n')

print("The sum of probabilities for the fourth image is: ", psum4)
print("The mean for the fourth image is: ", np.mean(histogram4))
print("The variance for the fourth image is: ", np.var(histogram4) / 256)
print("The Third Central Moment for the fourth image is: ", float(stats.skew(histogram4)))
print("The Fourth Central Moment for the fourth image is: ", float(stats.kurtosis(histogram4)), '\n')

print("The sum of probabilities for the fifth image is: ", psum5)
print("The mean for the fifth image is: ", np.mean(histogram5))
print("The variance for the fifth image is: ", np.var(histogram5) / 256)
print("The Third Central Moment for the fifth image is: ", float(stats.skew(histogram5)))
print("The Fourth Central Moment for the fifth image is: ", float(stats.kurtosis(histogram5)))

plt.show()


