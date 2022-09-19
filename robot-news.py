import canaltech
import instagram
import canva
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from dotenv import load_dotenv
########################################################


def getDriver():
    option = Options()
    option.add_argument('--profile-directory=./')
    option.add_argument('--user-data-dir=./')
    driver = webdriver.Firefox(firefox_options=option)
    driver.set_window_position(0, 0)
    driver.set_window_size(800, 800)
    return driver

########################################################


load_dotenv()
email = os.getenv('email')
password = os.getenv('password')
name_account = os.getenv('name_account')
driver = getDriver()

########################################################

canaltech.showRecentArticles(driver, 'seguranca')

id_article = input('\n-> Insira o ID da noticia: ')
article = canaltech.getArticle(int(id_article), driver)

canva.open()
canva.newTab()
canva.setTitle(article.title)
canva.uploadImg()
canva.setImage()
canva.saveImage()
canva.exit()

instagram.goTo(driver)
instagram.auth(driver, email, password)
instagram.post(driver, article.author, article.link,
               article.content_1, article.content_2)

driver.close()
