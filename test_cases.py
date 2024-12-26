import selenium
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_successful_login():
    # Set up WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Navigate to the URL
    driver.get("https://a_leibpaqkgx3.v7.demo.nocobase.com/signin?redirect=/admin")
    print("Page opened successfully")

    # Locate the username/email field and enter text
    try:
        username_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username/Email']"))
        )
        username_field.send_keys("admin@nocobase.com")
        print("Entered username/email")
    except Exception as e:
        print(f"Error locating username/email field: {e}")
        driver.quit()
        return

    # Locate the password field and enter text
    try:
        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']"))
        )
        password_field.send_keys("admin123")
        print("Entered password")
    except Exception as e:
        print(f"Error locating password field: {e}")
        driver.quit()
        return

    # Locate the sign-in button and click it
    try:
        sign_in_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        sign_in_button.click()
        print("Clicked sign-in button")
    except Exception as e:
        print(f"Error locating sign-in button: {e}")
        driver.quit()
        return

    # Wait for the admin dashboard to load
    try:
        WebDriverWait(driver, 20).until(EC.title_contains("Admin Dashboard"))
        print("Admin Dashboard loaded")
    except Exception as e:
        print(f"Error loading Admin Dashboard: {e}")
        driver.quit()
        return

    # Verify the result (example: check the page title)
    expected_title = "Admin Dashboard"
    actual_title = driver.title
    assert expected_title == actual_title, f"Test Failed: {actual_title} != {expected_title}"
    print("Login successful")

    # Close the browser
    driver.quit()

# Run the test case
test_successful_login()

def test_invalid_login():
    # Set up WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Navigate to the URL
    driver.get("https://a_leibpaqkgx3.v7.demo.nocobase.com/signin?redirect=/admin")
    print("Page opened successfully")

    # Locate the username/email field and enter text
    try:
        username_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username/Email']"))
        )
        username_field.send_keys("invalid_user")
        print("Entered invalid username/email")
    except Exception as e:
        print(f"Error locating username/email field: {e}")
        driver.quit()
        return

    # Locate the password field and enter text
    try:
        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']"))
        )
        password_field.send_keys("invalid_password")
        print("Entered invalid password")
    except Exception as e:
        print(f"Error locating password field: {e}")
        driver.quit()
        return

    # Locate the sign-in button and click it
    try:
        sign_in_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        sign_in_button.click()
        print("Clicked sign-in button")
    except Exception as e:
        print(f"Error locating sign-in button: {e}")
        driver.quit()
        return

    # Verify the result (example: check for error message)
    try:
        error_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='error-message']"))
        )
        assert error_message.is_displayed(), "Test Failed: Error message not displayed"
        print("Error message displayed")
    except Exception as e:
        print(f"Error locating error message: {e}")
        driver.quit()
        return

    # Close the browser
    driver.quit()

# Run the test case
test_invalid_login()

def test_password_masking():
    # Set up WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Navigate to the URL
    driver.get("https://a_leibpaqkgx3.v7.demo.nocobase.com/signin?redirect=/admin")
    print("Page opened successfully")

    # Locate the password field and enter text
    try:
        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']"))
        )
        password_field.send_keys("password")
        print("Entered password")
    except Exception as e:
        print(f"Error locating password field: {e}")
        driver.quit()
        return

    # Verify that the password field masks the entered characters
    assert password_field.get_attribute("type") == "password", "Test Failed: Password field is not masked"
    print("Password field is masked")

    # Close the browser
    driver.quit()

# Run the test case
test_password_masking()

def test_navigation_to_users_page():
    # Set up WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Navigate to the URL
    driver.get("https://a_leibpaqkgx3.v7.demo.nocobase.com/signin?redirect=/admin")
    print("Page opened successfully")

    # Log in with valid credentials
    try:
        username_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Username/Email']"))
        )
        username_field.send_keys("admin@nocobase.com")
        print("Entered username/email")

        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Password']"))
        )
        password_field.send_keys("admin123")
        print("Entered password")

        sign_in_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        sign_in_button.click()
        print("Clicked sign-in button")
    except Exception as e:
        print(f"Error during login: {e}")
        driver.quit()
        return

    # Wait for the page to load after login
    try:
        # Add a wait for a specific element or an indication that the login is successful
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='button' and @aria-label='Users']"))
        )
        print("Logged in successfully")
    except Exception as e:
        print(f"Error during login process: {e}")
        driver.quit()
        return

    # Wait for the Users button to be available and click it
    try:
        users_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='button' and @aria-label='Users']"))
        )
        users_button.click()
        print("Clicked Users button")

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='button' and @aria-label='Users']"))
        )
        print("Users page loaded")
    except Exception as e:
        print(f"Error loading Users page: {e}")
        driver.quit()
        return

    # Verify the result (check the URL or page title)
    try:
        # Wait until the title has the expected value
        WebDriverWait(driver, 20).until(
            lambda driver: "Users" in driver.title
        )
        actual_title = driver.title
        expected_title = "Users"
        assert expected_title == actual_title, f"Test Failed: {actual_title} != {expected_title}"
        print("Navigation to Users page successful")
    except Exception as e:
        print(f"Error verifying the page title or URL: {e}")
        driver.quit()
        return

    # Close the browser
    driver.quit()



