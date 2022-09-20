import ImageScripts
import scriptshelp
from time import sleep
########################################################
link_canaltech = 'https://canaltech.com.br/'
########################################################
########################################################
class Article():
    def __init__(self, link, img_url, title, author, content_1, content_2):
        self.link = link
        self.img_url = img_url
        self.title = title
        self.author = author
        self.content_1 = content_1
        self.content_2 = content_2
    pass

def goTo(driver,category):
    driver.get(link_canaltech + category)
    

def getArticlesWebElements( driver, category):
    goTo(driver,category)
    div_articles = driver.find_element_by_xpath(
        '//div[contains(@class,"pg-article")]')
    return div_articles.find_elements_by_tag_name('article')


def getArticle(id, driver, category):
    article = getArticlesWebElements(driver,category)[id]
    link = article.find_element_by_tag_name('a').get_attribute('href')
    driver.get(link)

    meta_infos_webelement = driver.find_element_by_xpath(
        '//span[@class="meta-info"]')

    link = scriptshelp.shortenLink(link)
    title = driver.find_element_by_xpath(
        '//h1[contains(@class,"titulo-principal")]').text
    author = meta_infos_webelement.find_element_by_tag_name('a').text
    content_1 = driver.find_elements_by_xpath('//p')[0].text
    content_2 = driver.find_elements_by_xpath('//p')[1].text
    img_url = driver.find_element_by_xpath(
        '//img[@class="header__img"]').get_attribute('src')

    ImageScripts.getImgFromWeb(img_url,'post.png')
    ImageScripts.convert('post.png','post.png','png')

    return Article(link, img_url, title, author, content_1, content_2)


def showRecentArticles(driver,category):
    articles = getArticlesWebElements(driver, category)
    count_article = 0
    for article in articles:
        link = article.find_element_by_tag_name('a').get_attribute('href')
        title = article.find_element_by_tag_name('h3').text
        spans = article.find_elements_by_tag_name('span')
        date = spans[0].text
        category = spans[1].text

        print(
        f"""
#####################################
| Id: {count_article}
| Titulo: {title}
| Categoria: {category}
| Postado há: {date}
#####################################""")
        count_article += 1

########################################################