#
#   MunkiHelperPackageImageView.py
#
#   Created by Jesse Peterson on 5/20/12.
#   Copyright 2012 __MyCompanyName__. All rights reserved.
#

from Foundation import *
from AppKit import *
import objc

class MunkiHelperPackageImageView (NSImageView):
	controller = objc.IBOutlet()
	
	def awakeFromNib(self):
		self.registerForDraggedTypes_([NSFilenamesPboardType])

	def draggingEntered_(self, sender):
		if self.controller.isValidPackageDrag(sender.draggingPasteboard()):
			return NSDragOperationCopy
		else:
			return NSDragOperationNone

	def performDragOperation_(self, sender):
		if not self.controller.isValidPackageDrag(sender.draggingPasteboard()):
			return False

		pboard = sender.draggingPasteboard()
		fileArray = pboard.propertyListForType_(NSFilenamesPboardType)
		package = fileArray[0]

		self.controller.addPackage(package)

		return True
