import commands


def removeISOCopiedFiles(diskNum):
    print 'For ' + diskNum + ', deleting /home/test/ISO_Test/ISO_Copy path contents...'
    commands.getoutput('rm -rf /home/test/ISO_Test/ISO_Copy/*')