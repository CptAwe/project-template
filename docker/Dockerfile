FROM python:3.14

WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy required files
COPY src /app/src

ENTRYPOINT [ "python" ]
CMD [ "/app/src/main.py" ]
