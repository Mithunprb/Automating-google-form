#!usr/bin/python3
# Import Module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time

#Firefox driver config
#feel free to use chrome, safari etc
driver = webdriver.Firefox()

driver.get('https://forms.gle/2AKYz8eqm3AYvfPC7')

#wait for 5 sec
time.sleep(5)

#You can data that you want to add
#in input text 
datas = [
    ['Sample Name', 'herergos@email'],
    ['First Last', 'putemail@email.domain'],
]


# Iterate through each data
for data in datas:
                                                        # Initialize count is zero
    count = 0

                                                        # contain input boxes
    textboxes = driver.find_elements_by_class_name(
        "quantumWizTextinputPaperinputInput")

    
    #remember to copy xpath not html not id/class xpath from <label>
    check1_0 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[4]/label')

    check1_1 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[2]/label')

    check1_2 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div/span/div/div[3]/label')

    check1  = random.choice([check1_0, check1_1, check1_2])
    check1.click()

    check2_0 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div[1]/label')

    check2_1 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div[1]/label')

    check2_2 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div[2]/label')

    check2_3 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div/span/div/div[4]/label')
    
    check2  = random.choice([check2_0, check2_1, check2_2, check2_3])
    check2.click()

    check3_0 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div/span/div/div[1]/label')
    
    check3_1 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div/span/div/div[2]/label')
    check3 = func = random.choice([check3_0, check3_1])
    check3.click()
    
    check4_0 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div/span/div/div[4]/label')

    check4_1 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div/span/div/div[6]/label')
    check4_2 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div/span/div/div[5]/label')
    check4  = random.choice([check4_0, check4_1, check4_2])
    check4.click()

    check5_0 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div/span/div/div[1]/label')
    check5_1 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/div/span/div/div[2]/label')
    check5  = random.choice([check5_0, check5_1])
    check5.click()  

    check6_0 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/div/span/div/div[1]/label')
    check6_1 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/div/span/div/div[2]/label')
    check6  = random.choice([check6_0, check6_1])
    check6.click()

    check7_0 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/div/span/div/div[1]/label')
    check7_1 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/div/span/div/div[2]/label')
    check7  = random.choice([check7_0, check7_1])
    check7.click()

    check8_0 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/div/span/div/div[3]/label')
    check8_1 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/div/span/div/div[1]/label')
    check8_2 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/div/span/div/div[2]/label')
    check8_3 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/div/span/div/div[4]/label')
    check8  = random.choice([check8_0, check8_1, check8_2, check8_3])
    check8.click()

    check9_0 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div[1]/div/span/div/div[1]/label')
    check9_1 = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[11]/div/div/div[2]/div[1]/div/span/div/div[2]/label')
    check9  = random.choice([check9_0, check9_1])
    check9.click()
                                                   # Iterate through all input boxes
    for value in textboxes:
                                                        # enter value
        value.send_keys(data[count])
                                                        # increment count value
        count += 1
                                                        # click on submit button (Remove sing in and limt of 1 respons from settings)
    submit = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit.click()

                                                                    # fill another response => (keep setting of the form for link of another response)
    another_response = driver.find_element_by_xpath(
        '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()


driver.close()
