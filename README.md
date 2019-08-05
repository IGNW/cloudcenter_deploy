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
docker build . -t cloudcenter_container
```

* Build a container and run the commands 
```
docker run cloudcenter_container                                                    # Run the app with no settings
docker run cloudcenter_container cloudcenter_deploy                                 # Same command as above
docker run cloudcenter_container cloudcenter_deploy show_apps                       # Run the program with the show_apps flag
docker run cloudcenter_container cloudcenter_deploy restful.json mybuild_name       # Deploy a build into cloud center
```

### Example Run and Result
```
Administrators-MacBook-Pro-7:cloudcenter_deploy joej$ docker run cloudcenter_container cloudcenter_deploy restful.json mybuild_name

Deployment Name: mybuild_name
URL to deployment information (raw): https://172.22.4.62:63669/cloudcenter-ccm-backend/api/v2/jobs/320

Administrators-MacBook-Pro-7:cloudcenter_deploy joej$  
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