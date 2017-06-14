FROM python:3.6.1-alpine3.6

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app



RUN apk add -U tzdata
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

RUN echo "Asia/Shanghai" > /etc/timezone

RUN date

RUN apk add --no-cache python-dev gcc musl-dev openssl-dev libxml2-dev libxslt-dev libffi-dev libxml2 libxslt  \
    && pip3 install -r requirements.txt 
  

#RUN pip3 install -r requirements.txt

CMD python run.py



