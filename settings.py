import yaml


class Settings():
    def __init__(self):
        self.c3_version = 5
        self.c3_user = ""
        self.c3_apikey = ""
        self.c3_server = ""
        self.c3_port = ""
        self.url_base_v1 = ""
        self.url_base_v2 = ""
        self.data_url = None
        self.deployment_name = None
        self.disable_ssl_warnings = True

        try:
            with open("settings.yaml", "r") as f:
                settings_file = f.read()
            yaml_file = yaml.safe_load(settings_file)

            for k, v in yaml_file.items():
                setattr(self, k, v)

        except IOError:
            print('No settings file found, using the default values')

        self.set_url_base()

    def __repr__(self):
        return str(vars(self))

    def set_url_base(self):
        if self.c3_version == 4:
            self.url_base_v1 = 'https://{0}/v1'.format(self.c3_server)
            self.url_base_v2 = 'https://{0}/v2'.format(self.c3_server)
        elif self.c3_version == 5:
            self.url_base_v1 = 'https://{0}:{1}/cloudcenter-ccm-backend/api/v1'.format(
                self.c3_server, self.c3_port)
            self.url_base_v2 = 'https://{0}:{1}/cloudcenter-ccm-backend/api/v2'.format(
                self.c3_server, self.c3_port)
