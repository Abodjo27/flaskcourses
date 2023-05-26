FROM python:3.11

# Copiez les fichiers de l'application
COPY . /app
WORKDIR /app

# Installez les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Commande d'exécution de l'application
CMD ["python", "app.py"]
