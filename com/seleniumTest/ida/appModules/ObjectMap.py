from selenium.webdriver.support.ui import  WebDriverWait


def getElement(driver,locateType,locatorExpression):
    try:
        element = WebDriverWait(driver,30).until(lambda  x: x.find_element(by=locateType,value=locatorExpression))

        return element
    except Exception,e:
        raise  e


if __name__ == '__main__':
    from selenium import webdriver
    driver= webdriver.Chrome(executable_path="/Users/luomingsu/Downloads/python/chromedriver")
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("http://www.baidu.com")
    searchBox=getElement(driver,"id","kw")
