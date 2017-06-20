FROM andyxu9529/scrapy_docker

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app



RUN  pip3 install -r requirements.txt 
  

#RUN pip3 install -r requirements.txt

CMD python run.py



