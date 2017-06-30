#!/usr/bin/python

# https://developer.apple.com/reference/systemconfiguration/
#     1517123-scdynamicstorecopyconsoleuser?language=objc

# An example of calling a function that has pointer/by reference/'out'-style
# parameters that return additional values. In PyObjC you pass None for these
# and the values are added to a tuple of returned values

from SystemConfiguration import SCDynamicStoreCopyConsoleUser

# if we pass None for the 'store' parameter (the first one),
# the SystemConfiguration framework will use a temporary store it creates
name, uid, gid = SCDynamicStoreCopyConsoleUser(None, None, None)

print 'Name: %s' % name
print 'uid: %s' % uid
print 'gid: %s' % gid
