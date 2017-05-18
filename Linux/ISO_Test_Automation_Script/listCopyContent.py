import commands


def listCopyContent(diskNum):
    print 'Writing copied ' + diskNum + 'content to file \'/home/test/ISO_Test/ISO_' + diskNum + '_copy_content.txt\''
    commands.getoutput(
        'ls -R /home/test/ISO_Test/ISO_Copy/* > /home/test/ISO_Test/ISO_' + diskNum + '_copy_content.txt')
