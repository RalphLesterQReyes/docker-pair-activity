# 1. Use a slim Python image to save space and RAM
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy only the requirements first (Efficient Layering)
COPY requirements.txt .

# 4. Install the libraries (Pandas, Seaborn, Matplotlib)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy your script and the supermarket data into the container
COPY analytics.py .
COPY dataset.csv .

# 6. Create an output folder inside the container for the graphs
RUN mkdir output

# 7. Run the script when the container starts
CMD ["python", "analytics.py"]