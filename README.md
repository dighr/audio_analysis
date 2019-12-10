# Audio Transcription
## Set Up Guide : Django app with Postgres, Nginx, and Gunicorn on Ubuntu 18.04 DigitalOcean Droplet
This guide will demonstrate how to install and configure some components on Ubuntu 18.04 DigitalOcean VM to support and serve Django applications. A PostgreSQL database will be set up and the Gunicorn application server will be configured to interface with our applications. Then Nginx will be set up to reverse proxy to Gunicorn, giving us access to its security and performance features to serve our apps.

### Prerequisites and Goals
In order to complete this guide, you should have a fresh Ubuntu 18.04 server instance with a basic firewall and a non-root user with sudo privileges configured. You can learn how to set this up by running through our initial server setup guide.

We will be installing Django within a virtual environment. Installing Django into an environment specific to your project will allow your projects and their requirements to be handled separately.

Once we have our database and application up and running, we will install and configure the Gunicorn application server. This will serve as an interface to our application, translating client requests from HTTP to Python calls that our application can process. We will then set up Nginx in front of Gunicorn to take advantage of its high performance connection handling mechanisms and its easy-to-implement security features.

### Installing the Packages from the Ubuntu Repositories
To begin the process, we’ll download and install all of the items we need from the Ubuntu repositories. We will use the Python package manager `pip` to install additional components a bit later.

We need to update the local `apt` package index and then download and install the packages. The packages we install depend on which version of Python your project will use.

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
Change each `peer` to `trust`

After updating `pg_hba.conf`, the server needs the config needs to be reloaded. The easiest way to do this is by restarting the postgres service:
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
## Creating systemd Socket and Service Files for Gunicorn
Start by creating and opening a systemd socket file for Gunicorn with `sudo` privileges:
```
$ sudo nano /etc/systemd/system/gunicorn.socket
```
Inside, we will create a `[Unit]` section to describe the socket, a `[Socket]` section to define the socket location, and an `[Install]` section to make sure the socket is created at the right time:

```
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```

Save and close the file. 

Next, create and open a systemd service file for Gunicorn with `sudo` privileges in your text editor. The service filename should match the socket filename with the exception of the extension:
```
$ sudo nano /etc/systemd/system/gunicorn.service
```
Add the following: Remember to replace the **bolded** sections with the names created by the user.


<pre><code>
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=<b>username</b>
Group=www-data
WorkingDirectory=/home/<b>username</b>/<b>myprojectdir</b>
ExecStart=/home/<b>username</b>/<b>myprojectdir</b>/<b>myprojectenv</b>/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          <b>myproject</b>.wsgi:application

[Install]
WantedBy=multi-user.target
</code></pre>

Save and close the file.

We can now start and enable the Gunicorn socket. This will create the socket file at `/run/gunicorn.sock` now and at boot. When a connection is made to that socket, systemd will automatically start the `gunicorn.service` to handle it:
```
$ sudo systemctl start gunicorn.socket
$ sudo systemctl enable gunicorn.socket
```
We can confirm that the operation was successful by checking for the socket file.

## Checking for the Gunicorn Socket File
Check the status of the process to find out whether it was able to start:
```
$ sudo systemctl status gunicorn.socket
```
Next, check for the existence of the `gunicorn.sock` file within the `/run` directory:
```
$ file /run/gunicorn.sock
```
> Output
```
/run/gunicorn.sock: socket
```

