#!/usr/bin/env python

# Call the Cloud Center API and deploy a saved .json file.

# Import Python Packages
import sys
import requests
import os
import json
import urllib3

# Import settings file
import settings

# If you don't have a real SSL cert, let's disable the warnings.  If you have a real cert, comment this out.
urllib3.disable_warnings()

# Import the configuration
config = settings.Settings()

# If required settings are missing, raise an error
if not all([config.c3_user, config.c3_apikey, config.c3_server, config.c3_port]):
    raise Exception('\n\nPlease setup your Cloud Center specifics first.\n')


def main(argv):

    bad_command = False

    if len(argv) < 2:
        bad_command = True

    if len(argv) == 2:
        if argv[1] == "show_services":
            show_services()
        elif argv[1] == "show_apps":
            argv.remove(argv[1])
            show_apps()
        else:
            bad_command = True

    if len(argv) == 3:
        myjsonfile = argv[1]
        deployment_name = argv[2]

        argv.remove(argv[0])
        argv.remove(deployment_name)
        jsonbody = readexternalfile(myjsonfile)
        body = updatedata(jsonbody, deployment_name)
        data_url = '{0}/jobs'.format(config.url_base_v2)
        response = open_url(data_url, "post", body)
        if type(response) is str:
            print("Error: {}".format(response))
            exit(1)
        else:
            show_info(response)

    if bad_command:
        print("\nUsage examples:")
        print("         {0} show_apps".format(argv[0]))
        print("         {0} show_services (json response)".format(argv[0]))
        print("         {0} <your_json_file>.json <new_deployment_name>".format(argv[0]))

        print("\nAvailable JSON files:")
        list = os.listdir(r"./")
        for i in list:
            if ".json" in i:
                print(i)
        print("\n")
        exit(1)


def readexternalfile(file):
    try:
        with open(file, 'r') as f:
            data = json.load(f)

    except IOError:
        print("Sorry, file not found: {0}".format(file))
        exit(1)

    return data


def updatedata(jsonbody, newdepname):
    if "name" in jsonbody:
        jsonbody["name"] = newdepname
    else:
        print("Bad file format, deployment name not found in file.")
        exit(1)
    return jsonbody


def show_info(response):
    new_response = parse_response(response["resource"], "get", body=None)
    print("\nDeployment Name: {}".format(new_response["name"]))
    print("URL to deployment information (raw): {}\n".format(response["resource"]))


def show_apps():
    data_url = '{0}/apps'.format(config.url_base_v2)
    apps_data = open_url(data_url, "get")
    col_width = 30

    if len(apps_data["appsV2Responses"]) > 1:
        print("\n\nApplication Profile Name      Description\n-------------------------------------------------------------------------------")
        for app in apps_data["appsV2Responses"]:
            print(app["appName"].ljust(col_width) +
                  app["appDesc"].ljust(col_width))

    else:
        print("No application profiles found.")


def show_services():
    data_url = '{0}/tenants/1/services'.format(config.url_base_v1)
    data = (open_url(data_url, "get"))
    col_width = 25

    if len(data["services"]) > 1:
        print("\n\nService Name             Description\n------------------------------------------------------------------------")
        for service in data["services"]:
            print(service["name"].ljust(col_width) + service["description"].ljust(col_width))

    else:
        print("No services found.")


def open_url(url, method, body=None):
    headers = {'Accept': 'application/json'}
    auth = (config.c3_user, config.c3_apikey)

    if method == "get":
        try:
            result = requests.get(url, headers=headers, verify=False, auth=auth)
        except Exception:
            error = "Application Server Failure: Not able to communicate with Server at {0} ".format(config.c3_server)
            return error
    elif method == "post":
        try:
            result = requests.post(url, json=body, headers=headers, verify=False, auth=auth)
        except Exception:
            error = "Application Server Failure: Not able to communicate with Server at {0} ".format(config.c3_server)
            return error

    elif method == "delete":
        try:
            result = requests.delete(url, json=body, headers=headers, verify=False, auth=auth)
        except Exception:
            error = "Application Server Failure: Not able to communicate with Server at {0} ".format(config.c3_server)
            return error

    else:
        return {"resource": "Invalid method: {}".format(method)}

    if (result.status_code == 401):
        return "Invalid credentials"

    elif (result.status_code == 200 or result.status_code == 201 or result.status_code == 202):
        decoded_json = json.loads(result.text)
        return decoded_json

    else:
        return {"resource": "Unknown error code: {0} - With this error text: {1}".format(
            result.status_code, result.text)}

    return


def parse_response(url, method, body=None):
    headers = {'Accept': 'application/json'}
    auth = (config.c3_user, config.c3_apikey)

    if method == "get":
        try:
            result = requests.get(url, headers=headers, verify=False,
                                  auth=auth)
        except Exception:
            error = "Application Server Failure: " \
                    "Not able to communicate with Server at {0}\n".format(
                        config.c3_server)
            return error

        if (result.status_code == 401):
            return "Invalid credentials"

        elif (result.status_code == 200 or
              result.status_code == 201 or
              result.status_code == 202):
            decoded_json = json.loads(result.text)
            return decoded_json

        else:
            return {"resource": "Unknown error code: {0} - "
                    "With this error text: {1}".format(
                        result.status_code, result.text)}

    else:
        return {"resource": "Invalid method: {}".format(method)}

    return


if __name__ == '__main__':
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        pass
