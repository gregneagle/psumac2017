#!/usr/bin/python

# https://developer.apple.com/reference/appkit/nsworkspace?language=objc

from AppKit import NSWorkspace

# get the shared workspace
workspace = NSWorkspace.sharedWorkspace()

# print a list of running applications
print workspace.runningApplications()
