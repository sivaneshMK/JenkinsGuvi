from selenium import webdriver


def test_login_with_valid_cred():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com")
    print(driver.title)