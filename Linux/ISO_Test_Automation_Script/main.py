#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-02-08 23:00:45
# @Author  : Nelson Wang (nelson.wang@quest.com)
# @Link    : 
# @Version : 1.0

import mount
import checkMounted
import unmount
import checkUnmounted
import printDividerLine
import printScenarioDivider
import listMountedContent
import copyToCopyPath
import listCopyContent
import compareISOAndCopyContent
import removeISOCopiedFiles

if __name__ == '__main__':
    # Scenario: Test ISO file mount and unmount
    printScenarioDivider.printScenarioDivider('Mount/Unmount Test')
    # Test ISO D1 file mount and unmount
    # Mount ISO file D1
    mount.mount('D1')
    # Check if ISO D1 mounted succefully
    checkMounted.checkMounted('D1')
    # Unmount ISO D1
    unmount.unmount('D1')
    # Check if ISO D1 unmounted successfully
    checkUnmounted.checkUnmounted('D1')
    printDividerLine.printDividerLine()
    # Test ISO D2 file mount and unmount
    # Mount ISO file D1
    mount.mount('D2')
    # Check if ISO D1 mounted succefully
    checkMounted.checkMounted('D2')
    # Unmount ISO D1
    unmount.unmount('D2')
    # Check if ISO D2 unmounted successfully
    checkUnmounted.checkUnmounted('D2')

    # Scenario: List mounted ISO file content to a .txt file to have a manual
    # check
    printScenarioDivider.printScenarioDivider(
        'List mounted ISO content to have manual check')
    # List mounted ISO D1 content to 'ISO_D1_mounted_content.txt'
    # Mount ISO file D1
    mount.mount('D1')
    # List all mounted D1 content and write output to
    # 'ISO_D1_mounted_content.txt'
    listMountedContent.listMountedContent('D1')
    # Unmount D1
    unmount.unmount('D1')
    printDividerLine.printDividerLine()
    # List mounted ISO D2 content to 'ISO_D2_mounted_content.txt'
    # Mount ISO file D2
    mount.mount('D2')
    # List all mounted D2 content and write output to
    # 'ISO_D2_mounted_content.txt'
    listMountedContent.listMountedContent('D2')
    # Unmount D2
    unmount.unmount('D2')

    # Scenario: Test the mounted ISO content can be successfully copied to an
    # other folder
    printScenarioDivider.printScenarioDivider('Test copy mounted ISO content')
    # Copy D1 content to the ISO_Copy path and compare the content is right
    # Mount D1
    mount.mount("D1")
    # Copy ISO_Mount content to ISO_Copy
    copyToCopyPath.copyToCopyPath('D1')
    # List ISO_Copy content to 'ISO_D1_copy_content.txt'
    listCopyContent.listCopyContent('D1')
    # Compare if 'ISO_D1_mounted_content.txt' and 'ISO_D1_copy_content.txt'
    # are the same
    compareISOAndCopyContent.compareISOAndCopyContent('D1')
    # Remove all files in /home/test/ISO_Test/ISO_Copy path
    removeISOCopiedFiles.removeISOCopiedFiles('D1')
    # Unmount D1
    unmount.unmount('D1')
    printDividerLine.printDividerLine()
    # Copy D2 content to the ISO_Copy path and compare the content is right
    # Mount D2
    mount.mount("D2")
    # Copy ISO_Mount content to ISO_Copy
    copyToCopyPath.copyToCopyPath('D2')
    # List ISO_Copy content to 'ISO_D2_copy_content.txt'
    listCopyContent.listCopyContent('D2')
    # Compare if 'ISO_D2_mounted_content.txt' and 'ISO_D2_copy_content.txt'
    # are the same
    compareISOAndCopyContent.compareISOAndCopyContent('D2')
    # Remove all files in /home/test/ISO_Test/ISO_Copy path
    removeISOCopiedFiles.removeISOCopiedFiles('D2')
    # Unmount D2
    unmount.unmount('D2')
    printDividerLine.printDividerLine()

    # Scenario: Mount D1 and use the Linux x64 installer to install FMS in silent mode with default setting
    