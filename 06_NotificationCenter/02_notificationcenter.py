#!/usr/bin/python

# See:
# https://developer.apple.com/reference/foundation/
#    nsusernotificationcenter?language=objc
# and:
# https://developer.apple.com/reference/foundation/
#    nsusernotification?language=objc

from Foundation import NSBundle
from Foundation import NSUserNotificationCenter
from Foundation import NSUserNotification


def set_fake_bundleid(bundleid):
    # disturbing hack warning! Thank you, @frogor
    bundle = NSBundle.mainBundle()
    info = bundle.localizedInfoDictionary() or bundle.infoDictionary()
    # override the bundleid with the one we want
    info['CFBundleIdentifier'] = bundleid


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

    # deliver the notification
    nc.deliverNotification_(notification)


notify(u'Updates available', u'', u'Software updates are available.',
       bundleid='com.googlecode.munki.ManagedSoftwareCenter')
