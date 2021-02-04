import cv2
import sys
import urllib
from urllib import request
from pylibdmtx.pylibdmtx import decode
import numpy as np

#video_capture = cv2.VideoCapture(1)  #2nd Local USB Camera

#image2 = cv2.imread('http://10.202.180.29/oneshotimage')  


while True:

    req = urllib.request.urlopen('http://10.202.180.29/oneshotimage')  #Get web camera still image sony
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    image2 = cv2.imdecode(arr, -1) # 'Load it as it is'
    
    
    # Capture frame-by-frame
    #ret, image = video_capture.read()  



    #height, width = image.shape[:2]    
    height, width = image2.shape[:2]  

    cv2.imshow("Faces found", image2)

    x = decode((image2.tobytes(), width, height))  

    for a in range(len(x)):
        print((x[a]).data.decode("utf-8"))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything is done, release the capture
#video_capture.release()
cv2.destroyAllWindows()

 