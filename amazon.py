from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# --- ANTI-BOT CONFIGURATION ---
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Remove navigator.webdriver flag in Chrome
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get("https://www.amazon.in/")
wait = WebDriverWait(driver, 15)

try:
    # Step 1: Account / Sign-In Navigation
    login = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="nav-link-accountList"]/button'))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", login)
    login.click()

    signin = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="nav-flyout-ya-signin"]/a/span'))
    )
    signin.click()

    # Step 2: Login Credentials
    mobile = wait.until(EC.element_to_be_clickable((By.ID, "ap_email_login")))
    mobile.send_keys("8148136669")

    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="continue"]/span/input')))
    button.click()

    password = wait.until(EC.element_to_be_clickable((By.ID, 'ap_password')))
    password.send_keys("Varsha@3101")

    signin_btn = wait.until(EC.element_to_be_clickable((By.ID, "signInSubmit")))
    signin_btn.click()
    print("Login Successfully")

    # Step 3: Search for iPhone
    searchbox = wait.until(EC.element_to_be_clickable((By.ID, "twotabsearchtextbox")))
    searchbox.clear()
    searchbox.send_keys("iPhone 18 Pro")

    searchicon = wait.until(EC.element_to_be_clickable((By.ID, "nav-search-submit-button")))
    searchicon.click()
    print("Product Search Success")

    # Step 4: Select iPhone from Search Results
    driver.execute_script("window.scrollBy(0, 500);")
    product_link = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//a[contains(@href, "/dp/") or contains(@href, "/sspa/click")][.//span[contains(text(), "iPhone")]]')
        )
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", product_link)
    product_link.click()
    print("Product clicked")

    # Step 5: Switch to Product Tab
    wait.until(lambda d: len(driver.window_handles) > 1)
    driver.switch_to.window(driver.window_handles[-1])
    print("Product page opened. Current URL:", driver.current_url)

    # Step 6: Select Variant Options (Storage/Color) if required by Amazon
    time.sleep(2)
    try:
        storage_btn = driver.find_element(By.XPATH, '//input[contains(@aria-labelledby, "size_name") or contains(@aria-labelledby, "color_name")]')
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", storage_btn)
        storage_btn.click()
        print("Selected product variant")
        time.sleep(1)
    except Exception:
        print("Variant pre-selected or not required")

    # Step 7: Multi-Selector Cart Search with Presence Check
    cart_selectors = [
        '//input[@id="add-to-cart-button"]',
        '//button[@id="add-to-cart-button"]',
        '//*[@id="add-to-cart-button"]',
        '//input[@name="submit.add-to-cart"]',
        '//button[@name="submit.add-to-cart"]',
        '//*[@id="attach-adds-to-cart-button"]'
    ]

    cartbutton = None
    for selector in cart_selectors:
        try:
            cartbutton = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, selector))
            )
            if cartbutton:
                print(f"Found cart button with selector: {selector}")
                break
        except Exception:
            continue

    if cartbutton:
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", cartbutton)
        time.sleep(1)
        try:
            cartbutton.click()
        except Exception:
            driver.execute_script("arguments[0].click();", cartbutton)
        print("Clicked Add to Cart button successfully")
    else:
        print("Cart button not found among expected selectors")

    # Step 8: Handle Side-Drawer or Direct Cart Navigation
    time.sleep(5)
    try:
        drawer_cart_btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="attach-view-cart-button-form"]//input | //*[@id="sw-gtc"]//a'))
        )
        drawer_cart_btn.click()
        print("Navigated to cart via drawer")
    except Exception:
        driver.get("https://www.amazon.in/gp/cart/view.html")
        print("Navigated to cart directly via URL")

    # Step 9: Proceed to Checkout
    proceed = wait.until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="sc-buy-box-ptc-button"]//input | //input[@name="proceedToRetailCheckout"]'))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", proceed)
    proceed.click()
    print("Proceeded to checkout")

    time.sleep(30)

finally:
    driver.quit()