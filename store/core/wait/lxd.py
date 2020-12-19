import pylxd
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class FrontyLxd:
    def __init__(self):
        self.client = pylxd.Client(endpoint='https://18.212.143.227:8443', cert=('lxd.crt', 'lxd.key'), verify=False)

        self.containers = self.client.containers

    def get_all_containers(self):
        print("______________________________________________", self.containers.all())
        return self.containers.all()

    def get_container(self, name):
        return self.containers.get(name)

    @staticmethod
    def start_container(container):
        container.start()

    @staticmethod
    def freeze_container(container):
        container.freeze()

    @staticmethod
    def delete_container(container):
        container.delete()

    @staticmethod
    def put_file(container, file_path):
        file_data = open(file_path).read()
        container.files.put(file_path, file_data)

    @staticmethod
    def create_file(container, file_path):
        new_file_data = container.files.get(file_path)
        open(file_path, 'wb').write(new_file_data)
