import numpy as np
import cv2
import sys, math
import matplotlib.pyplot as plt


##### VARIABLES ########
#Set insect parameters
xFov = 180 # degrees, fov locust azimuth
yFov = 180 # degrees, fov locust elevation
angPix = 2.33 # deg/pixel interommatidial angle specimen
# Set Image Parameters
greyValue = 0
scaleCon = (1,1,1) * greyValue
backgroundColor = 255  # 0 black, 255 white 
scaleRes = 10  # resolution scale, to downsample later
fps = 200 # Frame Resolution
numFrames = 10 # Number of repetition frames at end and beginning 
# Set velocity 
wVel = 0 #pix/second
hVel = 0 # pix/second
##################################
wVelOp = -10 # pix/second
hVelOp = -10 # pix/second

#createImage(xFov, yFov , angPix, scaleRes)
from ommatidiaStimulus import createImage
img, outHeight, outWidth, hImage, wImage = createImage(xFov, yFov, angPix, scaleRes)

# Estimate Parameters
dt = 1./ fps
tEnd = 0 

#h_t = np. arange(hTime, tEnd, dt)


if hVel == 0 and wVel<0 :
	
	wTime = wImage/wVel # second time of stimulus f(velocity)
	hTime = hImage/wVel #  ''
	h_t = np. arange(hTime, tEnd, dt)
	w_t = np.arange(wTime,tEnd , dt )
	wLength = np.multiply(w_t, wVel)
	hLength = 0 * np.ones(len(h_t))

elif wVel == 0 and hVel<0:
	wTime = wImage/hVel # second time of stimulus f(velocity)
	hTime = hImage/hVel #  ''
	h_t = np. arange(hTime, tEnd, dt)
	w_t = np.arange(wTime,tEnd , dt )
	hLength = np.multiply(h_t, hVel)
	wLength = 0 * np.ones(len(w_t))



elif wVel <0 and hVel<0:
	wTime = wImage/wVel # second time of stimulus f(velocity)
	hTime = hImage/hVel #  ''
	h_t = np. arange(hTime, tEnd, dt)
	w_t = np.arange(wTime,tEnd , dt )
	hLength = np.multiply(h_t, hVel)
	wLength = np.multiply(w_t, wVel)


if hVelOp == 0 and wVelOp<0 :
	
	wTimeOp = wImage/wVelOp # second time of stimulus f(velocity)
	hTimeOp = hImage/wVelOp #  ''
	h_tOp = np. arange(hTimeOp, tEnd, dt)
	w_tOp = np.arange(wTimeOp,tEnd , dt )
	wLengthOp = np.multiply(w_tOp, wVelOp)
	hLengthOp = 0 * np.ones(len(h_tOp))

elif wVelOp == 0 and hVelOp<0:
	wTimeOp = wImage/hVelOp # second time of stimulus f(velocity)
	hTimeOp = hImage/hVelOp #  ''
	h_tOp = np. arange(hTimeOp, tEnd, dt)
	w_tOp = np.arange(wTimeOp,tEnd , dt )
	hLengthOp = np.multiply(h_tOp, hVelOp)
	wLengthOp = 0 * np.ones(len(w_tOp))

elif wVelOp == 0 and hVelOp == 0:
	wLengthOp = 0 * np.ones(len(w_t))
	hLengthOp = 0 * np.ones(len(h_t))

elif wVelOp<0 and hVelOp<0:
	wTimeOp = wImage/wVelOp # second time of stimulus f(velocity)
	hTimeOp = hImage/wVelOp #  ''
	h_tOp = np. arange(hTimeOp, tEnd, dt)
	w_tOp = np.arange(wTimeOp,tEnd , dt )
	hLengthOp = np.multiply(h_tOp, hVelOp)
	wLengthOp = np.multiply(w_tOp, wVelOp)

if wVel == 0 and hVel == 0:
	wLength = 0 * np.ones(len(w_tOp))
	hLength = 0 * np.ones(len(h_tOp))

#print len(hLength)

fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
#writerOut = cv2.VideoWriter('stim_fps_'+str(fps) +'_v_' +str(velStim)+'_l_'+str(lStim)+ '_x_'+ str(xStart)+ '_Sc_'+str(scaleCon)+'.avi', fourcc, fps , (outWidth, outHeight))
writerOut = cv2.VideoWriter('stimBasil.avi', fourcc, fps , (outWidth, outHeight))
a = []
for i in range(len(wLength)) :
	xTopLeft1 = int(round(wLength[i]))
	yTopLeft1 = int(round( (hLength[i])))
	xBottomRight1 = int(round(wImage - wLengthOp[i]))
	yBottomRight1 = int(round(hImage - hLengthOp[i]))
	# xBottomRight1 = int(round(wImage))
	# yBottomRight1 = int(round(hImage))
	figureSquare1 = cv2.rectangle(img,(xTopLeft1,yTopLeft1),(xBottomRight1,yBottomRight1),scaleCon, thickness = cv2.FILLED )
	#cv2.imshow('figureSquare1', img)
	imgResize = cv2.resize(img, (outWidth, outHeight) , interpolation = cv2.INTER_AREA )
	cv2.waitKey(int(math.ceil(dt)))
	writerOut.write(imgResize)
	a.append(xTopLeft1)
	#print xTopLeft1

# plt.plot(h_t, a)
# plt.show()

writerOut.release()

cv2.destroyAllWindows()
