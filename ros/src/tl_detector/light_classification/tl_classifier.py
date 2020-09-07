from styx_msgs.msg import TrafficLight
import cv2
import numpy as np

class TLClassifier(object):
    def __init__(self):
        #TODO load classifier
        pass

    def get_classification(self, img):
        """Determines the color of the traffic light in the image

        Args:
            image (cv::Mat): image containing the traffic light

        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)

        """
        #TODO implement light color prediction
        LAB = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
        yellow = LAB[:,:,2]
        binary = np.zeros_like(yellow)
        binary[(yellow > 200) & (yellow <= 255)] = 255
        yellowcount = np.sum(binary)/255

        red = img[:,:,2]
        green = img[:,:,1]
        blue = img[:,:,0]
        
        binary = np.zeros_like(red)
        binary[(red > 240) & (red <= 255) & (green < 100)] = 255
        redcount = np.sum(binary)/255

        binary = np.zeros_like(green)
        binary[(green > 240) & (green <= 255) & (blue < 100)] = 255
        greencount = np.sum(binary)/255

        if yellowcount > 800 and redcount > 700 and greencount > 700:
            return 1  

        if redcount > 300 and greencount < 500:
            return 0

        if greencount > 700 and redcount < 500:
            return 2
#         print("Redcount", redcount)
#         print("Greencount", greencount)
#         print("Yellowcount", yellowcount)
        return 4
#         return TrafficLight.UNKNOWN
