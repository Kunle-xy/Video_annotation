# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variables that FastAPI needs (optional)
ENV MODULE_NAME=main
ENV VARIABLE_NAME=app

# Run the command to start FastAPI when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]