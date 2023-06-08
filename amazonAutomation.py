from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# exec_path = ('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Firefox.lnk')
driver = webdriver.Firefox()
driver.get('https://www.amazon.com')
driver.maximize_window()
time.sleep(3)
menu_btn = driver.find_element('id','nav-hamburger-menu')
menu_btn.click()
time.sleep(3)

login_btn = driver.find_element('id', 'hmenu-customer-name')
login_btn.click()
time.sleep(3)

username_field = driver.find_element('id', 'ap_email')
username_field.send_keys('user@gmail.com')
username_field.send_keys(Keys.RETURN)
time.sleep(5)

password_field = driver.find_element('id', 'ap_password')
with open(r'c:\\Users\\hp\Desktop\\testbed1\\CSR.txt', 'r') as x: # password in CSR.txt
    password = x.read()
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)
time.sleep(4)
print('Login is success')





# url = ("https://www.gmail.com")
# driver = webdriver.Firefox()
# driver.get(url)
# # time.sleep(25)
# driver.implicitly_wait(3)
# element = driver.find_element(By.ID, 'foo')
# driver.find_element('identifierId').send_Keys(my_username)
# driver.find_elements_('identifierId').send_Keys(my_username)

# driver.find_element(By.Id'Next').click()
# driver.implicitly_wait(60)
# driver.find_element('password').send_keys(my_password)
# driver.find_element('passwordNext').click()
