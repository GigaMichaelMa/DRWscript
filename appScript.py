from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.file_detector import UselessFileDetector
from pynput.keyboard import Key, Controller
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox("/home/loli/pyHac")
driver.get("https://boards.greenhouse.io/drweng/jobs/1795561?gh_src=63484a9c1")

# driver.find_element_by_id("first_name").send_keys("Ebony")
# driver.find_element_by_id("last_name").send_keys("Moore")
# driver.find_element_by_id("email").send_keys("workfreerhack@gmail.com")
# driver.find_element_by_id("job_application_location").send_keys("Ebony")
# driver.find_element_by_id("phone").send_keys("Ebony")
# # resume_attatch = driver.find_element_by_xpath(
# #     '//*[@id="main_fields"]/div[9]/div/div[3]/a[1]')
# # resume_attatch.click()

# # keyboard = Controller()
# # keyboard.press("r")
# # keyboard.release("r")
# # keyboard.press(Key.enter)
# # keyboard.release(Key.enter)

# driver.find_element_by_xpath(
#     '//*[@id="s2id_education_school_name"]/a/span[1]').click()
# univ = driver.find_element_by_xpath(
#     '//*[@id="select2-drop"]/div/input')
# univ.send_keys("university of vermont")
# time.sleep(1)
# univ.send_keys(Keys.ENTER)


# driver.find_element_by_xpath(
#     '//*[@id="s2id_education_degree"]/a/span[1]').click()
# deg = driver.find_element_by_xpath('//*[@id="select2-drop"]/div/input')
# deg.send_keys('ba')
# time.sleep(1)
# deg.send_keys(Keys.ENTER)

# driver.find_element_by_xpath(
#     '//*[@id="s2id_education_discipline"]/a/span[1]').click()
# dis = driver.find_element_by_xpath('//*[@id="select2-drop"]/div/input')
# dis.send_keys("infor")
# time.sleep(1)
# dis.send_keys(Keys.ENTER)

# driver.find_element_by_xpath(
#     '//*[@id="education_section"]/div/fieldset/div[4]/fieldset/input[1]').send_keys("08")
# driver.find_element_by_xpath(
#     '//*[@id="education_section"]/div/fieldset/div[4]/fieldset/input[2]').send_keys("2012")

# driver.find_element_by_xpath(
#     '//*[@id="education_section"]/div/fieldset/div[5]/fieldset/input[1]').send_keys("05")
# driver.find_element_by_xpath(
#     '//*[@id="education_section"]/div/fieldset/div[5]/fieldset/input[2]').send_keys("2014")


#basically, fugma
# driver.execute_script("scroll(0, 1000);")

# job = driver.find_element_by_id(
#     "job_application_answers_attributes_2_answer_selected_options_attributes_2_question_option_id")
# driver.find_element_by_xpath(
#     '//*[@id="s2id_job_application_answers_attributes_2_answer_selected_options_attributes_2_question_option_id"]/a/span[1]').click()
# driver.execute_script("scroll(0, 1000);")

# Select(job).select_by_value('35264648')
driver.execute_script("scroll(0, 1000);")
driver.find_element_by_id(
    'job_application_answers_attributes_5_text_value').send_keys("No")
