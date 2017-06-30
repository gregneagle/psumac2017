#!/usr/bin/python

# https://developer.apple.com/reference/appkit/nsworkspace?language=objc
# https://developer.apple.com/reference/appkit/
#     nsrunningapplication?language=objc
# https://developer.apple.com/reference/appkit/nsrunningapplication/
#     1525949-hidden?language=objc

from AppKit import NSWorkspace

# get the shared workspace object
workspace = NSWorkspace.sharedWorkspace()

# get the list of running applications
running_apps = workspace.runningApplications()

# iterate through the list looking for bundleIdentifier of com.apple.Terminal
for app in running_apps:
    if app.bundleIdentifier() == 'com.apple.Terminal':
        print 'Localized name: %s' % app.localizedName()
        print 'Bundle URL: %s' % app.bundleURL()
        print 'Launch date: %s' % app.launchDate()
        #print 'Currently hidden: %s' % app.hidden()
        # the hidden property getter is "isHidden()"
        print 'Currently hidden: %s' % app.isHidden()
