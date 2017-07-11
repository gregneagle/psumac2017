#!/usr/bin/python

# https://gist.githubusercontent.com/pudquick/
#     097f97f4cb67c554f04dba6b5a09a506/raw/
#     09ae00656d20938af0145fec1c7a115d8c64a5c4/lockscreen_pyobjc.py

import objc
from Foundation import NSBundle
login_bundle = NSBundle.bundleWithPath_(
    '/System/Library/PrivateFrameworks/login.framework')

functions = [('SACLockScreenImmediate', '@'),]
objc.loadBundleFunctions(login_bundle, globals(), functions)


# Lock the screen regardless of security settings or who is logged in
result = SACLockScreenImmediate()