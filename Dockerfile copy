FROM python:3.9
# ENV PYTHONUNBUFFERED=1
# ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY ./requirement.txt .
COPY . .
RUN pip3 install --upgrade pip
RUN pip install -r requirement.txt
EXPOSE 8000
# ENV NAME env

# CMD [ "uvicorn","main:app","--host","0.0.0.0", "--port","80" ]

