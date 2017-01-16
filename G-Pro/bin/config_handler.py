#!/user/bin/python

# Handle all configurations and settings

# import statements
import configparser

confile = "config.ini"


# test if config.ini exists and create if it doesn't
def checkconfig(path):

    try:
        file = open(path, "a")
        print("config.ini created")
        file.close()
    except IOError as exception:
        print('Could not fetch configurations', exception)


def get_config(path):
    """
     Returns the config object
    """
    config = configparser.ConfigParser()
    config.read(path)
    return config

def get_setting(path, section, setting):
    """
    get values from front sections
    """
    checkconfig(path)
    config = get_config(path)
    value = config.get(section, setting)
    print ("{section} {setting} is {value}".format(section=section,
                                                  setting=setting, value=value))
    return value


# checkconfig(confile)
# get_setting(confile, 'File_Settings', 'workdir')
