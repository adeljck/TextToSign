# coding=utf-8
import base64
import requests
from selenium import webdriver


def generatesign(name: str) -> str:
    base_url = "http://shouxieti.shufazi.cn/"
    browser = webdriver.Chrome(executable_path="./chromedriver.exe")
    browser.get(base_url)
    browser.find_element_by_css_selector("#ziti > option:nth-child(6)").click()
    browser.find_element_by_id("fontcolor").clear()
    browser.find_element_by_id("fontcolor").send_keys("#000")
    browser.find_element_by_id("colors").clear()
    browser.find_element_by_id("colors").send_keys("#fff")
    browser.find_element_by_css_selector("#sizes > option:nth-child(7)").click()
    browser.find_element_by_id("text").clear()
    browser.find_element_by_id("text").send_keys(name)
    browser.find_element_by_css_selector(
        "#form > div > div.form-group.col-xs-12.col-sm-4.col-md-2.col-lg-2.pull-right > div > button").click()
    img_link = browser.find_element_by_id("SaveImg").get_attribute("src")
    sign_b64 = url_to_base64(img_link)
    return sign_b64


def url_to_base64(url):
    response = requests.get(url)
    encoded = base64.b64encode(response.content)
    return encoded.decode()
