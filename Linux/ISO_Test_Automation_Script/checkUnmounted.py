import commands


def checkUnmounted(diskNum):
    print 'Checking if unmounted successfully...'
    print '\t\'ls\' the path /home/test/ISO_Test/ISO_Mount...'

    lsOutput = commands.getoutput('ls /home/test/ISO_Test/ISO_Mount')
    print '\tThe result is:\n\t' + lsOutput

    if lsOutput == '':
        print 'Succefully unmounted ' + diskNum + '! <--PASS'
    else:
        print 'Failed to unmount ' + diskNum + '! <--FAIL'
