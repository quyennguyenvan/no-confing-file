#action 1
# download the configuration from keyvault
wget -o config.json https://$1.vault.azure.net/secrets/config?api-version=2016-10-01
# build app 
docker run -f Dockerfile -t application:$tag .
# mount data to source
docker run -v $(pwd)/config.json:/app/config.json -t application:$tag