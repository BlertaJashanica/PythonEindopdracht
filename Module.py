import os
import platform
import socket
import psutil

class Module:
    def __init__(self):
        pass

    def getInfo():
        pass

class NetworkInfoModule(Module):
    def __init__(self):
        super().__init__()

    def getInfo():
        # Get the hostname of the computer
        hostname = socket.gethostname()
        print("Hostname:", hostname)

        # Get the IP address of the computer
        ip_address = socket.gethostbyname(hostname)
        print('IP Address:', ip_address)

class HardwareInfoModule(Module):
    def __init__(self):
        super().__init__()
    
    def getInfo():
        # Get the number of logical CPUs
        cpu_count = psutil.cpu_count(logical=True)
        print('CPU Count:', cpu_count)

        # Get memory usage statistics
        memory = psutil.virtual_memory()
        print('Total Memory:', memory.total)
        print('Available Memory:', memory.available)

        # Get disk usage statistics
        disk = psutil.disk_usage('/')
        print('Total Disk Space:', disk.total)
        print('Used Disk Space:', disk.used)

class ComputerInfoModule(Module):
    def __init__(self):
        super().__init__()

    def getInfo():

        # Get the computer's operating system
        print('Operating System:', platform.system())

        # Get the computer's processor architecture
        print('Processor Architecture:', platform.machine())

        # Get the computer's network name
        print('Network Name:', platform.node())

        # Get the computer's processor name
        print("Processor:", platform.processor())


class UserInfoModule(Module):
    def __init__(self):
        super().__init__()

    def getInfo():
        username = os.getlogin()
        print("Username:", username)

        # Get the home directory of the current user
        home_dir = os.path.expanduser("~")
        print('Home Directory:', home_dir)

user1 = UserInfoModule
user1.getInfo()

computer1 = ComputerInfoModule
computer1.getInfo()

hardware1 = HardwareInfoModule
hardware1.getInfo()

network1 = NetworkInfoModule
network1.getInfo()
