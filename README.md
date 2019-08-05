# cloudcenter_deploy
This scipt will deploy a Cisco Cloud Center Application Profile with your choice of name.  

### Requirements
* Installed and working Cisco Cloud Center 5 environment
    * Script should work with Cloud Center 4 but was not tested
    * Would need to modify the ```c3_version``` parameter to 4 in order to do so
* Docker Desktop installed on your local computer


### Script Information
* Run without any arguments for help information and options.
* Update the settings.yaml with the required information
* Add any additional parameters into that file and they will override the defaults

### How to use
* Update the "settings.yaml" file with the API credentails
* Download the "restful.json" file from the Cloud Center deployment screen when you define an application profile deployment.  See screenshots below.
* Build the docker container using the command
    * If you update the "settings.yaml" or the "restful.json" file, you will need to rebuild the docker container.

```
docker build . -t cloudcenter_deploy
```

* Build a container and connect to it using the following command
```
docker run -it cloudcenter_deploy bash
```

* Execute the script including the .json filename and the new deployment name.
```
./cloudcenter_deploy restful.json my_deployment_name
```

### Example Run and Result
```
bash-4.3# ./cloudcenter_deploy.py restful.json my_app

Deployment Name: my_app
URL to deployment information (raw): https://172.22.4.62:63669/cloudcenter-ccm-backend/api/v2/jobs/298

bash-4.3# 
```

---
### Show the JSON:
![alt text][showjson]
---
### Download the JSON:
![alt text][downloadjson]


[showjson]: show_json.png "Show the json"
[downloadjson]: download_json.png "Download the json"

### More information
For details on how to obtain the API key refer to the Cisco Documentation on Cloud Center 5

https://docs.cloudcenter.cisco.com/