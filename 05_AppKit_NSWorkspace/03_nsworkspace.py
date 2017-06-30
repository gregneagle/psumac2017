#!/usr/bin/python

# https://developer.apple.com/reference/appkit/nsworkspace?language=objc
# https://developer.apple.com/reference/appkit/
#     nsrunningapplication?language=objc

from AppKit import NSWorkspace

# get the shared workspace object
workspace = NSWorkspace.sharedWorkspace()

# get the list of runningApplications
# (returns an array of NSRunningApplication objects)
running_apps = workspace.runningApplications()

# iterate through the list of NSRunningApplication objects and print the
# localized name
for app in running_apps:
    print app.localizedName()
