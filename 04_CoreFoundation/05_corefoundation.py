#!/usr/bin/python

# https://developer.apple.com/reference/corefoundation/
#     1666648-preferences_utilities?language=objc

import CoreFoundation

# get effective preference
askForPassword = CoreFoundation.CFPreferencesCopyAppValue(
    "askForPassword", "com.apple.screensaver")

# find out if it's 'forced' AKA managed always by MCX or config profile
valueIsManaged = CoreFoundation.CFPreferencesAppValueIsForced(
    "askForPassword", "com.apple.screensaver")

print "Screensaver ask for password: %s" % askForPassword
print "Screensaver ask for password value is managed: %s" % valueIsManaged