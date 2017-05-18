import commands


def copyToCopyPath(diskName):
    print 'Copying ISO_Mount content to ISO_Copy path...'
    commands.getoutput('cp -r /home/test/ISO_Test/ISO_Mount/* /home/test/ISO_Test/ISO_Copy/')
