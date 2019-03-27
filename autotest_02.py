from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://www.mail.ru")

news = browser.find_elements_by_css_selector('.news-item__inner')

hrefs = browser.find_elements_by_css_selector('.news-item__inner a')

i=0

for x in news:
    print(x.text)
    print(hrefs[i].get_attribute('href'))
    i+=1

browser.close()
