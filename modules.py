import os
import platform
import socket
import psutil

class Module:
    def __init__(self):
        data = {}

    def run():
        pass
    def log():
        pass

class InfoModule(Module):
    def __init__(self):
        super().__init__()

    def run(self):
    
        hostname = socket.gethostname()
        self.data["Hostname"] = hostname

        ip_address = socket.gethostbyname(hostname)
        self.data["IP Address"] = ip_address

        self.data["Operating System"] = platform.system()

        username = os.getlogin()
        self.data["Username"] = username

        home_dir = os.path.expanduser("~")
        self.data["Home Directory"] = home_dir

        cpu_count = psutil.cpu_count(logical=True)
        self.data["CPU Count"] = cpu_count

        memory = psutil.virtual_memory()
        self.data["Total Memory"] = memory.total
        self.data["Available Memory"] = memory.available

        disk = psutil.disk_usage('/')
        self.data["Total Disk Space"] = disk.total
        self.data["Used Disk Space"] = disk.used

        self.data["Processor Architecture"] = platform.machine()
        self.data["Network Name"] = platform.node()
        self.data["Processor"] = platform.processor()



    def log(self):
        for key, value in self.data.items():
            print(key + ":", value)





