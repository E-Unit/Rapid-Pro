#!/user/bin/python

# Handle all configurations and settings

# import statements
import configparser
import getpass
import os
import platform
import errno


# test if config.ini exists and create if it doesn't
def checkconfig(path):

    try:
        file = open(path, "a")
        print("config.ini present")
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


# use default working directory
def defaultdirectory(path):

    value = get_setting(path, 'File_Settings', 'workdir')
    print(value)

    if value == None:

        # get user name
        user = getpass.getuser()

        if platform.system() == 'Windows':

            initdir = 'C:/Users/%s/Documents/Rapid Pro' % user
            makedir(initdir)
            print("I'm on Windows")

        elif platform.system() == 'Linux':
            initdir = '/home/%s/Documents/Rapid Pro' % user
            makedir(initdir)
            print("I'm on Linus")

        else:
            print('Don\'t tell me you\'re running apple :S ')
            print("Garbage")

    else:
        initdir = value
        print("here we go")
        return initdir


def makedir(var1):

    try:
        os.mkdir(var1)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

