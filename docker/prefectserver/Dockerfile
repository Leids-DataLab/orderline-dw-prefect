# Base image
FROM python:3.11-slim

# RUN apt-get update && \
#     apt-get install -y curl && \
#     rm -rf /var/lib/apt/lists/*

# Install prefect
# TODO versie kiezen
RUN pip install prefect

EXPOSE 4200

CMD ["prefect", "server", "start"]
