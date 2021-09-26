"""module for parsing project configuration"""
import configparser

_CONFIG_PATH = "config.ini"
_config = configparser.ConfigParser()
_config.read(_CONFIG_PATH)

app_name = _config["Application"]["name"]
clock_zone = _config["Clock"]["zone"]
logpath= _config["Clock"]["logpath"]