import yaml


class Config:
    __Instance = None

    @staticmethod
    def Instance():
        if Config.__Instance is None:
            Config.__Instance = Config()

        return Config.__Instance

    def __init__(self):
        with open("config.yaml") as stream:
            try:
                self._yaml = yaml.safe_load(stream)
            except yaml.YAMLError as err:
                print(err)
                exit(1)

    def get(self, key: str):
        return self._yaml[key]
