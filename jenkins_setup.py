from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(executable_path='E:\chromedriver.exe')
driver.get('http://localhost:8091/login?from=%2F')


def log_in(username, password):
    try:
        
        user_name_input = driver.find_element_by_xpath('//input[@name="j_username"]')
        user_name_input.send_keys(username)
        password_input = driver.find_element_by_xpath('//input[@name="j_password"]')
        password_input.send_keys(password)
        password_input.submit()
        time.sleep(3)
    except Exception as e:
        error = True
        print(e)




def check_manage_jenkins():
    try:
       manage=  driver.find_element_by_partial_link_text('Manage Jenkins')
       manage.click()
    except Exception as e:
        error = True
        print(e)



def check_global_tool_conf():
    try:
        global_tool= driver.find_element_by_partial_link_text('Global Tool Configuration')
        global_tool.click()
    except Exception as e:
        error= True
        print(e)




# jdk entry
def set_jdk():
    try:
        driver.execute_script("window.scrollTo(document.body.scrollHeight/1.5,document.body.scrollHeight/3.0);")
        # //*[@id="jenkins"]
        driver.find_element_by_xpath("//*[@id='yui-gen20-button']").click();
        el = driver.find_element_by_xpath('//*[@id="jenkins"]')
        el.click()
        if (driver.find_element_by_id(("cb2")).is_selected()):
            driver.find_element_by_id("cb2").click()
        # //*[@id="yui-gen13"]/table/tbody/tr[1]/td[3]/input
        el = driver.find_element_by_xpath("//*[@id='yui-gen13']/table/tbody/tr[1]/td[3]/input")
        el.clear()
        el.send_keys("JAVA_HOME")
        # //*[@id="yui-gen13"]/table/tbody/tr[3]/td[3]/input
        el = driver.find_element_by_xpath("//*[@id ='yui-gen13']/table/tbody/tr[3]/td[3]/input")
        el.clear()
        el.send_keys("C:\\Program Files\\Java\\jdk-9.0.4")

        time.sleep(3)
    except Exception as e:
        error = True
        print(e)


# git entry
def set_git():
    try:
        driver.execute_script("window.scrollTo(document.body.scrollHeight/1.25,document.body.scrollHeight/2);")
        if (driver.find_element_by_id(("cb3")).is_selected()):
            driver.find_element_by_id("cb3").click()
        # //*[@id="yui-gen5"]/table/tbody/tr[2]/td[3]/input
        el = driver.find_element_by_xpath("//*[@id='yui-gen5']/table/tbody/tr[2]/td[3]/input")
        el.clear()
        el.send_keys("Default")

        # //*[@id ='yui-gen5']/table/tbody/tr[4]/td[3]/input

        el = driver.find_element_by_xpath("//*[@id ='yui-gen5']/table/tbody/tr[4]/td[3]/input")
        el.clear()
        el.send_keys("C:\\Program Files\\Git\\bin\\git.exe")

        time.sleep(3)
    except Exception as e:
        error = True
        print(e)


# maven
def set_maven():
    try:
        driver.execute_script("window.scrollTo(document.body.scrollHeight/1.2,document.body.scrollHeight/1.5);")
        driver.find_element_by_xpath("//*[@id='yui-gen21-button']").click();
        if (driver.find_element_by_id(("cb4")).is_selected()):
            driver.find_element_by_id("cb4").click()
        # //*[@id="yui-gen15"]/table/tbody/tr[2]/td[3]/input
        el = driver.find_element_by_xpath("//*[@id='yui-gen15']/table/tbody/tr[1]/td[3]/input")
        el.clear()
        el.send_keys("MAVEN_HOME")

        # //*[@id ='yui-gen15']/table/tbody/tr[4]/td[3]/input

        el = driver.find_element_by_xpath("//*[@id ='yui-gen15']/table/tbody/tr[3]/td[3]/input")
        el.clear()
        el.send_keys("C:\\Users\\Ravi\\Downloads\\Compressed\\apache-maven-3.6.1-bin\\apache-maven-3.6.1")

        time.sleep(3)
    except Exception as e:
        error = True
        print(e)


#Apply and save
def save_apply():
    try:
        driver.execute_script("window.scrollTo(document.body.scrollHeight,document.body.scrollHeight/1.25);")
        # //*[@id="yui-gen22-button"]
        driver.find_element_by_xpath("//*[@id='yui-gen22-button']").click();
        time.sleep(10)
        driver.find_element_by_xpath("//*[@id='yui-gen37-button']").click();
    except Exception as e:
        error = True
        print(e)

log_in("ravikumar", "Ravi@1997")
check_manage_jenkins()
check_global_tool_conf()
set_jdk()
set_git()
set_maven()
save_apply()