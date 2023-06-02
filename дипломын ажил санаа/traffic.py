import cv2
import numpy as np
import autosc

def find_color_regions(image_loc, lower_red, upper_red, lower_green, upper_green, lower_orange,upper_orange, min_contour_area=100):
    image = cv2.imread(image_loc)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    mask_red = cv2.inRange(hsv_image, lower_red, upper_red)
    mask_green = cv2.inRange(hsv_image, lower_green, upper_green)
    mask_orange = cv2.inRange(hsv_image, lower_orange, upper_orange)
    mask = cv2.bitwise_or(mask_red, mask_green, mask_orange)
    
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filter contours based on area
    contours = [contour for contour in contours if cv2.contourArea(contour) > min_contour_area]
    
    # Draw bounding boxes or contours around the color regions
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
    cv2.imshow('Color Regions', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Specify the color range (in HSV space)
lower_red = np.array([0, 100, 100])    # Lower threshold for red color in HSV
upper_red = np.array([10, 255, 255])   # Upper threshold for red color in HSV

lower_green = np.array([40, 50, 50])
upper_green = np.array([80, 255, 255])

lower_orange = np.array([11, 100, 100])
upper_orange = np.array([21, 255, 255])

# Call the function with the image path and color range values
screenshot_path = autosc.sc_map()
image_loc = screenshot_path
print(image_loc)
find_color_regions(image_loc, lower_red, upper_red, lower_green, upper_green, lower_orange,upper_orange, min_contour_area=100)
