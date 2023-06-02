import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import threading
import cv2
import numpy as np

def amin():
    print("Тa horoolol sodon_harhorin yarmag talbai_urd hotin_tuw гэсэн 5н байршилаас нэгийг сонгож бичнэ үү")
    locations = input('--> ')


    def no_traf():
            # Set the path to the web driver executable
        webdriver_path = 'C:\Program Files\Google\Chrome\Application'

        # Configure the web driver
        options = Options()
        options.headless = True  # Run the browser in headless mode (without GUI)
        driver = webdriver.Chrome(executable_path=webdriver_path, options=options)

        location = locations

        if 'horoolol' in location:
            url = 'https://www.google.com/maps/@47.9191906,106.871925,14.9z?entry=ttu'
        elif 'sodon_harhorin' in location:
            url = 'https://www.google.com/maps/@47.9165843,106.8268367,14.9z?entry=ttu'
        elif 'yarmag' in location:
            url = 'https://www.google.com/maps/@47.8777736,106.8302329,14.08z?entry=ttu'
        elif 'talbai_urd' in location:    
            url = 'https://www.google.com/maps/@47.9009703,106.9118133,14.08z?entry=ttu'
        elif 'hotin_tuw' in location:
            url = 'https://www.google.com/maps/@47.9190529,106.9176701,14.63z?entry=ttu'
        else:
            print('уучлаарай та сонголтонд байхгүй үг ашигласан тул хотын төвийн ерөнхий байдлаар авлаа')
            location = 'main_loc'
            url = 'https://www.google.com/maps/@47.9132844,106.8742878,13.54z?entry=ttu'  # Replace with your desired URL
        driver.get(url)

        # Create the screenshot filename using the timestamp
        screenshot_path = f'traffic_jam/screenshot_{location}1.png'  # Replace with the desired path to save the screenshot

        # Delete the previous screenshot if it exists
        if os.path.exists(screenshot_path):
            os.remove(screenshot_path)

        # Save the new screenshot
        driver.save_screenshot(screenshot_path)

        ntraf_percent = []
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

        image_path = screenshot_path

        # Specify the color ranges as a list of tuples: (color_name, lower_color, upper_color)
        color_ranges = [
            ('Green', np.array([40, 50, 50]), np.array([80, 255, 255])),
            ('Red', np.array([0, 100, 100]), np.array([10, 255, 255])),
            ('Orange', np.array([11, 100, 100]), np.array([21, 255, 255]))
        ]

        # Call the function to calculate the percentages of the colors
        color_percentages = calculate_color_percentages(image_path, color_ranges)

        # Display the results
        for color_name, color_percentage in color_percentages.items():
            print(f"The image contains approximately {color_percentage:.2f}% {color_name} color.")
            ntraf_percent.append(f"{color_percentage:.2f}")
        print(ntraf_percent)
        driver.quit()
        return ntraf_percent

    def sc_map():
        # Set the path to the web driver executable
        webdriver_path = 'C:\Program Files\Google\Chrome\Application'

        # Configure the web driver
        options = Options()
        options.headless = True  # Run the browser in headless mode (without GUI)
        driver = webdriver.Chrome(executable_path=webdriver_path, options=options)

        location = locations

        if 'horoolol' in location:
            url = 'https://www.google.com/maps/@47.9191906,106.871925,14.9z/data=!5m1!1e1?entry=ttu'
        elif 'sodon_harhorin' in location:
            url = 'https://www.google.com/maps/@47.9165843,106.8268367,14.9z/data=!5m1!1e1?entry=ttu'
        elif 'yarmag' in location:
            url = 'https://www.google.com/maps/@47.8777736,106.8302329,14.08z/data=!5m1!1e1?entry=ttu'
        elif 'talbai_urd' in location:    
            url = 'https://www.google.com/maps/@47.9009703,106.9118133,14.08z/data=!5m1!1e1?entry=ttu'
        elif 'hotin_tuw' in location:
            url = 'https://www.google.com/maps/@47.9190529,106.9176701,14.63z/data=!5m1!1e1?entry=ttu'
        else:
            print('уучлаарай та сонголтонд байхгүй үг ашигласан тул хотын төвийн ерөнхий байдлаар авлаа')
            location = 'main_loc'
            url = 'https://www.google.com/maps/@47.9132844,106.8742878,13.54z/data=!5m1!1e1?entry=ttu'  # Replace with your desired URL
        driver.get(url)

        # Create the screenshot filename using the timestamp
        screenshot_path = f'traffic_jam/screenshot_{location}.png'  # Replace with the desired path to save the screenshot

        # Delete the previous screenshot if it exists
        if os.path.exists(screenshot_path):
            os.remove(screenshot_path)

        # Save the new screenshot
        driver.save_screenshot(screenshot_path)

        ntraf_percent = no_traf()
        ntraf_percent = [float(x) for x in ntraf_percent]
        print(ntraf_percent)
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
        percent = ntraf_percent
        for i in range(len(colors)):
            color_percentages[colors[i]] = color_percentages[colors[i]] - percent[i]

        # Find the color with the maximum percentage
        max_color = max(color_percentages, key=color_percentages.get)
        max_percentage = color_percentages[max_color]

        # Display the results
        for color_name, color_percentage in color_percentages.items():
            print(f"The image contains approximately {color_percentage:.2f}% {color_name} color.")
        if max_color == 'Orange':
            print('Түгжрэлийн түвшин дундаж байна')
        elif max_color == 'Red':
            print('Түгжрэлийн түвшин өндөр байна')
        elif max_color == 'Green':
            print('Түгжрэлийн түвшин бага байна')
        # green_color = f"{color_percentages['Green']:.2f}"
        # red_color = f"{color_percentages['Red']:.2f}"
        # orange_color = f"{color_percentages['Orange']:.2f}"
        # if -1.5 < max_percentage - orange_color < 1.5:
        #     print('Түгжрэлийн түвшин дундажаас доогуур байна')
        # elif -1.5 < orange_color - red_color < 1.5:
        #     print('Түгжрэлийн түвшин дундажаас дээгүүр байна')
        # elif -1.5 < green_color - orange_color < 1.5:
        #     print('Түгжрэлийн түвшин дундажаас доогуур байна')

        # print(green_color, red_color, orange_color)

        driver.quit()
    sc_map()