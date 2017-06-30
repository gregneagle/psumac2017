#!/usr/bin/python

# https://developer.apple.com/reference/appkit/nsworkspace?language=objc
# https://developer.apple.com/reference/appkit/
#     nsrunningapplication?language=objc
# https://developer.apple.com/reference/appkit/
#     nsapplicationactivationoptions?language=objc

from AppKit import NSWorkspace, NSApplicationActivateIgnoringOtherApps

# get the shared workspace object
workspace = NSWorkspace.sharedWorkspace()

# get the list of running applications
running_apps = workspace.runningApplications()

# iterate through the list looking for bundleIdentifier of com.apple.finder
for app in running_apps:
    if app.bundleIdentifier() == 'com.apple.finder':
        app.activateWithOptions_(NSApplicationActivateIgnoringOtherApps)