def test_deactivate_user():
    # Set up WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Navigate to the Leads page
    try:
        leads_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='button' and @aria-label='Leads']"))
        )
        leads_button.click()
        print("Clicked Leads button")

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='button' and @aria-label='Leads']"))
        )
        print("Leads page loaded")
    except Exception as e:
        print(f"Error loading Leads page: {e}")
        driver.quit()
        return

    # Search for the lead
    try:
        search_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@class='ant-input css-9akr02' and @type='text']"))
        )
        search_field.send_keys("Billy Bennett")
        print("Entered lead name")

        filter_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@role='button' and @aria-label='action-Action-Filter-submit-lead-filter-form']"))
        )
        filter_button.click()
        print("Clicked Filter button")
    except Exception as e:
        print(f"Error searching for lead: {e}")
        driver.quit()
        return

    # Deactivate the lead
    try:
        deactivate_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@role='button' and @aria-label='action-Action.Link-Deactivate-customize:update-lead-table-Billy Bennett']"))
        )
        deactivate_button.click()
        print("Clicked Deactivate button")
    except Exception as e:
        print(f"Error deactivating lead: {e}")
        driver.quit()
        return

    # Press the first confirmation button
    try:
        confirmation_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and @class='ant-btn css-52f0p9 ant-btn-primary']"))
        )
        confirmation_button.click()
        print("Clicked first OK button")
    except Exception as e:
        print(f"Error clicking first OK button: {e}")
        driver.quit()
        return

    # Press the final OK button
    try:
        final_ok_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and @class='ant-btn css-52f0p9 ant-btn-primary']"))
        )
        final_ok_button.click()
        print("Clicked final OK button")
    except Exception as e:
        print(f"Error clicking final OK button: {e}")
        driver.quit()
        return

    # Verify the lead is deactivated
    try:
        inactive_leads = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='ant-select-selection-overflow']"))
        )
        assert "Billy Bennett" in inactive_leads.text, "Test Failed: Lead not deactivated"
        print("Lead deactivated successfully")
    except Exception as e:
        print(f"Error verifying deactivation: {e}")
        driver.quit()
        return

    driver.quit()


def test_convert_lead_to_user():
    # Set up WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Convert the lead to a user
    try:
        convert_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@role='button' and @aria-label='action-Action.Link-Convert to user-customize:popup-lead-table-Dr. Darryl Daniel']"))
        )
        convert_button.click()
        print("Clicked Convert to user button")
    except Exception as e:
        print(f"Error converting lead to user: {e}")
        driver.quit()
        return

    # Press the confirmation button
    try:
        confirmation_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@role='button' and @aria-label='action-Action-Convert to user-customize:triggerWorkflows-lead-form-Dr. Darryl Daniel']"))
        )
        confirmation_button.click()
        print("Clicked Convert to user confirmation button")
    except Exception as e:
        print(f"Error clicking Convert to user confirmation button: {e}")
        driver.quit()
        return

    # Press the final OK button
    try:
        final_ok_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='button' and @class='ant-btn css-52f0p9 ant-btn-primary']"))
        )
        final_ok_button.click()
        print("Clicked final OK button")
    except Exception as e:
        print(f"Error clicking final OK button: {e}")
        driver.quit()
        return

    # Verify the lead is converted to a user
    try:
        user_list = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='ant-select-selection-overflow']"))
        )
        assert "Dr. Darryl Daniel" in user_list.text, "Test Failed: Lead not converted to user"
        print("Lead converted to user successfully")
    except Exception as e:
        print(f"Error verifying conversion: {e}")
        driver.quit()
        return

    driver.quit()



# Run the test cases
test_navigation_to_users_page()
test_deactivate_user()
test_convert_lead_to_user()
