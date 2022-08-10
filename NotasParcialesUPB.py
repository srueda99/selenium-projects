# Imports
import unittest
import os
from dotenv import load_dotenv
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Carga las variables de entorno
load_dotenv()

class HelloWorld(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
    
    def testSIGAA(self):
        # Variables de inicio de sesión
        usuario = os.getenv("SIGAA_USER")
        contrasena = os.getenv("SIGAA_PASSWORD")
        # Se dirige a la página de SIGAA UPB
        self.driver.get('https://sigaa.upb.edu.co/BANPDN/twbkwbis.P_WWWLogin')
        # Localiza los campos a llenar
        user = self.driver.find_element(by = By.ID, value = 'usernameUserInput')
        password = self.driver.find_element(by = By.ID, value = 'password')
        signIn_btn = self.driver.find_element(by = By.XPATH, value = '//*[@id="loginForm"]/div[3]/div/button')
        # Llena los valores de inicio de sesión
        user.send_keys(usuario)
        password.send_keys(contrasena)
        signIn_btn.click()
        # Navegamos dentro de la página principal
        estudiante_btn = self.driver.find_element(by = By.ID, value = 'bmenu--P_StuMainMnu___UID2')
        estudiante_btn.click()
        menu = self.driver.find_element(by = By.ID, value = 'bmenu--P_AdminMnu___UID4')
        menu.click()
        notas_menu = self.driver.find_element(by = By.ID, value = 'contentItem22')
        notas_menu.click()
        enviar_btn = self.driver.find_element(by = By.ID, value = 'id____UID6')
        enviar_btn.click()
        # Cuenta el número de materias del estudiante
        materias_tabla = self.driver.find_element(by = By.XPATH, value = '//*[@id="contentHolder"]/div[2]/table[2]')
        materias = materias_tabla.find_elements(by = By.TAG_NAME, value = 'tr')
        num_materias = len(materias)-1
        # Extrae los datos de la tabla
        for i in range(num_materias):
            materia_Link = self.driver.find_element(by = By.XPATH, value = f'//*[@id="contentHolder"]/div[2]/table[2]/tbody/tr[{i+2}]/td[1]/a')
            materia_Link.click()
            materia = self.driver.find_element(by = By.XPATH, value = '//*[@id="contentHolder"]/div[2]/table[1]/tbody/tr[5]/td[2]')
            print('\n******************************')
            print('------------------------------')
            print(materia.text)
            print('------------------------------')
            notas_tabla = self.driver.find_element(by = By.XPATH, value = '//*[@id="contentHolder"]/div[2]/table[2]')
            notas = notas_tabla.find_elements(by = By.TAG_NAME, value = 'tr')
            num_filas = len(notas)-1
            for j in range(num_filas):
                titulo = self.driver.find_element(by = By.XPATH, value = f'//*[@id="contentHolder"]/div[2]/table[2]/tbody/tr[{j+2}]/td[1]')
                nota = self.driver.find_element(by = By.XPATH, value = f'//*[@id="contentHolder"]/div[2]/table[2]/tbody/tr[{j+2}]/td[3]')
                peso = self.driver.find_element(by = By.XPATH, value = f'//*[@id="contentHolder"]/div[2]/table[2]/tbody/tr[{j+2}]/td[5]')
                print(titulo.text)
                print(nota.text)
                print(peso.text + '%')
                print('-------')
            self.driver.back()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reports', report_name = 'ver-notas'))