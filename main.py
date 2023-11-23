from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui as auto
import time
import getpass
import win32gui
import win32con

# Define o Console sempre no topo (most on top) e suas dimensões
hwnd = win32gui.GetForegroundWindow()
win32gui.SetWindowPos(hwnd,win32con.HWND_TOPMOST,100,100,550,300,0)

print('### - SCRIPT PARA SOLICITAR VALIDADE NO RUB - ###')
print('Desenvolvido pelo TI David (5353181)')
print()
print('- Login no RUB -')

# Credenciais RUB
IP = input('Digite o IP da sua loja, Exemplo = 10.48.69.146: ')
USER = input('Digite a sua matrícula: ')
PASSWORD = getpass.getpass('Digite sua senha: ')

DRIVER = webdriver.Chrome()
DRIVER.get(f'http://{IP}/vue/#/dashboard')
DRIVER.maximize_window()

def aguardar(segundos):
    time.sleep(segundos)


def LoginRub():
    USER_BOX = DRIVER.find_element(By.ID, 'login-fld-usr')
    USER_BOX.send_keys(USER)

    PASSWORD_BOX = DRIVER.find_element(By.ID, 'login-fld-pwd')
    PASSWORD_BOX.send_keys(PASSWORD)

    LOGIN_BUTTON = DRIVER.find_element(By.ID, 'login-vbtn-loginbtn')
    LOGIN_BUTTON.click()


def Solicitar_Validade():
    print('Pressione CTRL + C para fechar o programa.')
    i = 0
    produtos = DRIVER.find_elements(By.XPATH, '//td[@colindex="0"]')
    for produto in produtos:
            produtos = DRIVER.find_elements(By.XPATH, '//td[@colindex="0"]')
            produtos[i].click()
            i += 1
            solicitar_tarefa = DRIVER.find_element(By.XPATH, '//a[@id="painel_validade-solicitartarefa-solicitartarefa"]')
            solicitar_tarefa.click()

            solicitar_selecionado = DRIVER.find_element(By.XPATH, '//a[@id="painel_validade-act-ACT_GERAR_TAREFA_VALIDADE"]')
            solicitar_selecionado.click()
            aguardar(1.2)
            ok_button = DRIVER.find_element(By.XPATH, '//a[@id="main-vbtn-msgdef-ok-2"]')
            ok_button.click()
            aguardar(1.2)
            ok_button.click()

LoginRub()
print('Entre na página de uma das validades pendentes.')
Loop = True
while Loop:
    input('Pressione [Enter] para rodar o script: ')
    try:
        Solicitar_Validade()
    except:
        continue