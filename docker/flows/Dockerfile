# Base image
FROM python:3.11-slim

# Workdir instellen
WORKDIR /app

# Dit heeft DBT nodig
RUN mkdir -p /root/.dbt

# Installeer programma's/drivers.
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    apt-transport-https \
    unixodbc \
    unixodbc-dev \
    gnupg2

# Voeg Microsoft's GPG sleutel toe
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

# Voeg de repository voor de ODBC driver toe
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list

# Installeer de ODBC Driver 17 voor SQL Server
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Verwijder tijdelijke bestanden uit de container
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Poetry
# TODO: eigenlijk moet dit met pipx
RUN pip install poetry

# Project bestanden kopieren
COPY . .

# Installeer met poetry
RUN poetry install

# Serveer de flow 'all' bij het opstarten van de container.
CMD ["poetry", "run", "prefect-flows", "--mode", "serve", "serveallflows"]
