
# IPL Project Using Django

This project is more of a data project, data visualization. The main aim
of the project is to convert the raw open data plots, that tells a story
on the IPL matches. We are going to use Django framework for backend which
will handle all the data tables which is called as `models` and we are going
to use Django's `QuerySet API` for extracting the data and with the help of
`views` and `templates` we are going to render the graph. We have used
html/css/JS for writing templates and with the integration of [highcharts](https://www.highcharts.com/)
we are displaying graph on browser.

## Dataset

raw data which is .csv file, it's the real world data of IPL matches.
below is the link you can download the data from there.

Two dataset has been used for this project:

| Dataset | Link |
| --- | --- |
| IPL Data | https://www.kaggle.com/manasgarg/ipl |


## Run Locally

Clone the project

```bash
  ~ git clone git@gitlab.com:mountblue/cohort-17-python/vivek-dubey/ipl-project-django.git
```

Go to the project directory

```bash
  ~ cd ipl-project-django
```

After Downloading the dataset include it in the django project structure
near `manage.py`

Install dependencies

```bash
  ~ pip3 install -r requirements.txt
```

create the datbase in postgresql and change the credentials in your
django-project's `settings.py` file.

```bash
  DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': '<your_database_name>',
       'USER': '<your_username>',
       'PASSWORD': '<your password>',
       'HOST': '',
       'PORT': '',
   }
}
```

After this run following 2 commands to work with your database.

```bash
~ python3 manage.py makemigrations
~ python3 manage.py migrate
```

Now, you are ready to work with your database. But first we need to
import the csv dataset into our models for that run the below custom command.

```bash
~ python3 manage.py load_matches
~ python3 manage.py load_deliveries
```

Now, all the setups are completed start the server

```bash
~ python3 manage.py runserver
```

If you want to access admin page, you need to be a superuser for that
create one

```bash
~ python3 manage.py createsuperuser
```


## Authors

- [@Vivek Dubey](https://www.github.com/VivekCR7)

  

