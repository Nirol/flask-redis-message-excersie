# using a python small basic image
FROM python:3.8

# creates a dir for our application
WORKDIR /app
# copy our requirements.txt file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
# copy the rest of our application
COPY . .


#  set the flask app name and the flask env:

ENV FLASK_APP=words_app
ENV FLASK_ENV=development


# exposing our app port in docker internal network
EXPOSE 5000
# run the application
CMD flask run -h 0.0.0.0