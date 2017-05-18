import commands


def mount(diskNum):
    # Search the ISO_Downloaded path to find the D1 iso file
    isoTestPath = '/home/test/ISO_Test'
    isoDownloadedPath = isoTestPath + '/ISO_Downloaded'
    isoFilePath = commands.getoutput(
        'find /home/test/ISO_Test/ISO_Downloaded -name \"*' + diskNum + '.iso\"')

    # Mount the found iso file
    print 'Mounting ' + diskNum + '...'
    print commands.getoutput('mount -o loop ' + isoFilePath +
                             ' /home/test/ISO_Test/ISO_Mount')
