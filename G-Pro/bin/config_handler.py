#!/user/bin/python

# Handle all configurations and settings

# import statements
import configparser


# variable declarations
parser = configparser.ConfigParser()
path = "config.INI"

# test if config.INI exists and create if it doesn't
def checkconfig():

    try:
        f = open(path, "a")
        print ("config.INI created")
        f.close()
    except IOError as e:
        print('Could not fetch configurations', e)


def defworkdir():

    checkconfig()
    parser.read_file('config.INI')
    #
    # workdir = parser.get('File_Settings', 'savedir')
    # print (workdir)
    # return workdir


defworkdir()
# for candidate in ['File_Settings']:
#     print('{:<12}: {}'. format(candidate, parser.has_section(candidate)))

