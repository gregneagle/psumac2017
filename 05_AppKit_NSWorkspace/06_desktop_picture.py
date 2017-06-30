#!/usr/bin/python

# Uses Cocoa classes via PyObjC to set a random desktop picture on all screens.

import glob
import random

from AppKit import NSWorkspace, NSScreen
from Foundation import NSURL

# pick a picture at random from our folder of pictures
pictures_glob = glob.glob("/Library/Desktop Pictures/*.jpg")
picture_path = random.choice(pictures_glob)

# convert the desktop picture path to an NSURL object
# https://developer.apple.com/reference/foundation/nsurl?language=objc
file_url = NSURL.fileURLWithPath_(picture_path)

# get shared workspace
# https://developer.apple.com/reference/appkit/nsworkspace?language=objc
workspace = NSWorkspace.sharedWorkspace()

# iterate over all screens
# https://developer.apple.com/reference/appkit/nsscreen?language=objc
for screen in NSScreen.screens():
    # tell the workspace to set the desktop picture
    (result, error) = workspace.setDesktopImageURL_forScreen_options_error_(
        file_url, screen, None, None)
