from io import UnsupportedOperation
import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class HelloWorld(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
    
    def testSIGAA(self):
        # Variables de inicio de sesión y número de materias
        usuario = '000475627'
        contrasena = '8041235*'
        num_materias = 4
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
        notas_menu = self.driver.find_element(by = By.ID, value = 'contentItem23')
        notas_menu.click()
        enviar_btn = self.driver.find_element(by = By.ID, value = 'id____UID6')
        enviar_btn.click()
        # Extrae los datos de la tabla
        tabla = []
        for i in range(num_materias):
            materia = self.driver.find_element(by = By.XPATH, value = f'//*[@id="contentHolder"]/div[2]/table[2]/tbody/tr[{i+2}]/td[5]')
            nota = self.driver.find_element(by = By.XPATH, value = f'//*[@id="contentHolder"]/div[2]/table[2]/tbody/tr[{i+2}]/td[7]')
            tabla.append(materia.text)
            tabla.append(nota.text)
        print('\n******************************')
        print('------------------------------')
        for j in range(num_materias*2):
            print(tabla[j])
        print('------------------------------')
        print('******************************\n')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reports', report_name = 'ver-notasf'))