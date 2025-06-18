from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver


def main():
    driver = webdriver.Chrome()

    driver.get("https://freepacman.org/")
    pacman = driver.find_element(By.ID,"pacman")
    y = pacman.value_of_css_property("top")
    y = pacman.value_of_css_property("left")

    driver.quit()

main()