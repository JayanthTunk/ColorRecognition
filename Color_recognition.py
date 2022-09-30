import numpy as np
import pandas as pd
import cv2
import imutils


cam = cv2.VideoCapture(0)

r = g = b = x_position = y_position = 0

index = ['color', 'name_of_the_color', 'hex', 'R', 'G', 'B']
df = pd.read_csv('/home/jay/Documents/HCL Internship/colors.csv', names = index, header = None)


def ColorName(R,G,B):
	min = 10000
	for i in range(len(df)):
		j = abs(R - int(df.loc[i,"R"])) + abs(G - int(df.loc[i,"G"])) + abs(B - int(df.loc[i,"B"]))
		if (j <= min):
			min = j
			color_name = df.loc[i, 'name_of_the_color'] + '   Hex=' + df.loc[i, 'hex']
	return color_name


def color_identification(event, x, y, flags, param):
	global b, g, r, x_position, y_position, clicked
	x_position = x
	y_position = y
	b, g, r = frame[y,x]
	b = int(b)
	g = int(g)
	r = int(r)


cv2.namedWindow('Jayanth s Color recognition')
cv2.setMouseCallback('Jayanth s Color recognition', color_identification)

while True:
    (grabbed, frame) = cam.read()
    frame = imutils.resize(frame, width=900)
    kernal = np.ones((5, 5), "uint8")
    cv2.rectangle(frame, (20,20), (800, 60),(b,g,r), -1)    
    text = ColorName(b,g,r) + '   R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
    cv2.putText(frame,text, (50,50),2, 0.8, (255,255,255),2,cv2.LINE_AA)
    
    if(r+g+b >= 600):
        cv2.putText(frame,text,(50,50), 2, 0.8, (0,0,0),2,cv2.LINE_AA)   
        
    cv2.imshow('Jayanth s Color recognition',frame)
    
    if cv2.waitKey(20) & 0xFF == 27:
        break
    
cam.release()
cv2.destroyAllWindows()









