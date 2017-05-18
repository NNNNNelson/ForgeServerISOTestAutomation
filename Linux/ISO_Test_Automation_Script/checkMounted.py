import commands


def checkMounted(diskNum):
    print 'Checking if mounted successfully...'
    print '\t\'ls\' the path /home/test/ISO_Test/ISO_Mount...'

    lsOutput = commands.getoutput('ls /home/test/ISO_Test/ISO_Mount')
    print '\tThe result is:\n\t' + lsOutput

    if lsOutput != '':
        print 'Succefully mounted ' + diskNum + '! <--PASS'
    else:
        print 'Failed to mount ' + diskNum + '! <--FAIL'
