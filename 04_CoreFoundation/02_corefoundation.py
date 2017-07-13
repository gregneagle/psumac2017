#!/usr/bin/python

# https://developer.apple.com/reference/corefoundation/
#     1666648-preferences_utilities?language=objc


import subprocess
import CoreFoundation

# get the value using defaults
value = subprocess.check_output(
    ['/usr/bin/defaults', 'read', 'com.apple.Finder', 'ShowHardDrivesOnDesktop']
)
print 'Value is %s and is type %s' % (repr(value), type(value))

# get the value using CFPreferences
value = CoreFoundation.CFPreferencesCopyAppValue('ShowHardDrivesOnDesktop',
                                                 'com.apple.Finder')
print 'Value is %s and is type %s' % (repr(value), type(value))
