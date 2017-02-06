import selenium.webdriver as webdriver
import time
import os

driver = webdriver.Firefox()
driver.implicitly_wait(15)

# Login
albert_login = "https://admin.portal.nyu.edu/psp/paprod/EMPLOYEE/CSSS/c/\
SA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL?FolderPath=PORTAL_ROOT_OBJECT.NYU_STUDENT_CTR&\
IsFolder=false&IgnoreParamTempl=FolderPath%252cIsFolder&cmd=login&errorCode=127&languageCd=ENG"

driver.get(albert_login)
username = driver.find_element_by_id("userid")
password = driver.find_element_by_id("pwd")
username.send_keys(os.environ['NETID'])
password.send_keys(os.environ['NYU_PASSWORD'])
button = driver.find_element_by_class_name("psloginbutton")
button.click()

# Get and switch to the correct frame that has all the required information
frames = driver.find_elements_by_tag_name('frame')
frame = frames[1]
driver.switch_to_frame(frame)

# Go to Search
search = driver.find_element_by_id('DERIVED_SSS_SCR_SSS_LINK_ANCHOR2')
search.click()

time.sleep(5)
# Find the correct class and go to that link
cs = driver.find_element_by_link_text("Computer Science (CSCI-UA)")
cs.click()

time.sleep(5)
# Click "See more details"
details = driver.find_element_by_id("NYU_CLS_DERIVED_TERM$31")
details.click()

time.sleep(5)
# Get all details div and print the status
ml = driver.find_element_by_id("win0divNYU_CLS_SBDTLVW_CRSE_ID$31")
spans = ml.find_elements_by_tag_name("span")
print(spans[8].text)

