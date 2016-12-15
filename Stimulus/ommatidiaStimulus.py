import numpy as np
import cv2
import sys, math
import matplotlib.pyplot as plt


# Set stimulus parameters
velStim = -2 #m/s velocity of stimulus
lStim = 0.1 #m  half length of stimulus
xStart = 0.12 #m start approach distance away from specimen 

# Set locust parameters
xFov = 180 # degrees, fov locust azimuth
yFov = 180 # degrees, fov locust elevation
angPix = 2.33 # deg/pixel interommatidial angle specimen

#Set parameters image

backgroundColor = 255 # 0 black, 255 white 
scaleRes = 1  # resolution scale, to downsample later
fps = 2000 # Frame Resolution

#Configure Image 

def createImage(xFov, yFov , angPix, scaleRes):
	hImage = yFov / angPix * scaleRes 
	wImage = xFov / angPix * scaleRes
	img = np.ones((hImage,wImage,3), np.uint8)*backgroundColor
	return img

image = createImage(xFov, yFov, angPix, scaleRes)
#Initiate Parameters

dt = 1./fps 
tStart= xStart/velStim
tEnd = 0


def getParamters(velStim, tStart , tEnd, dt, lStim, angPix ):

	t = np.arange(tStart, tEnd, dt)
	xRun = np.multiply(velStim,t)
	thetaArray= np.divide(lStim , xRun)
	thetaRun = np.multiply(2 , np.arctan(thetaArray)) # this is the whole angle
	# lSquareRun1 = np.multiply(xStart , np.tan(np.divide(thetaRun1 , 2)))
	lPix = np.divide(thetaRun, angPix) # this is the whole length

	return t, lPix , thetaRun, xRun

tStimulus, lStimulus, theta, xRun  = getParamters(velStim, tStart, tEnd, dt, lStim, angPix)

plt.plot(tStimulus, theta)
plt.show()
print tStimulus




