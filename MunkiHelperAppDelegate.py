#
#  MunkiHelperAppDelegate.py
#  MunkiHelper
#
#  Created by Jesse Peterson on 5/19/12.
#  Copyright __MyCompanyName__ 2012. All rights reserved.
#

from Foundation import *
from AppKit import *

class MunkiHelperAppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")
