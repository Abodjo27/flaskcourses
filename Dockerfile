# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8010 available to the world outside this container
EXPOSE EXPOSE 8010

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
