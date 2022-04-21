# How to run this microservices on docker

Step1:docker-compose run web alembic upgrade head
Step2:docker-compose run web alembic revision --autogenerate -m "First migration"
Step3:docker-compose build  
Step4:docker-compose up




Url to check the Microservice via swagger UI based  is on   http://localhost:8000/docs



# Pgadmin4 for database

    http://localhost:5050

    Settings require:
     
    