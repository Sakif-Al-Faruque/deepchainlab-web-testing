from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

try: 
    # load chrome driver
    driver = webdriver.Chrome("chromedriver-win64\chromedriver.exe")

    # maximize the chrome browser window
    driver.maximize_window()
    # open the deepchainlabs login page
    driver.get("http://sqa.deepchainlabs.com/login")

    # print the title of this page
    print(driver.title)

    # select the input fields and button for login
    user_email_field = driver.find_element_by_id("emailField")
    user_password_field = driver.find_element_by_id("passwordField")
    user_login_button = driver.find_element_by_css_selector("div.t-place-items-center div.t-mt-4 div.t-cursor-pointer")


    # pass values to the input fields
    user_email_field.send_keys("admindcl@gmail.com")
    user_password_field.send_keys("adminpassword")


    time.sleep(5)
    # click on login button
    user_login_button.click()


    # move to blog page
    time.sleep(5)
    blog_page_link = driver.find_element_by_css_selector("div.t-z-20 div.t-hidden div.t-fixed div.t-mt-4 div.t-cursor-pointer div.t-flex p")
    blog_page_link.click()



    #move to create blog page
    time.sleep(5)
    blog_create_page_link = driver.find_element_by_css_selector("div.t-py-8 div.t-flex div.t-gap-4 span.t-cursor-pointer")
    blog_create_page_link.click()



    # fill up the create blog section
    time.sleep(2)
    blog_input_text_fields = driver.find_elements_by_tag_name("input")
    blog_input_text_fields[0].send_keys("rest api")
    blog_input_text_fields[1].send_keys("api")
    blog_input_text_fields[3].click()
    time.sleep(2)
    blog_input_text_fields[4].send_keys("5")


    # click on the publish button
    time.sleep(2)
    publish_btn = driver.find_elements_by_tag_name("button")
    publish_btn[0].click()


    # as the publish button does not work properly, the cancel button is clicked. That returns to blog list page
    time.sleep(5)
    back_to_blog_list = driver.find_element_by_css_selector("div.t-mt-8 span.t-cursor-pointer")
    back_to_blog_list.click()
finally:
    # at the end, close the browser
    time.sleep(5)
    driver.quit()