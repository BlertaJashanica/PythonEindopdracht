import os
import platform
import socket
import psutil

class Module:
    def __init__(self):
        pass

    def run():
        pass
    def log():
        pass

class InfoModule(Module):
    def __init__(self):
        super().__init__()

    def run(self):
        data = {}
        hostname = socket.gethostname()
        data["Hostname"] = hostname

        ip_address = socket.gethostbyname(hostname)
        data["IP Address"] = ip_address

        data["Operating System"] = platform.system()

        username = os.getlogin()
        data["Username"] = username

        home_dir = os.path.expanduser("~")
        data["Home Directory"] = home_dir

        cpu_count = psutil.cpu_count(logical=True)
        data["CPU Count"] = cpu_count

        memory = psutil.virtual_memory()
        data["Total Memory"] = memory.total
        data["Available Memory"] = memory.available

        disk = psutil.disk_usage('/')
        data["Total Disk Space"] = disk.total
        data["Used Disk Space"] = disk.used

        data["Processor Architecture"] = platform.machine()
        data["Network Name"] = platform.node()
        data["Processor"] = platform.processor()

        return data



    def log(self, data ):
        output = ""
        for key, value in data.items():
           output += str(key) + ": " + str(value) + "\n"
        return output




