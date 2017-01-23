#!/user/bin/python

# Handle all configurations and settings

# import statements
import configparser


# test if config.ini exists and create if it doesn't
def checkconfig(path):

    try:
        file = open(path, "a")
        print("config.ini created")
        file.close()
    except IOError as exception:
        print('Could not fetch configurations', exception)


def get_config(path, section, setting):
    """
     Returns the config object
    """
    config = configparser.ConfigParser()
    config.read(path)
    result = config.get(section, setting)
    return result


def get_setting(path, section, setting):
    """
    get values from front sections
    """
    checkconfig(path)
    value = get_config(path, section, setting)
    print("Section [{section}], Option [{setting}] is {value}".format(section=section,
                                                                      setting=setting, value=value))
    return value


# print(get_setting('config.ini', 'File_Settings', 'workdir'))
