Setup .env file from the sample.env and modify it:

```
cp sample.env .env
```


Load the environment variables into your current shell:

```
chmod +x export_envs.sh
source ./export_envs.sh /path/to/.env
```

Create the docker network:
```
# Use the bridge driver for local development with the dns proxy.
docker network create -d bridge tomudo 

# Use the overlay driver for remote deployment and potentially multiple swarm nodes.
docker network create -d overlay tomudo
```

Start the environment:

```
docker-compose up
```

The deploy part is not finished and does not work yet.
Deploy:

```
docker swarm init --advertise-addr MANAGER_NODE_IP
docker-compose -f docker-compose.yml -f docker-compose.prod.yml --env-file .env.prod build
docker stack deploy -c docker-compose.yml -c docker-compose.prod.yml <STACK_NAME>
```
