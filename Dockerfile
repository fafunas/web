FROM python:3.12


ENV REDIS_URL=redis://redis PYTHONUNBUFFERED=1

WORKDIR /app
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

# Create directory for MongoDB data
RUN mkdir -p /data/db


# Expose ports
EXPOSE 8000 27017

ENTRYPOINT ["reflex", "run", "--env", "prod", "--backend-only", "--loglevel", "debug" ]