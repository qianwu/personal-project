#write a script to search flights from make my trip web page
#https://www.makemytrip.com/
from selenium import webdriver
import time

def test_select_flights_from_place_to_place():
    driver = webdriver.Chrome()
    driver.get("https://www.makemytrip.com/")
    time.sleep(5)
    driver.find_element_by_id("fromCity").click()
    driver.find_element_by_xpath("//p[text()='New Delhi']").click()
    driver.find_element_by_xpath("//p[text()='Mumbai']").click()
    driver.find_element_by_xpath("//span[text()='Search']").click()
    driver.quit()

#Write a code to print prime numbers between 1 to 50 without using any loop
def find_prime(n):
    prime_numbers = []
    if (n == 1):
        prime_numbers.append(1)
    if (n == 2):
        prime_numbers.append(2)
    if (n>2) and (n//2 == 0):
        prime_numbers.append(n)
    return prime_numbers

def find_prime_without_loop(n):
    if n > 1:
        print(2)
    if n > 2:
        print(3)
    if n > 3:
        print(5)
    if n > 5:
        print(7)
    if n > 7:
        print(11)
    if n > 11:
        print(13)
    if n > 13:
        print(17)
    if n > 17:
        print(19)
    if n > 19:
        print(23)
    if n > 23:
        print(29)
    if n > 29:
        print(31)
    if n > 31:
        print(37)
    if n > 37:
        print(41)
    if n > 41:
        print(43)
    if n > 43:
        print(47)