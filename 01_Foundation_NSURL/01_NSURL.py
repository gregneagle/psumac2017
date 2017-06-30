#!/usr/bin/python

# https://developer.apple.com/reference/foundation/nsurl/
#     1410828-fileurlwithpath?language=objc

from Foundation import NSURL

print NSURL.fileURLWithPath_('/Users/Shared/foo')
