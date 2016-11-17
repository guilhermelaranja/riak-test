http://basho.com/posts/technical/running-riak-in-docker/

# riak-test

Just checking out Riak.

## Cluster stuff

### To start a 5 nodes cluster execute this inside the riak-container directory
```
riak-container$ docker-compose scale coordinator=1 member=4
```


### To see the logs
```
riak-container$ docker-compose logs
```


### Connect to a terminal inside the container
```
$ docker exec -it <containerId> /bin/bash
```


### To discover get the IP of the coordinator node
```
$ docker inspect -f '{{.NetworkSettings.IPAddress}}' riakcontainer_coordinator_1
```
Note: riakcontainer_coordinator_1 = docker container name, the command works for any container by either id or name. Also coordinator node was used just to show you can use container name, you could do this for any node.


### Every node will be listening in the port 8087 for Protocol Buffer and port 8098 for http, but to access the node from outside you need to get the ports those were mapped to in the host machine. To do that execute:
```
$ docker inspect -f 'localhost:{{(index (index .NetworkSettings.Ports "8087/tcp") 0).HostPort}}' <containerId>
```


### Check out the cluster status
```
docker exec <any_node_container_id/name> riak-admin cluster status
```


## API stuff - Python client


### Install the client
```
pip install riak
```


### Run the example code to write and fetch data from a node
```
docker inspect -f 'localhost {{(index (index .NetworkSettings.Ports "8087/tcp") 0).HostPort}}' riakcontainer_member_1 | xargs python simpleApiExample.py
```

