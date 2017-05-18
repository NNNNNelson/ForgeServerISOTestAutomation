import commands


def listMountedContent(diskNum):
    print 'Writing mounted ' + diskNum + 'content to file \'/home/test/ISO_Test/ISO_' + diskNum + '_mounted_content.txt\''
    commands.getoutput(
        'ls -R /home/test/ISO_Test/ISO_Mount/* > /home/test/ISO_Test/ISO_' + diskNum + '_mounted_content.txt')
    print 'Please manually check the mounted ' + diskNum + ' content.'
