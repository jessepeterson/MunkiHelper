#
#   MunkiHelperRepositoryImageView.py
#
#   Created by Jesse Peterson on 5/20/12.
#   Copyright 2012 __MyCompanyName__. All rights reserved.
#

from Foundation import *
from AppKit import *
import objc
from LaunchServices import kGenericFolderIcon
import os

class MunkiHelperRepositoryImageView (NSImageView):
	controller = objc.IBOutlet()
	
	def awakeFromNib(self):
		self.registerForDraggedTypes_([NSFilenamesPboardType])

	def draggingEntered_(self, sender):
		if self.isValidMunkiFolderDrag(sender.draggingPasteboard()):
			return NSDragOperationCopy
		else:
			return NSDragOperationNone

	def performDragOperation_(self, sender):
		if not self.isValidMunkiFolderDrag(sender.draggingPasteboard()):
			return False

		pboard = sender.draggingPasteboard()
		fileArray = pboard.propertyListForType_(NSFilenamesPboardType)
		folder = fileArray[0]

		#self.controller.setFolderPath_(folder)
		self.controller._.munkiFolderPath = folder
		NSLog("folder path %@", folder)

		self.setFolderIcon()

		return True

	def setFolderIcon(self):
		folderIcon = NSWorkspace.sharedWorkspace().iconForFileType_(NSFileTypeForHFSTypeCode(kGenericFolderIcon))
		self.setImage_(folderIcon)

	def isValidMunkiFolderDrag(self, pboard):
		if NSFilenamesPboardType not in pboard.types():
			return False

		filesArray = pboard.propertyListForType_(NSFilenamesPboardType)
		
		if len(filesArray) != 1:
			return False

		folder = filesArray[0]
		
		if not os.path.isdir(folder):
			return False

		for i in ['pkgs', 'manifests', 'catalogs', 'pkgsinfo']:
			if not os.path.isdir(os.path.join(folder, i)):
				NSLog("Not a Munki repository (no %@ folder): %@", i, folder)
				return False
		
		return True



