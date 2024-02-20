from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

options.add_extension("./block.crx") 

# Creating the webdriver and adding an ad block for the browser



browser = webdriver.Chrome(options=options)



browser.get("https://www.youtube.com/@MandRproductions/videos")

lengthMinutes = 0

videos = browser.find_elements(By.CLASS_NAME, "yt-core-image--fill-parent-width")


counter = 0

while lengthMinutes < 15: # Looping over the videos and checking their duration

  if counter % 3 == 0 and counter >= 1:
    
    h = 0
    v = 100
    browser.execute_script("return arguments[0].scrollIntoView(true);", videos[counter - 1]) # Scrolling down after several videos passed
    browser.execute_script("window.scrollBy(arguments[0],arguments[1])", h, v)

  videos = browser.find_elements(By.CLASS_NAME, "yt-core-image--fill-parent-width")

  time.sleep(2)
  
  
  

  videos[counter].click()
  time.sleep(2)

  durationElement = browser.find_element(By.CLASS_NAME, "ytp-time-duration") # Calculating the duration, if longer than 15 minutes we found the video we wanted
  duration = browser.execute_script("return arguments[0].textContent", durationElement)
  print(duration)

  lengthMinutes = int(duration.split(":")[0])
 

  if lengthMinutes >= 15:
    browser.get_screenshot_as_file("./photo.png") # Taking a screenshot of the video we found
  else:
    print("Too short, continuing the search..")

  counter += 1
  browser.back()
  


print("Success, video found after %d rounds. Screen shot taken!" % (counter)) # End of execution
browser.quit()