======
Browserstack Automate
======

Browserstack Automate integrates Browserstack and Behave to allow developers to automate their selinium tests across any number of devices. Simply define your Behave tests and the devices you wish to test against. The tests will be sent to Browserstack and return runner reports, screenshots and any errors reports.    


Flask starter project...

[![Build Status](https://travis-ci.org/realpython/flask-skeleton.svg?branch=master)](https://travis-ci.org/realpython/flask-skeleton)

## Quick Start

### Basics

1. Activate a virtualenv
1. Install the requirements

### Set Environment Variables

Update *project/server/config.py*, to either:

```sh
app_settings = 'project.server.config.DevelopmentConfig'
```

or

```sh
app_settings = 'project.server.config.ProductionConfig'
```

### install 

```sh
$ python manage.py install

```

### Run the Application

```sh
$ python manage.py runserver
```

So access the application at the address [http://localhost:5000/](http://localhost:5000/)

> Want to specify a different port?

> ```sh
> $ python manage.py runserver -h 0.0.0.0 -p 8080
> ```

### Testing

Without coverage:

```sh
$ python manage.py test
```
