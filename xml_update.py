from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
import time


def page_web(the_path):

    # This is the driver of the enginee (chrome, firefox , etc)
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

    # Link of the page web
    driver.get("https://red.cofidi.com.mx/Chrysler/Upload.aspx")

    # The first window 
    user = driver.find_element_by_xpath("//*[@id=\"ctl00_MainContent_Wizard1_TextBox2\"]")
    user.send_keys("crobles@raloy.com.mx")
    user.send_keys(Keys.ENTER)

    password = driver.find_element_by_xpath("//*[@id=\"ctl00_MainContent_Wizard1_TextBox3\"]")
    password.send_keys("CHR5870M")
    password.send_keys(Keys.ENTER)

    button_next = driver.find_element_by_xpath("//*[@id=\"ctl00_MainContent_Wizard1_StartNavigationTemplateContainerID_StartNextButton\"]")
    button_next.click()

    # The second window 
    user_step_two = driver.find_element_by_xpath("//*[@id=\"ctl00_MainContent_Wizard1_TextBox17\"]")
    user_step_two.send_keys("crobles@raloy.com.mx")
    user_step_two.send_keys(Keys.ENTER)

    select_element = driver.find_element_by_id("ctl00_MainContent_Wizard1_cboTipoServicio")
    select = Select(select_element)
    select.select_by_value("4")

    # Upload file(xml) here
    archivo_xml = driver.find_element_by_id('ctl00_MainContent_Wizard1_FileUpload1')
    archivo_xml.send_keys(the_path)


    button_up =  driver.find_element_by_xpath("//*[@id=\"ctl00_MainContent_Wizard1_StepNavigationTemplateContainerID_StepNextButton\"]")
    button_up.click()

    # Finish the process , choose the option in the page
    try:
        button_finish = driver.find_element_by_xpath("//*[@id=\"ctl00_MainContent_Wizard1_FinishNavigationTemplateContainerID_FinishButton\"]")
        button_finish.click()
    except:
        pass
    

def path():
    """ The function take page_web(), as cicle in the path """
    folder_contend = os.listdir(os.path.dirname(os.path.abspath(__file__)) + "/xml")

    conter = 0
    for i in folder_contend:
        page_web("/home/carlos/Documentos/Selenium/xml/"+i)
        conter = conter + 1
        print("Log: Num: {} | {}".format(conter, i)) 
    
    print("Log: El proceso ha terminado se subieron {} factura(s), 🏁 !!".format(conter))

"""
def way():
    folder_contend = os.listdir(os.path.dirname(os.path.abspath(__file__)) + "/xml")
    print(len(folder_contend))
"""

if __name__ == "__main__":
    path()

