# Scenario-1: Setup
# 1.Launch Browser with the url https://rahulshettyacademy.com/seleniumPractise/#/
# 2.Search the keyword "Ber"
# 3.Click on all the products displayed in the search result page
# 4. Save the names of the products
# 5. Click on cart-icon and click to checkout
#
# Scenario-2: Assertion and Validations
# 1.Verify products should be same in both search result page and shopping cart page
# 2.Verify whether Price decreases after applying discount
# 3.Sum of the products in the checkout page matches with the total amount of order summary

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#Launch Browser
driver= webdriver.Chrome(executable_path="C:\\Users\\Habeeba.Shaik\\Downloads\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

#Declare empty list to store the names of the products dynamically
expected_names=[]
actual_names=[]

#Search with the keyword "Ber"
driver.find_element_by_xpath("//*[@id='root']/div/header/div/div[2]/form/input").send_keys("ber")
time.sleep(4)

#Get the common xpath for all the Add to cart Button
products = driver.find_elements_by_xpath("//*[@class='product-action']/button")

#Iterate through individual buttons and append the list of product names to the declared list
for product in products:
   expected_names.append(product.find_element_by_xpath("parent::div/parent::div/h4").text)
   product.click()
print(expected_names)

#Clicking on Cart icon and proceeding with checkout
driver.find_element_by_xpath("//*[@id='root']/div/header/div/div[3]/a[4]/img").click()
driver.find_element_by_xpath("//*[@id='root']/div/header/div/div[3]/div[2]/div[2]/button").click()

#Get the common locator for the product names
veggies=driver.find_elements_by_css_selector("p.product-name")

#Itearate through individual buttons and append the list of product names to the declared list
for veggie in veggies:
    actual_names.append(veggie.text)
print(actual_names)

#Verify products should be same in both search result page and shopping cart page
#As actualName list return 3 empty string, slicing the empty string
assert expected_names == actual_names[:3]

#Get the value of the Total amount
time.sleep(2)
total_price = driver.find_element_by_xpath("//*[@class='discountAmt']").text
print(total_price)

#Using explicit wait as promo code takes time to locate
wait=WebDriverWait(driver,8)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='promoCode']")))
#Apply the promocode
driver.find_element_by_xpath("//*[@class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element_by_xpath("//*[@class='promoBtn']").click()
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//*[@class='promoInfo']")))

#Capture the discounted price
discount_Price = driver.find_element_by_xpath("//*[@class='discountAmt']").text

#Verify whether Price decreases after applying discount
assert float(discount_Price) < int(total_price)

#Get the sum of total of all product in the table
sum=0
amounts=driver.find_elements_by_xpath("//tr/td[5]/p")
for amount in amounts:
    sum=sum+int(amount.text)
print(sum)

#Capture the actual total from the order summary
total_amount=driver.find_element_by_xpath("//*[@class='totAmt']").text

#Sum of the products in the checkout page matches with the total amount of order summary
assert int(total_amount) == sum

driver.close()