#LOAD THE CONFIG
import json

# Open the configuration file
with open('config.json') as f:
    # Load JSON data from file
    config = json.load(f)

# Accessing SC_DOMAIN
SITE = config["Siti"]
FT_DOMAIN = SITE["Filmpertutti"]['domain']
SC_DOMAIN = SITE["StreamingCommunity"]['domain']
TF_DOMAIN = SITE["Tantifilm"]['domain']
LC_DOMAIN = SITE["LordChannel"]['domain']
SW_DOMAIN = SITE["StreamingWatch"]['domain']
AW_DOMAIN = SITE['AnimeWorld']['domain']
SKY_DOMAIN = SITE['SkyStreaming']['domain']
CB_DOMAIN = SITE['CB01']['domain']
DDL_DOMAIN = SITE['DDLStream']['domain']
MYSTERIUS = SITE['Mysterius']['enabled']
DLHD = SITE['DaddyLiveHD']['enabled']
TF_ForwardProxy = SITE['Tantifilm']["TF_ForwardProxy"]
SC_ForwardProxy = SITE['StreamingCommunity']["SC_ForwardProxy"]
TF_PROXY = SITE['Tantifilm']["TF_PROXY"]
CB_PROXY = SITE['CB01']["CB_PROXY"]
ips4_device_key = SITE['DDLStream']['cookies']["ips4_device_key"]
ips4_IPSSessionFront = SITE['DDLStream']['cookies']["ips4_IPSSessionFront"]
ips4_member_id = SITE['DDLStream']['cookies']["ips4_member_id"]
ips4_login_key = SITE['DDLStream']['cookies']["ips4_login_key"]
#General
GENERAL = config['General']
dotenv = GENERAL["load_env"]
HOST = GENERAL["HOST"]
PORT = GENERAL["PORT"]
Icon = GENERAL["Icon"]
Name = GENERAL["Name"]
Public_Instance = GENERAL["Public_Instance"]
Global_Proxy =  GENERAL["Global_Proxy"]