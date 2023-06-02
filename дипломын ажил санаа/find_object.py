import cv2
import numpy as np
import autosc as autosc

def FO():
    def calculate_color_percentages(image_path, color_ranges):
        image = cv2.imread(image_path)
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        total_pixels = hsv_image.size // 3  # Total number of pixels (assuming 3 channels)
        
        color_percentages = {}
        
        for color_name, lower_color, upper_color in color_ranges:
            # Create a mask based on the color thresholds
            mask = cv2.inRange(hsv_image, lower_color, upper_color)
            
            # Count the number of pixels in the mask
            color_pixels = cv2.countNonZero(mask)
            
            # Calculate the percentage of the color
            color_percentage = (color_pixels / total_pixels) * 100
            
            # Store the color percentage in the dictionary
            color_percentages[color_name] = color_percentage
        
        return color_percentages

    # Specify the path to your image file
    screenshot_path = autosc.sc_map()
    image_path = screenshot_path

    # Specify the color ranges as a list of tuples: (color_name, lower_color, upper_color)
    color_ranges = [
        ('Green', np.array([40, 50, 50]), np.array([80, 255, 255])),
        ('Red', np.array([0, 100, 100]), np.array([10, 255, 255])),
        ('Orange', np.array([11, 100, 100]), np.array([21, 255, 255]))
    ]

    # Call the function to calculate the percentages of the colors
    color_percentages = calculate_color_percentages(image_path, color_ranges)

    colors = ['Green', 'Red', 'Orange']
    percent = [0.93, 0.01, 0.91]
    for i in range(len(colors)):
        color_percentages[colors[i]] = color_percentages[colors[i]] - percent[i]

    # Find the color with the maximum percentage
    max_color = max(color_percentages, key=color_percentages.get)
    max_percentage = color_percentages[max_color]

    # Display the results
    for color_name, color_percentage in color_percentages.items():
        print(f"The image contains approximately {color_percentage:.2f}% {color_name} color.")
    print(f"The color with the maximum percentage is {max_color} with approximately {max_percentage:.2f}%.")
    if max_color == 'Orange':
        print('Зам бага зэргийн түгжрэлтэй байна')
    elif max_color == 'Red':
        print('Зам түгжрэлтэй байна')
    elif max_color == 'Green':
        print('Зам түгжрээгүй байна')

