#!/user/bin/env python
#  Set initial/user set working directory depending on platform

import platform, getpass, os



class defaultDir():

    #test platform and make working dir if not present
    def default_directory():
        #get user name
        user = getpass.getuser()

        if platform.system() == 'Windows':

            initdir = 'C:/Users/%s/Documents/Rapid Pro' % user

        if platform.system() == 'Linux':
            initdir = '/home/%s/Documents/Rapid Pro' % user

        try:
            os.mkdir(initdir)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise
            return(initdir)