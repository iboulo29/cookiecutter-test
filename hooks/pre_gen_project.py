import sys
# Vérification de la version de Python
MIN_PYTHON = (3, 10)
if sys.version_info < MIN_PYTHON:
    print(f"Erreur : Python >= {MIN_PYTHON[0]}.{MIN_PYTHON[1]} est requis.")
    sys.exit(1)

project_slug = "{{ cookiecutter.project_slug }}"

# Vérification simple du slug
if " " in project_slug:
    print("Erreur : project_slug ne doit pas contenir d’espaces.")
    sys.exit(1)