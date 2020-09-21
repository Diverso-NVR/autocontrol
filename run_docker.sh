docker stop nvr_autocontrol
docker rm nvr_autocontrol
docker build -t nvr_autocontrol .
docker run -d \
 -it \
 --restart on-failure \
 --name nvr_autocontrol \
 --net=host \
 --env-file ../.env_nvr \
 nvr_autocontrol