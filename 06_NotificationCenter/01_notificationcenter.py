#!/usr/bin/python

# See:
# https://developer.apple.com/reference/foundation/
#    nsusernotificationcenter?language=objc
# and:
# https://developer.apple.com/reference/foundation/
#    nsusernotification?language=objc

from Foundation import NSUserNotificationCenter
from Foundation import NSUserNotification


def notify(title, subtitle, text):
    # create a user notification
    notification = NSUserNotification.alloc().init()
    notification.setTitle_(title)
    notification.setSubtitle_(subtitle)
    notification.setInformativeText_(text)

    # get the default User Notification Center
    nc = NSUserNotificationCenter.defaultUserNotificationCenter()

    # tell the notification center to deliver the user notification
    nc.deliverNotification_(notification)


notify(u'Updates available', u'', u'Software updates are available.')
