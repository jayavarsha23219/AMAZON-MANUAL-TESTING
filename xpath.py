from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import os

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15)

# =========================================================
# TC01 - OPEN REGISTRATION PAGE
# =========================================================

driver.get(
    "https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php"
)

driver.maximize_window()
time.sleep(3)


# =========================================================
# TC02 - NAME
# =========================================================

name = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='First Name']")
    )
)

name.send_keys("Jayavarsha")
time.sleep(2)


# =========================================================
# TC03 - EMAIL
# =========================================================

email = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[contains(@placeholder,'example.com')]")
    )
)

email.send_keys("jayavarsha@gmail.com")
time.sleep(2)


# =========================================================
# TC04 - FEMALE RADIO BUTTON
# =========================================================

female = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//label[normalize-space()='Female']/preceding-sibling::input[@type='radio']"
        )
    )
)

driver.execute_script(
    "arguments[0].click();",
    female
)

time.sleep(2)


# =========================================================
# TC05 - MOBILE
# =========================================================

mobile = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[starts-with(@placeholder,'Enter Mobile')]")
    )
)

mobile.send_keys("9876543210")
time.sleep(2)


# =========================================================
# TC06 - DATE OF BIRTH
# =========================================================

dob = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//input[@type='date']")
    )
)

driver.execute_script(
    """
    arguments[0].value = '2006-03-31';

    arguments[0].dispatchEvent(
        new Event('input', {bubbles:true})
    );

    arguments[0].dispatchEvent(
        new Event('change', {bubbles:true})
    );
    """,
    dob
)

time.sleep(2)


# =========================================================
# TC07 - SUBJECT
# =========================================================

subject = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//input[@placeholder='Enter Subject']")
    )
)

subject.send_keys("Python")
time.sleep(2)


# =========================================================
# TC08 - SPORTS CHECKBOX
# =========================================================

sports = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//label[normalize-space()='Sports']/preceding-sibling::input[@type='checkbox']"
        )
    )
)

driver.execute_script(
    "arguments[0].click();",
    sports
)

time.sleep(2)


# =========================================================
# TC09 - PICTURE
# =========================================================

picture = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//input[@type='file' and @id='picture']"
        )
    )
)

file_path = r"C:\Users\admin\OneDrive\รูปภาพ\profile.jpg"

if os.path.isfile(file_path):

    picture.send_keys(file_path)

    print("Picture selected successfully")

else:

    print("Picture file not found:")
    print(file_path)

time.sleep(3)


# =========================================================
# TC10 - CURRENT ADDRESS
# =========================================================

address = wait.until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            "//label[normalize-space()='Current Address:']/following-sibling::div//textarea"
        )
    )
)

driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    address
)

time.sleep(2)

address.click()
address.clear()

address.send_keys(
    "Chennai, Tamil Nadu"
)

print("Current Address entered successfully")

time.sleep(3)


# =========================================================
# TC11 - STATE
# =========================================================

state_element = wait.until(
    EC.presence_of_element_located(
        (By.XPATH, "//select[1]")
    )
)

state = Select(state_element)

print("State options:")

for option in state.options:
    print(option.text)

time.sleep(2)

state.select_by_visible_text("Uttar Pradesh")

print("Uttar Pradesh selected")

time.sleep(5)


# =========================================================
# TC12 - CITY
# =========================================================

city = driver.find_element(
    By.XPATH,
    "//select[@id='city']"
)

Select(city).select_by_visible_text("Agra")

# =========================================================
# TC13 - FIND ALL INPUT FIELDS
# =========================================================

all_inputs = driver.find_elements(
    By.XPATH,
    "//input"
)

print(
    "Total input fields:",
    len(all_inputs)
)

time.sleep(2)


# =========================================================
# TC14 - SECOND TEXTBOX
# =========================================================

textboxes = driver.find_elements(
    By.XPATH,
    "//input[@type='text']"
)

print(
    "Total textboxes:",
    len(textboxes)
)

if len(textboxes) >= 2:

    second_textbox = textboxes[1]

    print("Second textbox found")

time.sleep(2)


# =========================================================
# TC15 - DYNAMIC ELEMENT
# =========================================================

dynamic_elements = driver.find_elements(
    By.XPATH,
    "//input[contains(@placeholder,'Enter')]"
)

print(
    "Dynamic elements:",
    len(dynamic_elements)
)

time.sleep(2)


# =========================================================
# TC16 - PARENT
# =========================================================

parent = name.find_element(
    By.XPATH,
    "./parent::*"
)

print(
    "Parent element:",
    parent.tag_name
)

time.sleep(2)


# =========================================================
# TC17 - ANCESTOR
# =========================================================

form = name.find_element(
    By.XPATH,
    "./ancestor::form"
)

print("Form found")

time.sleep(2)


# =========================================================
# TC18 - FOLLOWING
# =========================================================

following = name.find_element(
    By.XPATH,
    "./following::input[1]"
)

print("Following element found")

time.sleep(2)


# =========================================================
# TC19 - LOGIN BUTTON
# =========================================================

login_button = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            "//*[self::input or self::button]"
            "[@value='Login' or normalize-space()='Login']"
        )
    )
)

driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});",
    login_button
)

time.sleep(3)


# =========================================================
# TC20 - CLICK LOGIN
# =========================================================

driver.execute_script(
    "arguments[0].click();",
    login_button
)

print("Login button clicked")

time.sleep(5)


# =========================================================
# FINAL DETAILS
# =========================================================

print("Registration process completed")

print(
    "Current URL:",
    driver.current_url
)

print(
    "Page title:",
    driver.title
)

input("Press Enter to close...")

driver.quit()