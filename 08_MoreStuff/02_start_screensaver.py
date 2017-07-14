#!/usr/bin/python
'''A script to immediately start the screen saver. Should almost certainly
be run in the GUI user's context.'''

# inspired by
# http://www.ragingmenace.com/software/sleeptight/index.html

###################################################################
# ScreenSaver.framework private API
# Isn't class-dump fun?

# @protocol ScreenSaverControl
# - (double)screenSaverTimeRemaining;
# - (void)restartForUser:fp12;
# - (void)screenSaverStopNow;
# - (void)screenSaverStartNow;
# - (void)setScreenSaverCanRun:(char)fp12;
# - (BOOL)screenSaverCanRun;
# - (BOOL)screenSaverIsRunning;
# @end

# @interface ScreenSaverController:NSObject <ScreenSaverControl>

# + controller;
# + monitor;
# + daemonConnectionName;
# + daemonPath;
# + enginePath;
# - init;
# - (void)dealloc;
# - (void)_connectionClosed:fp12;
# - (BOOL)screenSaverIsRunning;
# - (BOOL)screenSaverCanRun;
# - (void)setScreenSaverCanRun:(char)fp12;
# - (void)screenSaverStartNow;
# - (void)screenSaverStopNow;
# - (void)restartForUser:fp12;
# - (double)screenSaverTimeRemaining;

# @end
###################################################################

import os
import time

import ScreenSaver
from CoreFoundation import CFPreferencesGetAppIntegerValue
from CoreFoundation import CFPreferencesSetValue
from CoreFoundation import CFPreferencesAppSynchronize
from CoreFoundation import kCFPreferencesCurrentUser, kCFPreferencesCurrentHost


def screensaver_password_active():
    '''Is askForPassword set to True for the screensaver?'''
    is_on, is_good = CFPreferencesGetAppIntegerValue(
        'askForPassword', 'com.apple.screensaver', None)
    if is_on and is_good:
        return True
    return False


def set_screensaver_password_pref(state):
    '''Set boolean value for askForPassword for com.apple.screensaver'''
    CFPreferencesSetValue(
        'askForPassword', int(bool(state)), 'com.apple.screensaver',
        kCFPreferencesCurrentUser, kCFPreferencesCurrentHost)
    CFPreferencesAppSynchronize('com.apple.screensaver')


def start_saver(controller):
    '''Start 'r up'''
    # Make sure password is required
    if not screensaver_password_active():
        set_screensaver_password_pref(True);
    for iteration in range(30):
        # If the screensaver is already running do nothing
        if controller.screenSaverIsRunning():
            return
        # Can screensaver start?
        if controller.screenSaverCanRun():
            # Start the screensaver
            controller.screenSaverStartNow()
            return


ss_controller = ScreenSaver.ScreenSaverController.controller()
if not ss_controller:
    exit(-1)
start_saver(ss_controller)
