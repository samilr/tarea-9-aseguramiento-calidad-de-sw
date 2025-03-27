# Automatización de Pruebas con Selenium WebDriver

## 1. Selección del Proyecto o Sitio Web
Elegí el sitio web [SauceDemo](https://www.saucedemo.com) para realizar la prueba automatizada. Este sitio es adecuado para pruebas de automatización debido a su interfaz de usuario simple y diversos escenarios de prueba posibles, como inicio de sesión, agregar productos al carrito, y navegación.

## 2. Configuración del Entorno de Pruebas
Para configurar el entorno de pruebas, seguí estos pasos:
- Me aseguré de tener Selenium WebDriver instalado en mi entorno de desarrollo.
- Seleccioné Python como el lenguaje de programación para escribir las pruebas.
- Configuré el proyecto de automatización de pruebas creando un archivo `requirements.txt` con las siguientes dependencias:
  ```
  selenium
  unittest
  ```
- Instalé las dependencias ejecutando:
  ```bash
  pip install -r requirements.txt
  ```

## 3. Identificación de Escenarios de Pruebas
Los escenarios de pruebas que abordé son los siguientes:
- Inicio de sesión
- Agregar un producto al carrito
- Eliminar un producto del carrito
- Verificar detalles del producto
- Navegación al carrito
- Mensaje de error para usuario bloqueado
- Verificar precios de los productos
- Agregar múltiples productos al carrito

## 4. Diseño de Casos de Prueba
Cada escenario identificado tiene sus propios casos de prueba, detallados de la siguiente manera:
- **Inicio de sesión:**
  - Pasos: Ingresar usuario y contraseña, hacer clic en el botón de inicio de sesión.
  - Datos de entrada: `standard_user`, `secret_sauce`
  - Resultados esperados: Redirección a la página de inventario con el título "Swag Labs".
- **Agregar un producto al carrito:**
  - Pasos: Iniciar sesión, hacer clic en el botón "Add to cart" del producto.
  - Resultados esperados: El producto se añade al carrito, y el contador del carrito muestra "1".
- **Eliminar un producto del carrito:**
  - Pasos: Iniciar sesión, agregar producto al carrito, hacer clic en el botón "Remove".
  - Resultados esperados: El producto se elimina del carrito, y el contador del carrito está vacío.

## 5. Configuración de Selenium WebDriver
Inicialicé la instancia de WebDriver en mi código:
```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com")
```
Me aseguré de manejar adecuadamente la apertura y cierre del navegador:
```python
driver.quit()
```

## 6. Implementación de Pruebas
Traduje mis casos de prueba a código utilizando los métodos y funciones de Selenium WebDriver. Aquí tienes un ejemplo:
```python
from selenium.webdriver.common.by import By

def test_login():
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
```

## 7. Manejo de Esperas Explícitas e Implícitas
Utilicé esperas explícitas para garantizar que los elementos estén presentes antes de interactuar con ellos:
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
```
Consideré el uso de esperas implícitas según las necesidades de mi proyecto:
```python
driver.implicitly_wait(10)
```

## 8. Ejecución de Pruebas
Ejecuté mis pruebas en el entorno de desarrollo y verifiqué que se ejecuten sin errores:
```bash
python -m unittest tarea_9_seleniun_sg.py
```

## 9. Generación de Reportes
Implementé la generación de informes utilizando herramientas como TestNG, ExtentReports, o generación de informes nativa del marco de prueba que estoy utilizando.

## 10. Revisión y Mejora Continua
Revisé el código de las pruebas para garantizar buenas prácticas y eficiencia.

## Notas Importantes
- Me aseguré de que mis pruebas sean modulares y mantenibles.
- Utilicé buenas prácticas de programación y nomenclatura.

### Ejemplo de código de pruebas en Python
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestSauceDemo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com")

    def test_login(self):
        driver = self.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
        self.assertIn("Swag Labs", driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
```

![image](https://github.com/user-attachments/assets/5541636f-bbcc-4a50-a72d-9ee92ee77421)
