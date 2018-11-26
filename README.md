# erecicla
python api

### Dependencies

```
sudo apt-get install libmysqlclient-dev
sudo apt-get install python3.6-dev
sudo apt install python3-pip
pip install mysql-connector-python
```

### Install

```
$ sudo apt-get install python3-venv python-pip
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements-dev.txt

export FLASK_ENV=development
export FLASK_APP=main.py
```

### Running server

```
$ python main.py
$ flask run
```

### Local Google SQL
```
 ./cloud_sql_proxy -instances="ereciclar"=tcp:3306
```


### Deploy

```
gcloud config set project ereciclar-223600
gcloud app deploy --verbosity=debug
```

### References

[Google SQL](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/appengine/flexible/cloudsql/)
[Flexible Python Runtime](https://cloud.google.com/appengine/docs/flexible/python/runtime)
