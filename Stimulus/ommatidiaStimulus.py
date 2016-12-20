import numpy as np
import cv2
import sys, math
import matplotlib.pyplot as plt


# Set stimulus parameters
velStim = -0.5  #m/s velocity of stimulus
lStim = 0.1 #m  half length of stimulus
xStart = 0.12 #m start approach distance away from specimen 

# Set locust parameters
xFov = 180 # degrees, fov locust azimuth
yFov = 180 # degrees, fov locust elevation
angPix = 2.33 # deg/pixel interommatidial angle specimen

#Set parameters image

backgroundColor = 255 # 0 black, 255 white 
scaleRes = 1  # resolution scale, to downsample later
fps = 200 # Frame Resolution

#Configure Image 

def createImage(xFov, yFov , angPix, scaleRes):
	outHeight =int(round(yFov / angPix))
	outWidth =int(round(xFov / angPix)) 	
	hImage = int(round(outHeight * scaleRes)) 
	wImage = int(round(outWidth * scaleRes))

	img = np.ones((hImage,wImage,3), np.uint8)*backgroundColor
	return img, outHeight, outWidth, hImage, wImage


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
	lPix1 = np.divide(thetaRun, angPix) # this is the whole length
	lPix = np.multiply(lPix1, scaleRes* 180/math.pi)

	return t, lPix , thetaRun, xRun

img, outHeight, outWidth, hImage, wImage = createImage(xFov, yFov, angPix, scaleRes)
tStimulus, lStimulus, theta, xRun  = getParamters(velStim, tStart, tEnd, dt, lStim, angPix)

# plt.plot(tStimulus, lStimulus)
# plt.show()
# print tStimulus

# def writerImage(fps, outWidth. outHeight, wImage, hImage, dt, lStimulus, img)
fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
writerOut = cv2.VideoWriter('stimOmmatidia3.avi', fourcc, fps , (outWidth, outHeight))

# Put in some frames at the beginning:

numFrames = 1000
firstFrame = 0
lastFrame = len(lStimulus)-1

for i in range(1,numFrames):
	length = lStimulus[firstFrame] 
	xTopLeft1 = int(round(wImage/2 - (length/2)))
	yTopLeft1 = int(round(hImage/2 - (length /2)))
	xBottomRight1 = int(round(wImage/2 + (length/2)))
	yBottomRight1 = int(round(hImage/2 + length/ 2))
	figureSquare1 = cv2.rectangle(img,(xTopLeft1,yTopLeft1),(xBottomRight1,yBottomRight1),(0,0,0), thickness = cv2.FILLED )
	#cv2.imshow('figureSquare1', img)
	imgResize = cv2.resize(img, (outWidth, outHeight) , interpolation = cv2.INTER_AREA )
	cv2.waitKey(int(math.ceil(dt)))
	#number = number +1
	writerOut.write(imgResize)

number = 1
for i in np.nditer(lStimulus) :
	xTopLeft1 = int(round(wImage/2 - (i/2)))
	yTopLeft1 = int(round(hImage/2 - (i /2)))
	xBottomRight1 = int(round(wImage/2 + (i/2)))
	yBottomRight1 = int(round(hImage/2 + i/ 2))
	figureSquare1 = cv2.rectangle(img,(xTopLeft1,yTopLeft1),(xBottomRight1,yBottomRight1),(0,0,0), thickness = cv2.FILLED )
	#cv2.imshow('figureSquare1', img)
	imgResize = cv2.resize(img, (outWidth, outHeight) , interpolation = cv2.INTER_AREA )
	cv2.waitKey(int(math.ceil(dt)))
	number = number +1
	writerOut.write(imgResize)


print len(lStimulus)
print lastFrame

for i in range(1,numFrames):
	length = lStimulus[lastFrame] 
	xTopLeft1 = int(round(wImage/2 - (length/2)))
	yTopLeft1 = int(round(hImage/2 - (length /2)))
	xBottomRight1 = int(round(wImage/2 + (length/2)))
	yBottomRight1 = int(round(hImage/2 + length/ 2))
	figureSquare1 = cv2.rectangle(img,(xTopLeft1,yTopLeft1),(xBottomRight1,yBottomRight1),(0,0,0), thickness = cv2.FILLED )
	#cv2.imshow('figureSquare1', img)
	imgResize = cv2.resize(img, (outWidth, outHeight) , interpolation = cv2.INTER_AREA )
	cv2.waitKey(int(math.ceil(dt)))
	#number = number +1
	writerOut.write(imgResize)




writerOut.release()

cv2.destroyAllWindows()



