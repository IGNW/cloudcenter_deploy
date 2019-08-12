[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/IGNW/cloudcenter_deploy)

# cloudcenter_deploy
This scipt will deploy a Cisco Cloud Center Application Profile with your choice of name.  

### Requirements
* Installed and working Cisco Cloud Center 5 environment
    * Script should work with Cloud Center 4 but was not tested
    * Would need to modify the ```c3_version``` parameter to 4 in order to do so
* Docker Desktop installed on your local computer

### Installation



### Script Information
* Run without any arguments for help information and options.
* Update the settings.yaml with the required information to login to your Cloud Center Suite
* Add any additional parameters into that file and they will override the defaults

### How to use
* Update the "settings.yaml" file with the API credentails
* Download the "restful.json" file from the Cloud Center deployment screen when you define an application profile deployment.  See screenshots below.
* Execute the script including the .json filename and the new deployment name.
```
./cloudcenter_deploy restful.json my_deployment_name
```

### How to build more than one application
* One restful.json file doesn't help much, so you will want several or many of them.  
* Change the name of the `restful.json` file to something related to the application.
* Examples:
	* apachecontainer-gcp.json
	* ubuntu16-dc1.json
	* myuniversity-aws.json 
* You can now run the script with these new names to build different applications in different locations.



### Example Run and Result
```
bash-4.3# ./cloudcenter_deploy.py restful.json my_app

Deployment Name: my_app
URL to deployment information (raw): https://172.22.4.62:63669/cloudcenter-ccm-backend/api/v2/jobs/298

bash-4.3# 
```

### Steps to download required JSON file
![alt text][getjson]

[getjson]: get_json.png "Get the required JSON file."


### Optional Install method - Build a docker container
We have provided a Dockerfile so that you can run this script in a container rather than natively on your server.

* Only do this once you have updated the `settings.yaml` file and downloaded the `restful.json` file to the root folder
* Build the container
```
docker build . -t cloudcenter_deploy
```
* If you update the "settings.yaml" or the "restful.json" file, you will need to rebuild the docker container using the above command.
* Run your Docker container 
```
docker run -it cloudcenter_deploy bash
```
* Follow the How to use instructions.


### More information
For details on how to obtain the API key refer to the Cisco Documentation on Cloud Center 5

[https://docs.cloudcenter.cisco.com/](https://docs.cloudcenter.cisco.com/)