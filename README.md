# riak-test

Just checking out Riak.


## To start a 5 nodes cluster execute this inside the riak-container directory
```
docker-compose scale coordinator=1 member=4
```


## To see the logs
```
docker-compose logs
```


## Connect to a terminal inside the container
```
docker exec -it <containerId> /bin/bash
```


## To discover get the IP of the coordinator node
```
docker inspect -f '{{.NetworkSettings.IPAddress}}' riak-containercompose_coordinator_1
```
Note: clusterdockercompose_coordinator_1 = docker container name, the command works for any container by either id or name



## Check out the cluster status
```
docker exec <any_node_container_id/name> riak-admin cluster status
```


