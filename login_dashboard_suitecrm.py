import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import json
import mysql.connector



#login Page
driver = webdriver.Chrome()
driver.get('https://demo.suiteondemand.com/index.php?module=Users&action=Login')
driver.maximize_window()
driver.implicitly_wait(3)

user_input = driver.find_element(By.ID, 'user_name')
user_input.send_keys('will')
time.sleep(3)

password_input = driver.find_element(By.ID, 'username_password')
password_input.send_keys('will')
time.sleep(3)

login_button = driver.find_element(By.ID, 'bigbutton')
login_button.click()
time.sleep(3)

# ✅ Handle password warning popup (browser-based)
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER).perform()  # or Keys.ESCAPE

time.sleep(3)
create_button = driver.find_element(By.LINK_TEXT,'CREATE')
create_button.click()
time.sleep(5)
click_create_accounts = driver.find_element(By.LINK_TEXT,'Create Accounts')
click_create_accounts.click()

name=driver.find_element(By.ID,'name')
name.send_keys("Wisdom")
time.sleep(2)
office_phone = driver.find_element(By.XPATH,"//input[@id='phone_office']")
office_phone.send_keys("6372924295")
time.sleep(2)
website = driver.find_element(By.XPATH,"//input[@id='website']")
website.send_keys("Treenetra.com")
time.sleep(2)
fax = driver.find_element(By.ID,"phone_fax")
fax.send_keys("7890")
time.sleep(2)
email_plus_button = driver.find_element(By.XPATH,"//button[@title='Add Email Address ']")
email_plus_button.click()
email_input = driver.find_element(By.XPATH,"//input[@id='Accounts0emailAddress0']")
email_input.send_keys("treenetr@gmail.com")
#radio_button
time.sleep(2)
radio_but1 = driver.find_element(By.XPATH,"//input[@id='Accounts0emailAddressOptOutFlag0']")
radio_but1.click()
radio_but2 = driver.find_element(By.XPATH,"//input[@id='Accounts0emailAddressInvalidFlag0']")
radio_but2.click()
time.sleep(2)

#Billing_address
driver.find_element(By.XPATH,"//textarea[@id='billing_address_street']").send_keys("IRC-Village")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='billing_address_city']").send_keys("Bhubaneswar")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='billing_address_state']").send_keys("Odisha/Indian")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='billing_address_postalcode']").send_keys("752030")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='billing_address_country']").send_keys("India")
time.sleep(2)

#shipping_address

driver.find_element(By.XPATH,"//textarea[@id='shipping_address_street']").send_keys("Balugaon")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='shipping_address_city']").send_keys("Khordha")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='shipping_address_state']").send_keys("Odisha/Indian")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='shipping_address_postalcode']").send_keys("752012")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='shipping_address_country']").send_keys("India")
time.sleep(2)
driver.find_element(By.XPATH,"//textarea[@id='description']").send_keys("Please delivery faster")

#more information
type_dropdown = driver.find_element(By.XPATH,'//select[@id="account_type"]')
select = Select(type_dropdown)
select.select_by_visible_text('Customer')
industry_dropdown = driver.find_element(By.XPATH,"//select[@id='industry']")
select = Select(industry_dropdown)
select.select_by_visible_text('Chemicals')

time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='annual_revenue']").send_keys("1000cr")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='employees']").send_keys("10k")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='parent_name']").send_keys("Treenetra")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='campaign_name']").send_keys("Treenetra")
time.sleep(2)
driver.find_element(By.XPATH,"//div[@id='EditView_tabs']/following-sibling::*[2]/input[@id='SAVE']").click()
time.sleep(3)

#view_accounts
driver.find_element(By.XPATH,"//div[text()='View Accounts']").click()

driver.find_element(By.XPATH,"//div[text()='View Accounts']").click()

headers = driver.find_elements(By.XPATH, "//table[contains(@class,'list')]//thead//th")
header_names = [h.text.strip() for h in headers if h.text.strip() != '']
print(" Headers:", header_names)

rows = driver.find_elements(By.XPATH, "//table[contains(@class,'list')]/tbody/tr")
all_data = []

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    row_data = [cell.text.strip() for cell in cells]
    if row_data and len(row_data) >= len(header_names):
        data_dict = dict(zip(header_names, row_data[:len(header_names)]))
        all_data.append(data_dict)

json_file = "suitecrm_accounts.json"
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(all_data, f, indent=4)

print(f" Data saved to {json_file}")
time.sleep(8)

# --- Step 4: Connect to MySQL ---
conn = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    user='root',
    password='Nayak@99',
    database='ratnakar'
)

if conn.is_connected():
    print(" Connected to MySQL")
else:
    print(" Connection failed")

cursor = conn.cursor()

# --- Step 5: Create Table if not exists ---
cursor.execute('''
    CREATE TABLE IF NOT EXISTS crm_table (
        Name VARCHAR(50),
        City VARCHAR(50),
        Billing_country VARCHAR(20),
        Phone VARCHAR(20),
        User VARCHAR(50),
        Email VARCHAR(50),
        Date_create VARCHAR(50)
    )
''')

# --- Step 6: Extract and Insert Table Data ---
rows = driver.find_elements(By.XPATH, "//table[@class='list view table-responsive']/tbody/tr")

for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    if len(cols) >= 7:
        Name = cols[1].text.strip()
        City = cols[2].text.strip()
        Billing_country = cols[3].text.strip()
        Phone = cols[4].text.strip()
        User = cols[5].text.strip()
        Email = cols[6].text.strip()
        Date_create = cols[7].text.strip()

        # Insert into MySQL
        cursor.execute('''
            INSERT INTO crm_table (Name, City, Billing_country, Phone, User, Email, Date_create)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        ''', (Name, City, Billing_country, Phone, User, Email, Date_create))

conn.commit()
print("Data inserted into MySQL")
conn.close()
driver.quit()










