import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import threading
import multiprocessing

def screen():
    print("Тa horoolol sodon_harhorin yarmag talbai_urd hotin_tuw гэсэн 5н байршилаас нэгийг сонгож бичнэ үү")
    locations = input('--> ')

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

        driver.quit()
        return screenshot_path

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

        driver.quit()
        return screenshot_path

    thread1 = threading.Thread(target=sc_map)
    thread2 = threading.Thread(target=no_traf)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

