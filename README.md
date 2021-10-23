# flask-redis-message-excersie

## Running with virtual env:

* create a new virtual environment.
* then activate it:
    * `source venv/bin/activate   `

* install required packages as described in requirements:
    * `pip install -r requirements.txt`
 
* set the FLASK_APP and FLASK_ENV variables:
    * `export FLASK_APP=words_app`
    * `export FLASK_ENV=development`
    * `export LOCAL_ENV_TYPE=VENV` 
 
* run flask:
    * `flask run`
    
##### Please note: 
Upon fresh git clone app install, the Redis python package was not installed correctly.   
This caused an redis import error while running flask.

I am not sure if this issue happened due to my local environment or not.  

I manage to solve this issue by uninstalling and reinstalling Redis, and by deactivating and reactivating the virtual env.   

## Running with Docker:

* `docker compose build`

* `docker compose run app`