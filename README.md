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


