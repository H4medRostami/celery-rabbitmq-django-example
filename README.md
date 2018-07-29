# celery-rabbitmq-django-example

sum 2 digit and render celery functions

first you need to install rabbitmq-server then:

2.install requirements with:

    pip3 install requirements.txt
    

3.change dir 

    source mysite/bin/activate
    
    cd mysite
    
    
4.On terminal:

    celery -A mysite worker -l info
    
    manage.py runserver
  
  
  urls:
  host:port/delay
  host:port/get
  host:port/ready

