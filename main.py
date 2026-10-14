# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By


# driver = webdriver.Chrome()
# driver.maximize_window()

# def print_course(file):
#     time.sleep(3)
#     items = driver.find_elements(By.CLASS_NAME, 'course-item')
    
#     for i in items:
#         if i.text.strip():
#             file.write(f'{i.text}\n{"-" * 30}\n')


        

# try:
#     driver.get(url='https://smartcode.am/hy/')
#     with open('text.txt', 'w', encoding='utf-8') as file:
#         time.sleep(3)
#         print_course(file)

#         driver.find_element(By.CSS_SELECTOR, 'body > main > section.courses.bg-silver > div > div.section-box > div > ul > li:nth-child(2)').click()
        
#         print_course(file)

#         driver.find_element(By.CSS_SELECTOR,'body > main > section.courses.bg-silver > div > div.section-box > div > ul > li:nth-child(3)').click()
#         # time.sleep(3)
#         print_course(file)

#         driver.find_element(By.CSS_SELECTOR,'body > main > section.courses.bg-silver > div > div.section-box > div > ul > li:nth-child(4)').click()
#         # time.sleep(3)
#         print_course(file)

#         driver.find_element(By.CSS_SELECTOR, 'body > main > section.courses.bg-silver > div > div.section-box > div > ul > li:nth-child(5)').click()
#         # time.sleep(3)
#         print_course(file)

#         driver.find_element(By.CSS_SELECTOR,'body > main > section.courses.bg-silver > div > div.section-box > div > ul > li:nth-child(6)').click()
#         # time.sleep(3)
#         print_course(file)


# except Exception as ex:
#     print(ex.__class__.__name__)
# finally:
#     driver.close()
#     driver.quit()

    