## Testing Socket Activation
Currently, if you’ve only started the `gunicorn.socket` unit, the `gunicorn.service` will not be active yet since the socket has not yet received any connections. You can check this by typing:
```
sudo systemctl status gunicorn
```
> Output
```
● gunicorn.service - gunicorn daemon
   Loaded: loaded (/etc/systemd/system/gunicorn.service; disabled; vendor preset: enabled)
   Active: inactive (dead)
```
To test the socket activation mechanism, we can send a connection to the socket through `curl` by typing:
```
curl --unix-socket /run/gunicorn.sock localhost
```
You should see the HTML output from your application in the terminal. This indicates that Gunicorn was started and was able to serve your Django application. You can verify that the Gunicorn service is running by typing:
```
$ sudo systemctl status gunicorn
```
> Output
```
● gunicorn.service - gunicorn daemon
   Loaded: loaded (/etc/systemd/system/gunicorn.service; disabled; vendor preset: enabled)
   Active: active (running) since Mon 2019-12-09 20:00:40 UTC; 4s ago
 Main PID: 1157 (gunicorn)
    Tasks: 4 (limit: 1153)
   CGroup: /system.slice/gunicorn.service
           ├─1157 /home/<username>/myprojectdir/myprojectenv/bin/python3 /home/<username>/myprojectdir/myprojectenv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/run/gunicorn.sock myproject.wsgi:application
           ├─1178 /home/<username>/myprojectdir/myprojectenv/bin/python3 /home/<username>/myprojectdir/myprojectenv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/run/gunicorn.sock myproject.wsgi:application
           ├─1180 /home/<username>/myprojectdir/myprojectenv/bin/python3 /home/<username>/myprojectdir/myprojectenv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/run/gunicorn.sock myproject.wsgi:application
           └─1181 /home/<username>/myprojectdir/myprojectenv/bin/python3 /home/<username>/myprojectdir/myprojectenv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/run/gunicorn.sock myproject.wsgi:application

Jul 09 20:00:40 django1 systemd[1]: Started gunicorn daemon.
Jul 09 20:00:40 django1 gunicorn[1157]: [2019-12-09 20:00:40 +0000] [1157] [INFO] Starting gunicorn 19.9.0
Jul 09 20:00:40 django1 gunicorn[1157]: [2019-12-09 20:00:40 +0000] [1157] [INFO] Listening at: unix:/run/gunicorn.sock (1157)
Jul 09 20:00:40 django1 gunicorn[1157]: [2019-12-09 20:00:40 +0000] [1157] [INFO] Using worker: sync
Jul 09 20:00:40 django1 gunicorn[1157]: [2019-12-09 20:00:40 +0000] [1178] [INFO] Booting worker with pid: 1178
Jul 09 20:00:40 django1 gunicorn[1157]: [2019-12-09 20:00:40 +0000] [1180] [INFO] Booting worker with pid: 1180
Jul 09 20:00:40 django1 gunicorn[1157]: [2019-12-09 20:00:40 +0000] [1181] [INFO] Booting worker with pid: 1181
Jul 09 20:00:41 django1 gunicorn[1157]:  - - [09/Dec/2019:20:00:41 +0000] "GET / HTTP/1.1" 200 16348 "-" "curl/7.58.0"
```
If the output from `curl` or the output of `systemctl status` indicates that a problem occurred, check the logs for additional details:
```
$ sudo journalctl -u gunicorn
```
Check your `/etc/systemd/system/gunicorn.service` file for problems. If you make changes to the `/etc/systemd/system/gunicorn.service` file, reload the daemon to reread the service definition and restart the Gunicorn process by typing:
```
$ sudo systemctl daemon-reload
$ sudo systemctl restart gunicorn
```
Make sure you troubleshoot the above issues before continuing.

## Configure Nginx to Proxy Pass to Gunicorn
Now that Gunicorn is set up, we need to configure Nginx to pass traffic to the process.

Start by creating and opening a new server block in Nginx’s sites-available directory:
```
$ sudo nano /etc/nginx/sites-available/myproject
```
Add following into the file (Replace **username** with the current system user):
<pre><code>
server {
    listen 80;
    server_name server_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/<b>username</b>/myprojectdir;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
</code></pre>
Save and close the file when you are finished. Now, we can enable the file by linking it to the sites-enabled directory:
```
$ sudo ln -s /etc/nginx/sites-available/myproject /etc/nginx/sites-enabled
```
Usually you will find a default symlink file in the `/etc/nginx/sites-enabled` linked to `/etc/nginx/sites-available/default`. Existance of this file can be checked by listing the files inside `/etc/nginx/sites-enabled` directory:
```
$ ls -l /etc/nginx/sites-enabled
```
If you find the output contains:
```
default -> /etc/nginx/sites-available/default
```
Then Remove this link:
```
$ sudo rm /etc/nginx/sites-enabled/default
```
Test your Nginx configuration for syntax errors by typing:
```
$ sudo nginx -t
```
If no errors are reported, go ahead and restart Nginx by typing:
```
$ sudo systemctl restart nginx
```
Finally, we need to open up our firewall to normal traffic on port 80. Since we no longer need access to the development server, we can remove the rule to open port 8000 as well:
```
$ sudo ufw delete allow 8000
$ sudo ufw allow 'Nginx Full'
```
You should now be able to go to your server’s domain or IP address to view your application.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

* https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-18-04
