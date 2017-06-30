#!/usr/bin/python

# https://developer.apple.com/reference/appkit/nsworkspace?language=objc

from AppKit import NSWorkspace

# get the shared workspace
workspace = NSWorkspace.sharedWorkspace()

app_name = 'Microsoft Word'

# find the full path for an application
print workspace.fullPathForApplication_(app_name)

# launch an application
workspace.launchApplication_(app_name)
