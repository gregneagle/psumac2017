#!/usr/bin/python
# https://developer.apple.com/reference/foundation/
#     1613024-foundation_functions?language=objc

import Foundation

print Foundation.NSUserName()
print Foundation.NSFullUserName()
print Foundation.NSHomeDirectory()
print Foundation.NSHomeDirectoryForUser('root')
print Foundation.NSTemporaryDirectory()
