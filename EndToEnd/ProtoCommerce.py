# Launch browser with URL https://rahulshettyacademy.com/angularpractice/"
# 1. Click on the shopbutton
# 2. Add the product into the cart "BlackBerry" dynamically
# 3. Click on the checkout button
# 4. Validate the Product in Shopping cart page
# 5. Click to checkout
# 6. Give India in the dynamic dropdown
# 7. Select the checkbox terms and conditions and Place order
# 8. Validate the order confirmation message

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#Launch Browser
driver = webdriver.Chrome(executable_path="C:\\Users\\Habeeba.Shaik\\Downloads\\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
#Click on the shop button
driver.find_element_by_xpath("/html/body/app-root/app-navbar/div/nav/ul/li[2]/a").click()

#Get the grid and iterate to the grid until we find the desired product
grid = driver.find_elements_by_xpath("//*[@class='card h-100']")
print(len(grid))
for product in grid:
    if product.find_element_by_xpath("div/h4/a").text =="Blackberry":
        product.find_element_by_xpath("div[2]/button").click()

#Click on checkout button
driver.find_element_by_xpath("//*[@class='nav-link btn btn-primary']").click()

#Validate the product on the Shopping cart page
assert driver.find_element_by_link_text("Blackberry").text == "Blackberry"

#Click on the checkout button
driver.find_element_by_xpath("//*[@class='btn btn-success']").click()

#Enter the country into the dynamic dropdown
driver.find_element_by_xpath("//*[@id='country']").send_keys("India")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element_by_link_text("India").click()
driver.execute_script("document.getElementById('checkbox2').click()")
#driver.find_element_by_xpath("//*[@id='checkbox2']").click()
driver.find_element_by_xpath("/html/body/app-root/app-shop/div/app-checkout/div/form/input").click()
order_confirmation_message=driver.find_element_by_xpath("/html/body/app-root/app-shop/div/app-checkout/div[2]/div").text
print(order_confirmation_message)
#Validate the success message
assert "Success!" in order_confirmation_message