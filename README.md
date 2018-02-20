
## Script migrate db version 0.10 to 0.11

Test with python3 but works with python2

Install pymongo

``` bash
pip3 install pymongo

//or

pip3 install -r requirements.txt
```

after, config host and db name

``` bash
URL = 'mongodb://localhost:27017/'
DBNAME = 'maestro'
```

``` bash
python3 migrate.oy
```