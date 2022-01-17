import configparser

gh = configparser.ConfigParser()
gh.read(".\\config\\config.ini")

sh = gh.get("HP", "host")
sp = gh.get("HP", "port")
sg = str(gh.get("HP", "group"))
seth = gh.get("MCSM", "http")
setk = gh.get("MCSM", "key")
sets = gh.get("MCSM", "server")
robotowner = gh.get("HP", "owner")
appversion = gh.get("Other", "version")
tfcheckupdate = gh.get("Other", "autocheckupdate")
