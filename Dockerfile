## Production image
FROM python:3.8-bullseye as app
# Install the function's dependencies using file requirements.txt
# from your project folder.
COPY requirements.txt  .
RUN pip install -r requirements.txt

# Copy function code
COPY app /opt/app
WORKDIR /opt/app
# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
ENTRYPOINT [ "python", "app.py"]