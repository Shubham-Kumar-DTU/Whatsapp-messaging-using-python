from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
driver.maximize_window()

name = input("Enter name of the user or group:")
msg = input("Enter message:")
count = int(input("Enter count:"))

input("Enter anything after scanning QR code")

user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
user.click()

msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[1]/div/div[2]")

for i in range(count):
        msg_box.send_keys(msg)
        driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]/button").click()


print("Success")

#//*[@id="pane-side"]/div[1]/div/div/div[10]/div/div/div[2]/div[1]/div[1]/span/span

