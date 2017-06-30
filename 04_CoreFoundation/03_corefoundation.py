#!/usr/bin/python

# https://developer.apple.com/reference/corefoundation/
#     1666648-preferences_utilities?language=objc


import subprocess
import CoreFoundation

# get the value using defaults
print 'Running defaults...'
value = subprocess.check_output(
    ['/usr/bin/defaults', 'read', 'com.apple.Finder', 'StandardViewSettings']
)
print 'Type returned from defaults is %s' % type(value)
print value

# get the value using CFPreferences
print 'Calling CFPreferencesCopyAppValue...'
value = CoreFoundation.CFPreferencesCopyAppValue('StandardViewSettings',
                                                 'com.apple.Finder')
print 'Type returned from CFPreferencesCopyAppValue is %s' % type(value)

print ("StandardViewSettings['ExtendedListViewSettings']['calculateAllSizes'] "
       "is: %s" % value['ExtendedListViewSettings']['calculateAllSizes'])
