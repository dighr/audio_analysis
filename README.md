# Audio Transcription
## Set Up Guide : Django app with Postgres, Nginx, and Gunicorn on Ubuntu 18.04 DigitalOcean Droplet
This guide will demonstrate how to install and configure some components on Ubuntu 18.04 DigitalOcean VM to support and serve Django applications. A PostgreSQL database will be set up and the Gunicorn application server will be configured to interface with our applications. Then Nginx will be set up to reverse proxy to Gunicorn, giving us access to its security and performance features to serve our apps.

### Prerequisites and Goals
In order to complete this guide, you should have a fresh Ubuntu 18.04 server instance with a basic firewall and a non-root user with sudo privileges configured. You can learn how to set this up by running through our initial server setup guide.

We will be installing Django within a virtual environment. Installing Django into an environment specific to your project will allow your projects and their requirements to be handled separately.

Once we have our database and application up and running, we will install and configure the Gunicorn application server. This will serve as an interface to our application, translating client requests from HTTP to Python calls that our application can process. We will then set up Nginx in front of Gunicorn to take advantage of its high performance connection handling mechanisms and its easy-to-implement security features.

### Installing the Packages from the Ubuntu Repositories
To begin the process, we’ll download and install all of the items we need from the Ubuntu repositories. We will use the Python package manager ```pip``` to install additional components a bit later.

We need to update the local ```apt``` package index and then download and install the packages. The packages we install depend on which version of Python your project will use.

We are using Django with Python 3, type:

```
$ sudo apt update
$ sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl
```
This will install pip, the Python development files needed to build Gunicorn later, the Postgres database system and the libraries needed to interact with it, and the Nginx web server.

### Creating the PostgreSQL Database and User
Now we will create a database and database user for our Django application.

Log into an interactive Postgres session by typing:
```
$ sudo -u postgres psql
```

You will be given a PostgreSQL prompt where we can set up our requirements.

First, create a database for your project:
```
postgres=# CREATE DATABASE myproject;
```

Next, create a database user for our project. Make sure to select a secure password:
```
postgres=# CREATE USER myprojectuser WITH PASSWORD 'password';
```

Afterwards, we’ll modify a few of the connection parameters for the user we just created. This will speed up database operations so that the correct values do not have to be queried and set each time a connection is established.

We are setting the default encoding to UTF-8, which Django expects. We are also setting the default transaction isolation scheme to “read committed”, which blocks reads from uncommitted transactions. Lastly, we are setting the timezone. By default, our Django projects will be set to use UTC. These are all recommendations from the Django project itself:
```
postgres=# ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
postgres=# ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
postgres=# ALTER ROLE myprojectuser SET timezone TO 'UTC';
```
Now, we can give our new user access to administer our new database:
```
postgres=# GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
```
Next, change the newly created target database owner to the new user:
```
postgres=# ALTER DATABASE myproject OWNER TO myprojectuser;
```
When you are finished, exit out of the PostgreSQL prompt by typing:
```
postgres=# \q
```

Postgres is now set up so that Django can connect to and manage its database information.

By default, Postgres uses an authentication scheme called “peer authentication” for local connections. This default authentication method need to be changed from ```peer``` to password-based authentication method ```md5```

Client authentication is controlled by a configuration file, which traditionally is named pg_hba.conf and is stored in the database cluster's data directory. Open the pg_hba.conf file with ```sudo``` privileges:
```
$ sudo vim /etc/postgresql/10/main/pg_hba.conf
```
Find:
```
# Database administrative login by Unix domain socket
local   all             postgres                                peer

# TYPE  DATABASE        USER            ADDRESS                 METHOD

# "local" is for Unix domain socket connections only
local   all             all                                     peer
```
Change each ```peer``` to ```trust```

After updating ```pg_hba.conf```, the server needs the config needs to be reloaded. The easiest way to do this is by restarting the postgres service:
```
$ sudo service postgresql restart
```

### Creating a Python Virtual Environment 
Now that we have our database, we can begin getting the rest of our project requirements ready. We will be installing our Python requirements within a virtual environment for easier management.

To do this, we first need access to the virtualenv command. We can install this with pip.

As we are using Python 3, upgrade pip and install the package by typing:
```
$ sudo -H pip3 install --upgrade pip
$ sudo -H pip3 install virtualenv
```

With virtualenv installed, we can start forming our project. Create and move into a directory where we can keep our project files:
```
$ mkdir ~/myprojectdir
$ cd ~/myprojectdir
```

Within the project directory, create a Python virtual environment by typing:
```
$ virtualenv -p python3 myprojectenv
```

This will create a directory called myprojectenv within your myprojectdir directory. Inside, it will install a local version of Python and a local version of pip. We can use this to install and configure an isolated Python environment for our project.

Before we install our project’s Python requirements, we need to activate the virtual environment. You can do that by typing:
```
$ source myprojectenv/bin/activate
```
Your prompt should change to indicate that you are now operating within a Python virtual environment. It will look something like this: 
```
(myprojectenv) $ user@host:~/myprojectdir$.
```


## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

* https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04
