#!/usr/bin/python

# https://developer.apple.com/reference/systemconfiguration/
#     1517123-scdynamicstorecopyconsoleuser?language=objc


from SystemConfiguration import SCDynamicStoreCopyConsoleUser

print SCDynamicStoreCopyConsoleUser(None, None, None)
