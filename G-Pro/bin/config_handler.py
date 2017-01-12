#!/user/bin/python

# Handle all configurations and settings

# import statements
import configparser



# variable declarations
parser = configparser.ConfigParser()
path = "config.ini"


# test if config.ini exists and create if it doesn't
def checkconfig():

    try:
        open(path, "a")
        print ("config.ini created")
    except IOError as e:
        print('Could not fetch configurations', e)



parser.read('config.ini')

# parser.write
print (parser.get('file_settings', 'savedir'))