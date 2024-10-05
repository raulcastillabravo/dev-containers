# Get the python image
FROM python:3.12-bullseye

# Switch to app directory
WORKDIR /src/api/

# Copy the requirements in to the app
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything else
COPY . .

#Run the python script
CMD flask run -h 0.0.0.0 -p 5000