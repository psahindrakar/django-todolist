# django-todolist
A simple project to learn django framework. This project should cover all the basics for creating REST api server using Python Django.

The project is configured using docker. There is an excellent blog and source code available [here](Configuring Nginx + Gunicorn :
https://realpython.com/blog/python/django-development-with-docker-compose-and-machine/)

# Build image for the project
docker-compose build
# Run the following command to create migrations for database
docker-compose run web /usr/local/bin/python manage.py makemigrations
# Run the following command to execute migration
docker-compose run web /usr/local/bin/python manage.py migrate
# Start the assembly of dockers defined in docker-compose.yml
docker-compose up -d
# Stop the assembly of dockers started by docker-compose up
docker-compose down

