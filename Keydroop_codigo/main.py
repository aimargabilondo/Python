import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

def generar_combinacion():
    caracteres = string.ascii_uppercase + string.digits
    bloques = [''.join(random.choices(caracteres, k=4)) for _ in range(4)]
    return '-'.join(bloques)

def ingresar_combinaciones(url, campo_selector, intervalo=2):
    # Configurar el servicio del driver de Chrome
    servicio = Service(r'C:\Users\aimar\OneDrive\Escritorio\chromedriver-win64\chromedriver.exe')  # Asegúrate de usar la ruta correcta
    driver = webdriver.Chrome(service=servicio)
    
    try:
        # Abrir la página web
        driver.get(url)
        time.sleep(5)  # Esperar a que cargue la página
        
        while True:
            # Generar una combinación
            combinacion = generar_combinacion()
            print(f"Ingresando combinación: {combinacion}")
            
            try:
                # Buscar el campo de texto
                campo = driver.find_element(By.CSS_SELECTOR, campo_selector)
                campo.clear()
                campo.send_keys(combinacion)
                campo.send_keys(Keys.RETURN)  # Simular Enter
                
                # Esperar antes de generar la siguiente combinación
                time.sleep(intervalo)
            except Exception as e:
                print(f"Error al ingresar combinación: {e}")
                break
    except Exception as e:
        print("Error:", e)
    finally:
        # Cerrar el navegador
        driver.quit()

# Configuración: URL de la página y selector del campo de texto
url = "https://key-drop.com/es/#/payment/giftcards?amount=25"
campo_selector = "input[name='gift_card_code']"  # Ajusta esto según el campo real
intervalo_segundos = 5  # Tiempo entre cada intento

# Ejecutar el script
ingresar_combinaciones(url, campo_selector, intervalo_segundos)
