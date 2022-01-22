from tracemalloc import start
from pyautogui import screenshot 
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time  
import keyboard 

DRIVER_PATH = r'C:\Users\laksh\Documents\ChromeDriver\chromedriver.exe'
IMG_PATH = './Dataset'
LINK = 'https://google.com'

def start_browser(driver):
 
    driver.get(LINK) 
    driver.maximize_window()
    time.sleep(10)  

# To keep adding frames of training sets 
def return_x():
    '''
    Used for indexing purpose.
    '''
    try:
        f = open('x.txt', 'r') 
        x = f.read() 
        f.close()
        return int(x)
    except: 
        write_x('0')
        return 0
    
def write_x(x):
    f = open('x.txt', 'w') 
    f.write(str(x)) 
    f.close() 

def capture_img(driver): 

    x = return_x()
    while True: 
        time.sleep(3) 
        img = screenshot() 
        img.save(f'{IMG_PATH}/frame_{x}.png') 
        x += 1

        if keyboard.is_pressed('q'):
            driver.close()
            break
    
    write_x(x) 

if __name__ == "__main__":
    driver = webdriver.Chrome(DRIVER_PATH) 
    start_browser(driver) 
    capture_img(driver) 
