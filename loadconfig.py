import configparser
import re
import os
import requests
import json

gh = configparser.ConfigParser()
gh.read(".\\config\\config.ini")
sh = gh.get("HP", "host")

gp = configparser.ConfigParser()
gp.read(".\\config\\config.ini")
sp = gp.get("HP", "port")

ga = configparser.ConfigParser()
ga.read(".\\config\\config.ini")
sa = ga.get("HP", "authkey")

gs = configparser.ConfigParser()
gs.read(".\\config\\config.ini")
sk = gs.get("HP", "sessionkey")

gs = configparser.ConfigParser()
gs.read(".\\config\\config.ini")
sg = str(gs.get("HP", "group"))

gq = configparser.ConfigParser()
gq.read(".\\config\\config.ini")
sq = gq.get("HP", "qq")

shh = configparser.ConfigParser()
shh.read(".\\config\\config.ini")
seth = shh.get("MCSM", "http")

skk = configparser.ConfigParser()
skk.read(".\\config\\config.ini")
setk = skk.get("MCSM", "key")

srn = configparser.ConfigParser()
srn.read(".\\config\\config.ini")
sets = srn.get("MCSM", "server")

roowner = configparser.ConfigParser()
roowner.read(".\\config\\config.ini")
robotowner = roowner.get("HP", "owner")

nowversion = configparser.ConfigParser()
nowversion.read(".\\config\\config.ini")
appversion = nowversion.get("Other", "version")

tfcheck = configparser.ConfigParser()
tfcheck.read(".\\config\\config.ini")
tfcheckupdate = tfcheck.get("Other", "autocheckupdate")
