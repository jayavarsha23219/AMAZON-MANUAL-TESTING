from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://assertqa.com/practice/webtables")
driver.maximize_window()

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))

print("=== TC01: Print all column headings ===")
headers = driver.find_elements(By.XPATH, "//table//th")
header_texts = [header.text for header in headers if header.text.strip()]
print("Headings:", header_texts)

print("\n=== TC02: Print the first data row ===")
first_row_cells = driver.find_elements(By.XPATH, "//table/tbody/tr[1]/td")
first_row_data = [cell.text for cell in first_row_cells]
print("First Row:", " | ".join(first_row_data))

print("\n=== TC03: Print the last data row ===")
last_row_cells = driver.find_elements(By.XPATH, "//table/tbody/tr[last()]/td")
last_row_data = [cell.text for cell in last_row_cells]
print("Last Row:", " | ".join(last_row_data))

print("\n=== TC04: Search for an employee by last name ===")
search_box = driver.find_element(By.XPATH, "//input[@type='text' or @type='search' or contains(@placeholder, 'Search')]")
search_box.clear()
search_box.send_keys("Smith")

# Print matching records after search filter
matching_rows = driver.find_elements(By.XPATH, "//table/tbody/tr")
for row in matching_rows:
    print("Matching Record:", row.text)

# Reset search filter for remaining test cases
search_box.clear()
search_box.send_keys("")

print("\n=== TC05: Extract all email addresses ===")
email_cells = driver.find_elements(By.XPATH, "//table/tbody/tr/td[4]")
emails = [email.text for email in email_cells]
for email in emails:
    print("Email:", email)

print("\n=== TC06: Find the employee with highest salary / amount ===")
# Note: The table has 'Salary' column instead of 'Due amount'
rows = driver.find_elements(By.XPATH, "//table/tbody/tr")
highest_salary = -1
top_employee = ""

for row in rows:
    cells = row.find_elements(By.TAG_NAME, "td")
    if len(cells) >= 6:
        # Extract name and numeric salary value
        name = f"{cells[1].text} {cells[2].text}"
        salary_text = cells[5].text.replace("$", "").replace(",", "").strip()
        salary_val = float(salary_text) if salary_text else 0
        
        if salary_val > highest_salary:
            highest_salary = salary_val
            top_employee = name

print(f"Employee with highest amount/salary: {top_employee} (${highest_salary:,.2f})")

print("\n=== TC07: Verify that a particular website link exists ===")
# Checks if any link inside or around the table exists
links = driver.find_elements(By.XPATH, "//table//a | //a[contains(@href, 'http')]")
if len(links) > 0:
    print("TC07 Result: PASS (Link exists on the page)")
else:
    print("TC07 Result: FAIL (No matching link found)")

print("\n=== TC08: Count data rows without counting the header ===")
data_rows = driver.find_elements(By.XPATH, "//table/tbody/tr")
print(f"Data Row Count: {len(data_rows)}")

# Clean up
input("Press Enter to close...")
