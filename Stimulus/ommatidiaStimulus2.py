import numpy as np
import cv2
import sys, math
import matplotlib.pyplot as plt


# Set stimulus parameters
velStim = -0.18  #m/s velocity of stimulus
lStim = 0.01 #m  half length of stimulus
xStart = 0.05 #m start approach distance away from specimen 

# Set locust parameters
xFov = 180 # degrees, fov locust azimuth
yFov = 180 # degrees, fov locust elevation
angPix = 4.5 # deg/pixel interommatidial angle specimen

#Set parameters image
#scaleCon = (100,100,100)
#scaleCon = (100,100,100)
scaleCon = (0,0,0)
backgroundColor = 255  # 0 black, 255 white 
scaleRes = 10  # resolution scale, to downsample later
fps = 200 # Frame Resolution
numFrames = 10 # Number of repetition frames at end and beginning 
#Starting position, 2 is center, 3 left up,, 4 right, down
xposFrac = 2
yposFrac = 2 
#Configure Image 

def createImage(xFov, yFov , angPix, scaleRes):
	outHeight =int(round(yFov / angPix))
	outWidth =int(round(xFov / angPix)) 	
	hImage = int(round(outHeight * scaleRes)) 
	wImage = int(round(outWidth * scaleRes))

	img = np.ones((hImage,wImage,3), np.uint8)*backgroundColor
	return img, outHeight, outWidth, hImage, wImage


#Initiate Parameters






def getParamters(velStim, xStart, fps, lStim, angPix ):
	dt = 1./fps 
	tEnd = 0
	tStart= xStart/velStim
	t = np.arange(tStart, tEnd, dt)
	xRun = np.multiply(velStim,t)
	thetaArray= np.divide(lStim , xRun)
	thetaRun = np.multiply(2 , np.arctan(thetaArray)) # this is the whole angle
	# lSquareRun1 = np.multiply(xStart , np.tan(np.divide(thetaRun1 , 2)))
	lPix1 = np.divide(thetaRun, angPix) # this is the whole length
	lPix = np.multiply(lPix1, scaleRes* 180/math.pi)

	return t, lPix , thetaRun, xRun, dt

img, outHeight, outWidth, hImage, wImage = createImage(xFov, yFov, angPix, scaleRes)
tStimulus, lStimulus, theta, xRun, dt  = getParamters(velStim, xStart, fps, lStim, angPix )

# plt.plot(tStimulus, lStimulus)
# plt.show()
# print tStimulus

# def writerImage(fps, outWidth. outHeight, wImage, hImage, dt, lStimulus, img)

fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
writerOut = cv2.VideoWriter('SquarePos_fps_'+str(fps) +'_v_' +str(velStim)+'_l_'+str(lStim)+ '_x_'+ str(xStart)+ '_Sc_'+str(scaleCon)+'.avi', fourcc, fps , (outWidth, outHeight))

# Put in some frames at the beginning:


# Repetition first frame
firstFrame = 0
# for i in range(1,numFrames):
# 	length = lStimulus[firstFrame] 
# 	xTopLeft1 = int(round(wImage/2 - (length/2)))
# 	yTopLeft1 = int(round(hImage/2 - (length /2)))
# 	xBottomRight1 = int(round(wImage/2 + (length/2)))
# 	yBottomRight1 = int(round(hImage/2 + length/ 2))
# 	figureSquare1 = cv2.rectangle(img,(xTopLeft1,yTopLeft1),(xBottomRight1,yBottomRight1),scaleCon, thickness = cv2.FILLED )
# 	#cv2.imshow('figureSquare1', img)
# 	imgResize = cv2.resize(img, (outWidth, outHeight) , interpolation = cv2.INTER_AREA )
# 	cv2.waitKey(int(math.ceil(dt)))
# 	writerOut.write(imgResize)



# Looming stimulus
for i in np.nditer(lStimulus) :
	xTopLeft1 = int(round(wImage/xposFrac - (i/2)))
	yTopLeft1 = int(round(hImage/yposFrac - (i /2)))
	xBottomRight1 = int(round(wImage/xposFrac + (i/2)))
	yBottomRight1 = int(round(hImage/yposFrac + i/ 2))
	figureSquare1 = cv2.rectangle(img,(xTopLeft1,yTopLeft1),(xBottomRight1,yBottomRight1),scaleCon, thickness = cv2.FILLED )
	#cv2.imshow('figureSquare1', img)
	imgResize = cv2.resize(img, (outWidth, outHeight) , interpolation = cv2.INTER_AREA )
	#imgResize = cv2.resize(img, (20, 20) , interpolation = cv2.INTER_AREA )
	
	cv2.waitKey(int(math.ceil(dt)))
	writerOut.write(imgResize)

# Repetition last frame
# lastFrame = len(lStimulus)-1

# for i in range(1,numFrames):
# 	length = lStimulus[lastFrame] 
# 	xTopLeft1 = int(round(wImage/2 - (length/2)))
# 	yTopLeft1 = int(round(hImage/2 - (length /2)))
# 	xBottomRight1 = int(round(wImage/2 + (length/2)))
# 	yBottomRight1 = int(round(hImage/2 + length/ 2))
# 	figureSquare1 = cv2.rectangle(img,(xTopLeft1,yTopLeft1),(xBottomRight1,yBottomRight1),scaleCon, thickness = cv2.FILLED )
# 	#cv2.imshow('figureSquare1', img)
# 	imgResize = cv2.resize(img, (20, 20) , interpolation = cv2.INTER_AREA )
	
# 	#imgResize = cv2.resize(img, (outWidth, outHeight) , interpolation = cv2.INTER_AREA )
# 	cv2.waitKey(int(math.ceil(dt)))
# 	writerOut.write(imgResize)


writerOut.release()

cv2.destroyAllWindows()


from tempfile import TemporaryFile
outfile = TemporaryFile()
data = []
data = np.column_stack((tStimulus, theta))
np.save(outfile,data)


