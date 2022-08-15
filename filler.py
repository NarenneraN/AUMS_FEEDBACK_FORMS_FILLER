from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

website = 'https://aumscb.amrita.edu/cas/login?service=https%3A%2F%2Faumscb.amrita.edu%2Faums%2FJsp%2FCore_Common%2Findex.jsp%3Ftask%3Doff'
path = 'E:\MY_WORKS\chromedriver'

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)


# 1. Filling the username and password

# Username Xpath - //input[@id="username"]
# Password Xpath - //input[@id="password"]
# Submit Button - //input[@class="btn-submit"]
driver.implicitly_wait(5)
username_box = driver.find_element(by="xpath",value='//input[@id="username"]')
password_box = driver.find_element(by="xpath",value='//input[@id="password"]')
submit_btn = driver.find_element(by="xpath",value='//input[@class="btn-submit"]')
username_box.send_keys('CB.EN.U4CSE20044')
password_box.send_keys('Naren464Dhiran')
submit_btn.click()
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"maincontentframe")))
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"Iframe1")))
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"sakaiframeId")))

# 2. Click the arrow button near home

# Arrow Xpath - //a[@class="Mrphs-sitesNav__dropdown"]
# elem = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "Mrphs-sitesNav__dropdown Mrphs-sitesNav__dropdown--hover")) #This is a dummy element
#     )
arrow_place = driver.find_element(by="xpath",value='//a[@class="Mrphs-sitesNav__dropdown"]')
arrow_place.click()
driver.implicitly_wait(5)

# 3. Click Evaluation system
# Eval system Xpath - //span[@class="Mrphs-sitesNav__submenuitem-title"]
eval_place = driver.find_elements(by="xpath",value='//span[@class="Mrphs-sitesNav__submenuitem-title"]')
eval_place[3].click()
driver.implicitly_wait(5)

times_visited = 0

WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"Mainc3b7fc40x29e7x45a6xa2f9xb8cdbbec80d4")))
while True:
    times_visited += 1
    # 4.
    # Total Times to fill - //table[@class="evalsysTable"]/tbody/tr
    subjects_list = driver.find_elements(by="xpath",value='//table[@class="evalsysTable"]/tbody/tr')
    subj_list_info = driver.find_elements(by="xpath",value='//table[@class="evalsysTable"]/tbody/tr/td[2]/span')
    i = 0

    for subjects in subjects_list:
        i = i+1
        WebDriverWait(driver, 600).until(
            EC.presence_of_element_located((By.XPATH, '//table[@class="evalsysTable"]/tbody/tr/td[2]/span')))
        subj_list_info = subjects.find_element(by="xpath", value='./td[2]/span')
        if subj_list_info.text == 'Pending':
            print(i)
            sub_link = subjects.find_element(by="xpath",value='./td/a')
            sub_link.click()
            questions_list = driver.find_elements(by="xpath",value='//table[@class="fullDisplayHorizontalScale fullDisplayHorizontal"]/tbody/tr')
            for questions in questions_list:
                first_opt = questions.find_element(by="xpath", value='./td/span/input')
                first_opt.click()
            submit_btn_end = driver.find_element(by="xpath", value='//input[@id="form-branch::submitEvaluation"]')
            submit_btn_end.click()
            driver.implicitly_wait(5)
            break
    if times_visited==len(subjects_list):
        break
    else:
        print("Submitted")

print("----JOB OVER---BYEE")
# driver.quit()