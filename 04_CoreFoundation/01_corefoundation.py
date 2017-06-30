#!/usr/bin/python

# https://developer.apple.com/reference/corefoundation/
#     1666648-preferences_utilities?language=objc

import CoreFoundation

# similar to `defaults read com.apple.Finder ShowHardDrivesOnDesktop`
print CoreFoundation.CFPreferencesCopyAppValue("ShowHardDrivesOnDesktop",
                                               "com.apple.Finder")
