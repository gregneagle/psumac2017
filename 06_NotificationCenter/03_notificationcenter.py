#!/usr/bin/python

# See:
# https://developer.apple.com/reference/foundation/
#    nsusernotificationcenter?language=objc
# and:
# https://developer.apple.com/reference/foundation/
#    nsusernotification?language=objc

import subprocess

from Foundation import NSObject
from Foundation import NSUserNotificationCenter
from Foundation import NSUserNotification
from Foundation import NSBundle
from Foundation import NSRunLoop
from Foundation import NSDate


def set_fake_bundleid(bundleid):
    # disturbing hack warning! Thank you, @frogor
    bundle = NSBundle.mainBundle()
    info = bundle.localizedInfoDictionary() or bundle.infoDictionary()
    # override the bundleid with the one we want
    info['CFBundleIdentifier'] = bundleid


def get_fake_bundleid():
    # get the current bundleid (which might have been overridden)
    bundle = NSBundle.mainBundle()
    info = bundle.localizedInfoDictionary() or bundle.infoDictionary()
    return info['CFBundleIdentifier']


def launch_app_by_bundleid(bundleid):
    # We really should use NSWorkspace methods but we'll be lazy
    subprocess.call(['/usr/bin/open', '-b', bundleid])


class NotificationCenterDelegate(NSObject):
    '''Class to implement required NSUserNotificationCenterDelegate methods'''
    # See https://developer.apple.com/reference/foundation/
    #         nsusernotificationcenterdelegate?language=objc

    keepRunning = True

    def userNotificationCenter_didActivateNotification_(
            self, center, userNotification):
        print "Got userNotificationCenter:didActivateNotification:"
        launch_app_by_bundleid(get_fake_bundleid())
        self.keepRunning = False

    def userNotificationCenter_shouldPresentNotification_(
            self, center, userNotification):
        print "Got userNotificationCenter:shouldPresentNotification:"
        return True

    def userNotificationCenter_didDeliverNotification_(
            self, center, notification):
        print "Got userNotificationCenter:didDeliverNotification:"


def notify(title, subtitle, text, bundleid=None):
    if bundleid:
        # fake our bundleid
        set_fake_bundleid(bundleid)

    # create a new user notification
    notification = NSUserNotification.alloc().init()
    notification.setTitle_(title)
    notification.setSubtitle_(subtitle)
    notification.setInformativeText_(text)

    # get the default User Notification Center
    nc = NSUserNotificationCenter.defaultUserNotificationCenter()

    # create a delegate object that implements our delegate methods
    my_delegate = NotificationCenterDelegate.alloc().init()
    nc.setDelegate_(my_delegate)

    # deliver the notification
    nc.deliverNotification_(notification)

    # keep running until the notification is activated
    while (my_delegate.keepRunning):
        NSRunLoop.currentRunLoop().runUntilDate_(
            NSDate.dateWithTimeIntervalSinceNow_(0.1))


notify(u'Updates available', u'', u'Software updates are available.',
       bundleid='com.googlecode.munki.ManagedSoftwareCenter')
