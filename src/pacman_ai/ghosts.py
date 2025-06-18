from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver



def clyde_cords(driver:webdriver):

    clyde = driver.find_element(By.ID,"clyde")
    y = clyde.value_of_css_property("top")
    x = clyde.value_of_css_property("left")
    return {"x":x,"y":y}


def inky_cords(driver:webdriver):

    inky = driver.find_element(By.ID,"inky")
    y = inky.value_of_css_property("top")
    x = inky.value_of_css_property("left")
    return {"x":x,"y":y}


def pinky_cords(driver:webdriver):

    pinky = driver.find_element(By.ID,"pinky")
    y = pinky.value_of_css_property("top")
    x = pinky.value_of_css_property("left")
    return {"x":x,"y":y}


def blinky_cords(driver:webdriver):

    blinky = driver.find_element(By.ID,"blinky")
    y = blinky.value_of_css_property("top")
    x = blinky.value_of_css_property("left")
    return {"x":x,"y":y}

