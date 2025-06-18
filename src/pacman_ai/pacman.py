from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver


def pacman_cords(driver:webdriver):

    pacman = driver.find_element(By.ID,"pacman")
    y = pacman.value_of_css_property("top")
    x = pacman.value_of_css_property("left")
    return {"x":x,"y":y}


def pacman_arrow(driver:webdriver):
    pacman_arrow = driver.find_element(by.ID,"pacman_arrow")
    arrow_url = pacman_arrow.value_of_css_property("background-image")
    arrow = arrow_url.replace("url(&quot;app/style/graphics/spriteSheets/characters/pacman/arrow_","").replace(".svg&quot;)","")
    return arrow 




