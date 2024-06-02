import configparser
Config = configparser.ConfigParser()
Config['DEFAULT'] = {
    "MAIN" : '0.5',
    "MUSIC" :  '0.5',
    "SFX" : '0.5'
}
with open('/test.ini','w') as configfile:
    Config.write(configfile)