#!/user/bin/python

# Handle all configurations and settings

# import statements
import configparser
import getpass
import os
import platform
import errno


# test if config.ini exists and create if it doesn't
def checkconfig():

    try:
        file = open('config.ini', "a")
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
    checkconfig()
    value = get_config(path, section, setting)
    print("Section [{section}], Option [{setting}] is {value}".format(section=section,
                                                                      setting=setting, value=value))
    return value


# use default working directory
def defaultdirectory():

    value = get_setting('./config.ini', 'File_Settings', 'workdir')
    print("hello bubba")

    if value is False:

        # get user name
        user = getpass.getuser()

        if platform.system() == 'Windows':

            initdir = 'C:/Users/%s/Documents/Rapid Pro' % user
            makedir(initdir)

        elif platform.system() == 'Linux':
            initdir = '/home/%s/Documents/Rapid Pro' % user
            makedir(initdir)

        else:
            print('Don\'t tell me you\'re running apple :S ')

    else:
        initdir = get_setting('./config.ini', 'File_Settings', 'workdir')
        return initdir


def makedir(var1):

    try:
        os.mkdir(var1)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


print(get_setting('./config.ini', 'File_Settings', 'workdir'))
