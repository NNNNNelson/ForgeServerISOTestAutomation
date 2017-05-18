import commands
import filecmp


def compareISOAndCopyContent(diskNum):
    print 'For ISO ' + diskNum + ', comparing copied files with original ISO files...'
    # Modify the mounted_content.txt file to delete pathe related lines
    commands.getoutput('sed \'s/^\/home.*//g\' /home/test/ISO_Test/ISO_' + diskNum +
                       '_mounted_content.txt > /home/test/ISO_Test/ISO_' + diskNum + '_mounted_content_modified.txt')
    # Modify the copy_content.txt file to delete pathe related lines
    commands.getoutput('sed \'s/^\/home.*//g\' /home/test/ISO_Test/ISO_' + diskNum +
                       '_copy_content.txt > /home/test/ISO_Test/ISO_' + diskNum + '_copy_content_modified.txt')
    # Compare if the modified files are the same
    compareResult = filecmp.cmp('/home/test/ISO_Test/ISO_' + diskNum +
                                '_mounted_content_modified.txt', '/home/test/ISO_Test/ISO_' + diskNum + '_copy_content_modified.txt')

    if compareResult:
        print 'The copied files are the same as original ISO files. <--PASS'
    else:
        print 'The copied files and original ISO files are different!. <--FAIL'
