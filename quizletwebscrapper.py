from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

user_url = "https://quizlet.com/32444309/introduction-to-computer-science-flash-cards/"
user_browser = webdriver.Chrome()
user_browser.execute_script("window.scrollBy(0,document.body.scrollHeight)")
user_browser.get(user_url)

user_all = user_browser.find_elements(By.CLASS_NAME, "TermText.notranslate.lang-en")

user_words_list = []
user_defs_list = []

for i in range(len(user_all)):
    if i % 2 == 0:
        user_words_list.append(user_all[i].text)
    else:
        user_defs_list.append(user_all[i].text)

print(user_words_list)
print(user_defs_list)

user_browser.close()