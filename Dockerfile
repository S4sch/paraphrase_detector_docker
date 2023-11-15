# Use an official Python runtime as a parent image
FROM python:3.9.7-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME Project2

# Run main.py when the container launches
CMD ["python", "main.py", "--model_name", "best_model", "--checkpoint_dir", "models", "--lr", "8.368448763558096e-05", "--weight_decay", "0.00018104578993251926", "--adam_epsilon", "1e-8", "--scheduler_step_size", "5", "--scheduler_gamma", "0.9455187198162054"]