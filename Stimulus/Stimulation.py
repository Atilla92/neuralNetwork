import numpy as np
import cv2
import sys, math
import matplotlib.pyplot as plt


#####Screen Dimensions TDel 20 "
# hScreen = 41 # cm
# wScreen =  30 # cm
# hResoScreen = 1600 # pixels
# wResScreen = 1200 #[pixels]
# hPixRatio = hResoScreen / hScreen
# wPixRatio = wResScreen / wScreen


#Screen Dimensions ThinkPad
hScreen = 17 # cm
wScreen =  31 # cm
hResoScreen = 1920 # pixels
wResScreen = 1080 #[pixels]
hPixRatio = hResoScreen / hScreen
wPixRatio = wResScreen / wScreen


# Set image dimensions
upScale = 10
outWidth = 736
outHeight = 500
lSquare=5000   # cm 
vApproach = 0.5 # Velocity approach m/s
startPos= 12 # Start position approach cm
backgroundColor = 255
fps = 200  # frame rate Hz


#cImage = (wImage/2, hImage/2)


#Set object parameters
# Must convert to picels of the screen 
# Distance should be 12 cm, obeject size 6-14 cm, v 2-10m/s
 # cm to pixel, still should adjust pixels for height and width, but are similar
lhSquare = hPixRatio * upScale * lSquare
lwSquare = wPixRatio * upScale * lSquare
wImage= outWidth*upScale 
hImage = outHeight * upScale

#print type(lSquare, vSquare, xStart)

#Set up stimulus graphics

img = np.ones((hImage,wImage,3), np.uint8)*backgroundColor



#Try to initialize some time parameters (here I should incorporate the physics behind looming stimulus papers)
dt = 1./fps 
xStart = startPos * wPixRatio # # Distance from locust
vSquare= -vApproach * 100 * wPixRatio # m/s to pixel/s approach velocity
tStart= xStart/vSquare
tEnd = 0
thetaInitial = 2* np.arctan(lhSquare/xStart)

#Initialize arrays
lSquareNew = []
tNew = [] 
xNew = []
thetaNew = []

print hPixRatio

def getParamters(vSquare, tStart , tEnd ):

	t1 = np.arange(tStart, tEnd, dt)
	xRun1 = np.multiply(vSquare,t1)
	thetaArray= np.divide(lhSquare , xRun1)
	thetaRun1 = np.multiply(2 , np.arctan(thetaArray))
	lSquareRun1 = np.multiply(xStart , np.tan(np.divide(thetaRun1 , 2)))
	return t1, lSquareRun1

tStimulus, lStimulus  = getParamters(vSquare, tStart, tEnd)

plt.plot(tStimulus, lStimulus)
plt.show()

fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
writerOut = cv2.VideoWriter('stimulus3.avi', fourcc, fps , (outWidth, outHeight))
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
	#cv2.imwrite("./Images/TestImage"+ str(number) +".jpg", img) 
	writerOut.write(imgResize)
writerOut.release()

cv2.destroyAllWindows()


