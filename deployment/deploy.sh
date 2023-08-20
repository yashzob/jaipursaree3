pip install -r .\requirements.txt
docker build -t saree:v12 .
docker tag saree:v12 ashishsng21/saree:v1
docker push ashishsng21/saree:v1

az login --use-device-code
az account set --subscription 012ba348-d3c5-43dd-b6d1-de7128528075
az group create --name saree-swatantra-rg --location eastus
cd ../deployment
az deployment group create --resource-group saree-swatantra-rg --template-file webapp.bicep
