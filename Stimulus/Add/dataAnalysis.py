import numpy as np 
import matplotlib.pyplot as plt
import sys


# Set stimulus parameters experiment
velStim = -0.25  #m/s velocity of stimulus
lStim = 0.01 #m  half length of stimulus
xStart = 0.05 #m start approach distance away from specimen 
fps = 200 # Frame Resolution
angPix = 4.5 # deg/pixel interommatidial angle specimen

#Name layers:
nameFile = 'HueData' 
groupA1 = 'Hue'
groupB1 = 'Edge Detection'

#Imprt data from iqr neural network
data= np.genfromtxt(nameFile, delimiter = ';')
#data1= open('HueData', 'r')
#print data[:,0:4]
#print len(data)

# Define rows and columns of neural network data
#have to include to read file, so it does it automatically, search for the string Inh, etc and then take that column
# is in the firts row of the text file, so should be easy to implement
#also see what happens to data if more groups are added to the datasampling, how to classify
time= data[1:-1,0]
time 
excitatory =data[1:-1,1]
vm = data[1:-1,3]



# Calculate values stimulus
from sys import path	
path.append('/home/atilla/Documents/Test/Neural_Network/Stimulus/')
from ommatidiaStimulus2 import getParamters
tStim, lPixStim , thetaStim, xStim, dt = getParamters(velStim, xStart, fps, lStim, angPix)
thetaNorm = (thetaStim - np.amin(thetaStim)) / (np.amax(thetaStim) - np.amin(thetaStim)) 
#Scale time back to experiment
#Not certain whether this scale is correct
tStimScale = (tStim*len(data))+len(data)

# if 'Hue' in data1.read():
# 	print True

IDNums=[]
IDNames=[]
with open(nameFile) as f:
	for line in f:
		line = line.strip()
		if '#' in line:
			IDFind=line.split('"')
			IDNumber = IDFind[2]
			IDNumber = IDNumber[1:-1]
			IDName=IDFind[1]
			print IDName
			IDNums.append(IDNumber)
			IDNames.append(IDName)

print len(IDNums), IDNames



foundA1 = False 
foundB1 = False 


with open(nameFile) as f:
	for line in f:
		line = line.strip()
		if groupA1 in line and foundA1 == False:
			IDlineA1 = line.split('=')
			IDGroupA1 = IDlineA1[1]
			#print IDGroupA1
			foundA1 = True
		if groupB1 in line and foundB1 == False:
			IDlineB1 = line.split('=')
			IDGroupB1 = IDlineB1[1]
			print IDGroupB1
			foundB1 = True
g =open(nameFile, 'r')
filedata = g.read()
g.close()

#for i in len(IDNums):
newdata = filedata.replace(IDNums[1], IDNames[1])
g=open('TextOut', 'w')
g.write(newdata)
g.close()

# if foundA1 == True:
# 	newdata = filedata.replace(IDGroupA1, groupA1)
# if foundB1 == True:
# 	g = open(nameFile, 'w')
# 	g.write(newdata)
# 	g.close()
#will probably produce an error if not there, 			
	
with open(nameFile) as f:
	for line in f:
		line = line.strip()
		if 'cycle' in line:
			IDLine = line.split(';')
			print IDLine

			groupA1Exc_avg=data[1:-1, IDLine.index(groupA1 + '_excIn_RangeAverage')]
			groupA1Vm_avg= data[1:-1, IDLine.index(groupA1 + '_vm_RangeAverage')]



			print groupA1Exc_avg










plt.plot(time,excitatory, 'r',time,vm, 'b')
plt.plot(tStimScale,thetaStim, 'm', tStimScale, thetaNorm, 'g')
plt.show()