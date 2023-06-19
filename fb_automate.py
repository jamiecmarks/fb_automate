# use selenium to automate and improve facebook marketplace searching
# made by https://github.com/jamiecmarks/

import sys, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# log in, arguments from the commandline
try:
    username = sys.argv[1]
except IndexError:
    username = ""

try:
    pwd = sys.argv[2]
except IndexError:
    pwd = ""


# webdriver initation


opts = webdriver.ChromeOptions()
opts.add_argument("--start-maximized");
opts.add_argument("--disable-notifications")



driver = webdriver.Chrome(options=opts)

driver.get("https://www.facebook.com/login/?next=%2Fmarketplace%2F")

# logging in using username and password
elem_email = driver.find_element(By.NAME, "email")
elem_email.send_keys(username)

elem_pwd = driver.find_element(By.NAME, "pass")
elem_pwd.send_keys(pwd)

elem_pwd.send_keys(Keys.RETURN)

# Wait for the login process to complete and the second page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.url_contains("marketplace"))

# specific search
driver.get("https://www.facebook.com/marketplace/melbourne/search?daysSinceListed=1&query=watch&exact=false")



for _ in range(100):
    driver.execute_script("""
    window.scrollTo(0, document.body.scrollHeight);""")
    time.sleep(0.2)

driver.execute_script("""
window.scrollTo(0, document.body.scrollHeight);

window.scrollTo(0, 0);



let divs = document.querySelectorAll(".x8gbvx8 > .x9f619")
const banned = ['india','samsung', 'apple', 'xiaomi', 'galaxy', 'smart', 'garmin', 'sponsored', 'google', 'g shock', 'fit']


for (var i = 0; i < divs.length; i++) {
   	let txt = divs[i].textContent;
  	for (var j = 0; j < banned.length; j++){
    	if (txt.toLowerCase().includes(banned[j])){
          	divs[i].remove()
      		break;
    	}
	}
}
""")

while True:
    pass

