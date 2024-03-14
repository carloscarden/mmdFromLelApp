# Mi Aplicación Django

 Instrucciones para ejecutar los tests.

## Requisitos

- Python 3.8 o superior
- Django 3.2 o superior

## Instalación

Primero, clona el repositorio e instala las dependencias:

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
pip install -r requirements.txt
```

## Ejecución de los Tests

Para ejecutar todos los tests, puedes usar el siguiente comando:


```bash
python manage.py test miapp
```

Si quieres ejecutar un test específico, puedes especificar el nombre del test después del nombre de la aplicación. 

```bash
python manage.py test mmdFromLelApp.tests.TestPrueba
```

