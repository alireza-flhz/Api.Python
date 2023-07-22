import time
import json
from flask import *
from selenium import webdriver
from flask import render_template, request
from flask import session, make_response, url_for, redirect


app = Flask(__name__, static_folder='static')


@ app.route('/', methods=['GET'])
def Get_Collections():
    driver = webdriver.Chrome(
        r"C:\Users\JTP\PycharmProjects\SeleniumTest\Browsers\chromedriver.exe")
    driver.get("https://salviamed.co.uk/")
    driver.find_element_by_xpath(
        "//*[@id='Events']/div/ul/li[4]/div/a").click()
    time.sleep(3)
    return "ok"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
