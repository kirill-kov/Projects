from selenium import webdriver
import time
import pyautogui

def scrShots():
    i=0

    while i<1:
        print("screenshot " + str(i) + " is done!")
        time.sleep(0.5)
        pyautogui.screenshot('/Users/Admin/Desktop/screenshots/image'+str(i)+'.jpg')
        i+=1
        #time.sleep(2)

def auth_test():
    lg = "login"
    ps = "password"

    driver = webdriver.Chrome()
    driver.get("http://www.metacpa.ru")

    time.sleep(4)

    auth = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div[2]/ul/li[4]/a')
    auth.click()

    fill_login = driver.find_element_by_id('LoginForm_username')
    fill_login.send_keys(lg)
    fill_password = driver.find_element_by_id('LoginForm_password')
    fill_password.send_keys(ps)

    btn = driver.find_element_by_id('yw0')
    btn.click()

    scrShots()

    time.sleep(2)
    driver.close()


def main():
    auth_test()

if __name__ == '__main__':
    main()
