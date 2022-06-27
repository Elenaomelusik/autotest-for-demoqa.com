from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

driver.implicitly_wait(10) # seconds
driver.get('https://demoqa.com/')


elementsbut = driver.find_element("xpath", '//*[@id="app"]/div/div/div[2]/div/div[1]').click()
checkboxbut = driver.find_element("id", 'item-1').click()
homebut = driver.find_element("xpath", '//*[@id="tree-node"]/ol/li/span/label').click()
radiobut = driver.find_element("id", 'item-2').click()
impressivebut = driver.find_element("xpath", '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]').click()
yesbut = driver.find_element("xpath", '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]/label').click()

#driver.quit()
