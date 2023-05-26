FROM python:3.11

# Installation de pip
RUN python -m ensurepip --upgrade

# Copie des fichiers de votre application
COPY . /app

# Définition du répertoire de travail
WORKDIR /app

# Installation des dépendances avec pip
RUN pip install -r requirements.txt

# Commande pour démarrer votre application
CMD [ "python", "app.py" ]
