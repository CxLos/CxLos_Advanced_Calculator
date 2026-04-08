
# Use the official Python image from the Python Docker Hub repository as the base image
FROM python:3.12-slim-bookworm

# Set environment variables to prevent Python from writing .pyc files and to ensure that output is sent directly to the terminal without buffering
ENV PYTHONDONTWRITEBYTECODE=1 \
   PYTHONUNBUFFERED=1

# Set the working directory to /app in the container
WORKDIR /app

# Update the package list, upgrade existing packages, and install necessary system dependencies for building Python packages and running the application
RUN apt-get update && \
   apt-get install -y --no-install-recommends gcc python3-dev libssl-dev && \
   rm -rf /var/lib/apt/lists/* && \
   python -m pip install --upgrade pip setuptools>=70.0.0 wheel && \
   groupadd -r appgroup && \
   useradd -r -g appgroup appuser

# Create a non-root user named 'myuser' with a home directory

# Copy the requirements.txt file to the container to install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application code into the container and set ownership to 'appuser' to ensure that the application runs with non-root privileges
COPY . .
RUN chown -R appuser:appgroup /app



# Copy the rest of the application's source code into the container, setting ownership to 'myuser'
# COPY --chown=myuser:myuser . .

# Switch to the 'myuser' user to run the application
# USER myuser
USER appuser

# Define a health check to monitor the application's health by sending a request to the /health endpoint every 30 seconds, with a timeout of 30 seconds and a start period of 5 seconds. If the health check fails, it will retry up to 3 times before marking the container as unhealthy.
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
   CMD curl -f http://localhost:8000/health || exit 1

   # Use the Python interpreter as the entrypoint and the script as the first argument
# This allows additional command-line arguments to be passed to the script via the docker run command
# ENTRYPOINT ["python", "main.py"]

# this sets a default argument, its also set in the program but this just illustrates how to use cmd and override it from the terminal

# CMD ["--url","http://github.com/cxlos"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]