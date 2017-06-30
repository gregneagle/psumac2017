#!/usr/bin/python

# https://developer.apple.com/reference/corefoundation/
#     1666648-preferences_utilities?language=objc

import CoreFoundation

# similar to `defaults write com.apple.Finder ShowHardDrivesOnDesktop -bool NO`
CoreFoundation.CFPreferencesSetAppValue(
    "ShowHardDrivesOnDesktop", False, "com.apple.Finder")
