import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

"""
    xpath es una estructura XML (objetos)
    Relativo : Busca en todo el arbol donde este ese nodo (Mas utilizado)
    Absoluta : Busca solo en esa ruta (Este es si no cambia un elemento de ubicación) 
"""

class Usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')
    
    def test_buscar_por_xpath(self):
        driver = self.driver
        driver.get('https://www.google.com')
        time.sleep(3)

        buscar_x_xpath = driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
        time.sleep(3)
        buscar_x_xpath.send_keys("selenium", Keys.ARROW_DOWN)
        time.sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()






