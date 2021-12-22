import os
import sys

# Almacenamos una nombre que estamos reemplazando en una variable de python:
project_slug = "{{ cookiecutter.project_slug }}"

# Asignamos colores a la terminal cuando ocurra algo
ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

# Ahora armamos una lógica básica donde prohibimos que nuestro proyecto inicie con
# la letra "x".
if project_slug.startswith("x"):
    print(f"{ERROR_COLOR}ERROR: {project_slug=} is not a valid name for this template.{RESET_ALL}")

    sys.exit(1)

print(f"{MESSAGE_COLOR}Let's do it! You're are going to create something awesome!")
print(f"Creating project at { os.getcwd() }{RESET_ALL}")
