import scriptshelp
import os
from time import sleep
########################################################
link = 'https://www.instagram.com/'
########################################################


def goTo(driver):
    driver.get(link)
    sleep(4)


def auth(driver, email, password):
    inputs_form_login = driver.find_elements_by_tag_name('input')
    input_email_form_login = inputs_form_login[0]
    input_password_form_login = inputs_form_login[1]
    button_form_login = driver.find_element_by_tag_name('button')
    input_email_form_login.send_keys(email)
    input_password_form_login.send_keys(password)
    sleep(1)

    button_form_login.click()
    scriptshelp.clear_console()
    sleep(5)

def post(driver, author, link, content_1, content_2):
    btn_new_post = driver.find_elements_by_tag_name('button')[2]
    btn_new_post.click()
    sleep(1)
    input_path_image = driver.find_elements_by_tag_name('input')[1]
    input_path_image.send_keys(os.getcwd()+'\\postIg.png')
    sleep(1)
    btn_go = driver.find_elements_by_tag_name('button')[5]
    btn_go.click()
    sleep(1)
    btn_go = driver.find_elements_by_tag_name('button')[5]
    btn_go.click()
    sleep(1)
    textarea = driver.find_elements_by_tag_name('textarea')[0]
    textarea.send_keys(
        f"""{content_1}
    
{content_2}
    
#~~~~~~~~~~~~~~~~~~~
| Autor: {author}
| Continue lendo: {link} 
#~~~~~~~~~~~~~~~~~~~""")
    btn_share = driver.find_elements_by_tag_name('button')[5]
    btn_share.click()
    sleep(3)
