import commands


def unmount(diskNum):
    print '\nUnmounting ' + diskNum + '...'
    commands.getoutput('umount /home/test/ISO_Test/ISO_Mount')
