#!/usr/bin/python

# https://developer.apple.com/reference/foundation/nsurl/
#     1414650-fileurlwithpath?language=objc

from Foundation import NSURL

print NSURL.fileURLWithPath_isDirectory_('/Users/Shared/foo', True)
