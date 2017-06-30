#!/usr/bin/python

# localauthdemo.py
# Created 19 Jan 2017, Greg Neagle
# Demonstrates using the LocalAuthentication framework and Touch ID

# Apple LocalAuthentication documentation
# https://developer.apple.com/reference/localauthentication?language=objc

# PyObjC LocalAuthentication wrappers from
# https://pypi.python.org/pypi/pyobjc-framework-LocalAuthentication/

import sys

from LocalAuthentication import LAContext
from LocalAuthentication import LAPolicyDeviceOwnerAuthentication


def authenticate(reason=''):
    '''Authenticate via Touch ID if possible, or user password if not'''

    class AuthStatus(object):
        '''Tracks the results of our authorization attempt'''
        def __init__(self):
            '''Initializes our instance variables'''
            self.result = None
            self.error = None

        def reply_handler(self, success, error):
            '''This is used in place of the callable block for
            LAContext's - evaluatePolicy:localizedReason:reply:
            to get the result of the attempted authentication'''
            if success:
                self.result = True
            else:
                self.error = error
                self.result = False

    # create object to track our authentication result
    auth_status = AuthStatus()
    # create LocalAuthentication context object
    context = LAContext.alloc().init()
    # make sure it can evaluate the policy
    can_eval_policy, error = context.canEvaluatePolicy_error_(
        LAPolicyDeviceOwnerAuthentication, None)

    if can_eval_policy:
        # attempt to authenticate
        context.evaluatePolicy_localizedReason_reply_(
            LAPolicyDeviceOwnerAuthentication, reason,
            auth_status.reply_handler)

        while auth_status.result is None:
            # wait for reply handler to fire and set
            pass

        if auth_status.error:
            print >> sys.stderr, auth_status.error
    else:
        print >> sys.stderr, error

    return auth_status.result

# main!
if authenticate(reason='prevent all your files from being erased'):
    print 'Chocolate purchased!'
else:
    print 'No chocolate for you!'
    