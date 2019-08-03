# cloudcenter_deploy
This scipt will deploy a Cisco Cloud Center Application Profile with your choice of name.  

###Script Information
* Run without and arguments for help information and options.
* Scipt must be updated to run on your system.

###How to use

* Edit the cloudcenter_deploy.py file so that the proper commectivity information is updated for your environment.
* Download the "restful.json" file from the Cloud Center deployment screen when you define an application profile deployment.  See screenshots below.
* Execute the script including the .json filename and the new deployment name.

```
./cloudcenter_deploy restful.json my_deployment_name
```

###Example Run and Result
```
bash-4.3# ./cloudcenter_deploy.py restful.json my_app

Deployment Name: my_app
URL to deployment information (raw): https://172.22.4.62:63669/cloudcenter-ccm-backend/api/v2/jobs/298

bash-4.3# 
```

---
###Show the JSON:
![alt text][showjson]
---
###Download the JSON:
![alt text][downloadjson]


[showjson]: show_json.png "Show the json"
[downloadjson]: download_json.png "Download the json"