# Spark


## Installing Docker on Unix


To install Docker on any of the most popular Linux operating systems (Ubuntu, Debian, CentOs, fedora etc) you should run the following command with sudo privileges:
```
curl -sSL https://get.docker.com/ | sh
```

Then optionally you can add your user account to the docker group:
```usermod -aG docker $USER```

This allows you to deploy containers without sudo but we don’t recommend doing this on CentOS for security reasons.

## Checking the installation

Now run the test container to check the installation successful:

```docker run hello-world```

You can see some Docker deployment logs on the screen and then “Hello from Docker!” message from successfully deployed container.

## Setting up Spark and PySpark

To set up a Spark cluster issue the following command:
```$ docker build -t pyspark```
This command will automatically download, install, and configure Spark, Python, and Jupyter notebook in an isolated environment. To start Spark and a Jupyter notebook
session, you can execute the following command:
```bash
docker run -it --rm -v YYYYYY:/home/jovyan/dir_on_host -p 8888:8888 -p 4040:4040 bigdatateam/spark-course1
```

```-it``` allows to see the information from the container

```--rm``` means that the container will be deleted after exiting/terminating

```-v``` means that the files from the Jupyter of the container will be transferred to the local file system directory YYYYYY

YYYYYY - a local path, for example, for Linux``` $(pwd)/bigdata```, $(pwd) - the path to the current directory

(--rm and -v YYYYYY:/home/jovyan/dir_on_host can be safely removed if it is not needed.)

```-p 8888:8888``` allows to connect to the Jupyter of the container on 127.0.0.1:XXXX or localhost:XXXX, XXXX - a port number of the local system

```-p 4040:4040``` allows to connect to the Spark web UI of the container on 127.0.0.1:AAAA or localhost:AAAA, AAAA - a port number of the local system (if you do not need this UI, delete this option)


After issuing the command, you can open a browser to
```http://127.0.0.1:8888``` to access the Jupyter notebook session.

## Checking the initialization
You can test the correct initialization of Spark by creating a new notebook and executing the following content
inside a cell:
```python
import pyspark
sc = pyspark.SparkContext('local[*]')
rdd = sc.parallelize(range(1000))
rdd.first()

# Result:
# 0
```
This will initialize a SparkContext and take the first element in a collection.
Once the SparkContext is initialized, we can also head over to ```http://127.0.0.1:4040/jobs/```to open the Spark Web UI.
