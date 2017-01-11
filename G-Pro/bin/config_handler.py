#!/user/bin/env python

# Handle all configurations and settings

# import statements
import configparser
import os
import errno


# variable declarations
config = configparser.ConfigParser()
path = "config.ini"


# test if config.ini exists and create if it doesn't
def configdir():

    try:
        open(path, "a")
        print ("config.ini created")
    except IOError as exception:
        raise print('Could not create config.ini')


