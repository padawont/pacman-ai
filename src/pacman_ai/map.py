from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
                                    
def amout_dots(driver:webdriver):
    dots_container = driver.find_element(by.ID,"dot-container")
    number_of_dots = 0
    number_of_powerpellts = 0
    for dot in dots_container:
        if dots_container[0].value_of_css_property("height") == 10:
            number_of_dots + 1
        elif dots_container[0].value_of_css_property("height") == 40:
            number_of_powerpellts + 1
        else:
            pass
    return {"dots":number_of_dots,"powerpellts":number_of_powerpellts}


def cord_dots(driver:webdriver):
    dots_container = driver.find_element(by.ID,"dot-container")
    number_of_dots = 0
    number_of_powerpellts = 0
    i = 0
    cord = {}
    for dot in dots_container:
        if dots_container[i].value_of_css_property("height") == 10:
            cord[number_of_dots + 1] = dots_container
            i + 1 
        elif dots_container[i].value_of_css_property("height") == 40:
            cord[number_of_powerpellts + 1] = dots_container
            i + 1 
        else:
            pass
    return cord




