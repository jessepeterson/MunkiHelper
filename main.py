#
#  main.py
#  MunkiHelper
#
#  Created by Jesse Peterson on 5/19/12.
#  Copyright __MyCompanyName__ 2012. All rights reserved.
#

#import modules required by application
import objc
import Foundation
import AppKit

from PyObjCTools import AppHelper

# import modules containing classes required to start application and load MainMenu.nib
import MunkiHelperAppDelegate
import MunkiHelperRepositoryImageView
import MunkiHelperPackageImageView

# pass control to AppKit
AppHelper.runEventLoop()
