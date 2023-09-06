from selenium.webdriver import EdgeOptions, Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import time

inicio = time()


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
        driver.get("https://www.gps-coordinates.net/my-location")
    except Exception as e:
        return "ERROR GETTING LINK", e

    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "lat"))
        )
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "lng"))
        )

        lat = driver.find_element(By.ID, "lat").text.split(" /")[0]
        lng = driver.find_element(By.ID, "lng").text.split(" /")[0]
    except Exception as e:
        return "ERROR PARSING LOCATION", e

    driver.quit()
    return lat, lng, f"https://www.google.com/maps/place/{lat},{lng}"


if __name__ == "__main__":
    lat,lng,link = (geolocation())

    tempo = float(str(time() - inicio)[:4])
    print({
        "lat":lat,
        "lng":lng,
        "link":link,
        "time":tempo
    })