from selenium.webdriver import EdgeOptions, Edge
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def geolocation():
  options = EdgeOptions()

  prefs = {
  "profile.default_content_setting_values.geolocation": 1
  }
  options.add_experimental_option("prefs", prefs)

  options.add_argument("--headless=new")
  options.add_argument("--disable-gpu")
  options.add_argument("--disable-infobars")
  options.add_argument("--incognito")
  options.add_argument("--disable-notifications")
  options.add_argument("--disable-extensions")
  options.add_argument("--disable-software-rasterizer")
  options.add_argument("--ignore-certificate-errors")
  options.add_argument("--disable-web-security")
  options.add_experimental_option("excludeSwitches", ["enable-logging"])
  driver = Edge(options=options)

  try:
    driver.get("https://geo-locate-fnca.onrender.com/")
  except Exception as e:
    return "ERROR GETTING LINK", e
  wait = WebDriverWait(driver, 10)  
  alert = wait.until(EC.alert_is_present())

  alert_text = alert.text

  alert.accept()

  print(alert_text)

if __name__ == "__main__":
  geolocation()
