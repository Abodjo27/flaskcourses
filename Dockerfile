# Use an official Python runtime as a parent image
FROM python:3.9

# Créer un nouvel utilisateur non privilégié
RUN adduser --disabled-password --gecos "" appuser

# Définir le répertoire de travail et les permissions appropriées
WORKDIR /app

RUN chown -R appuser:appuser /app

# Basculer vers l'utilisateur non privilégié
USER appuser

# Copier et installer les dépendances
COPY --chown=appuser:appuser requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source
COPY --chown=appuser:appuser assets /app/assets
COPY --chown=appuser:appuser templates /app/templates
COPY  app.py /app/app.py
COPY --chown=appuser:appuser data.json /app/data.json
COPY json_saver.py /app/json_saver.py
COPY --chown=appuser:appuser requirements.txt /app/requirements.txt

# Exposer le port 8010
EXPOSE 8010

# Exécuter l'application
CMD ["python", "app.py"]
