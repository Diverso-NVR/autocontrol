docker stop nvr_autocontrol
docker rm nvr_autocontrol
docker build -t nvr_autocontrol .
docker run -idt --name nvr_autocontrol --net=host --env-file .env nvr_autocontrol

