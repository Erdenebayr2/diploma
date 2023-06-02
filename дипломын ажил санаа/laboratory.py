import datetime
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def sc_map():
    # Set the path to the web driver executable
    webdriver_path = 'C:\Program Files\Google\Chrome\Application'

    # Configure the web driver
    options = Options()
    options.headless = True  # Run the browser in headless mode (without GUI)
    driver = webdriver.Chrome(executable_path=webdriver_path, options=options)

    print("Тa horoolol sodon_harhorin yarmag talbai_urd hotin_tuw гэсэн 5н байршилаас нэгийг сонгож бичнэ үү")
    location = input('--> ')
    if 'horoolol' in location:
        url = 'https://www.google.com/maps/dir/@47.9102008,106.8351907,17z/data=!4m2!4m1!3e0!5m1!1e1?entry=ttu'
    driver.get(url)

    # text_field = driver.find_element(By.CSS_SELECTOR, "input")  # Adjust the CSS selector to match the desired text field
    # text_field.send_keys("Your text here")

    # Generate a timestamp for the screenshot filename
    timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    # Create the screenshot filename using the timestamp
    screenshot_path = f'traffic_jam/screenshot_{location}.png'  # Replace with the desired path to save the screenshot

    # Delete the previous screenshot if it exists
    if os.path.exists(screenshot_path):
        os.remove(screenshot_path)

    # Save the new screenshot
    driver.save_screenshot(screenshot_path)

    driver.quit()
    return screenshot_path
sc_map()