# Base image
FROM python:3.11-slim

# RUN apt-get update && \
#     apt-get install -y curl && \
#     rm -rf /var/lib/apt/lists/*

# Install prefect
RUN pip install prefect==2.16.0

EXPOSE 4200

CMD ["prefect", "server", "start"]
