#
#  MunkiHelperAppDelegate.py
#  MunkiHelper
#
#  Created by Jesse Peterson on 5/19/12.
#  Copyright __MyCompanyName__ 2012. All rights reserved.
#

from Foundation import *
from AppKit import *
import objc
import os

class MunkiHelperAppDelegate(NSObject):
	munkiFolderPath = objc.ivar(u'munkiFolderPath')

	def applicationDidFinishLaunching_(self, sender):
		NSLog("Application did finish launching.")

	@objc.IBAction
	def openCatalogsFolder_(self, sender):
		if self.munkiFolderPath != None:
			ws = NSWorkspace.sharedWorkspace()
			ws.selectFile_inFileViewerRootedAtPath_(os.path.join(self.munkiFolderPath, 'catalogs'), None)

	@objc.IBAction
	def openManifestsFolder_(self, sender):
		if self.munkiFolderPath != None:
			ws = NSWorkspace.sharedWorkspace()
			ws.selectFile_inFileViewerRootedAtPath_(os.path.join(self.munkiFolderPath, 'manifests'), None)

	@objc.IBAction
	def openPkgsFolder_(self, sender):
		if self.munkiFolderPath != None:
			ws = NSWorkspace.sharedWorkspace()
			ws.selectFile_inFileViewerRootedAtPath_(os.path.join(self.munkiFolderPath, 'pkgs'), None)

	@objc.IBAction
	def openPkgsinfoFolder_(self, sender):
		if self.munkiFolderPath != None:
			ws = NSWorkspace.sharedWorkspace()
			ws.selectFile_inFileViewerRootedAtPath_(os.path.join(self.munkiFolderPath, 'pkgsinfo'), None)


	@objc.IBAction
	def rebuildCatalogs_(self, sender):
		ascr = NSAppleScript.alloc().initWithSource_('''
tell application "Terminal"
	activate
	do script "/usr/local/munki/makecatalogs %s"
end tell
''' % self.munkiFolderPath)
		ascr.executeAndReturnError_(None)

	def isValidPackageDrag(self, pboard):
		if self.munkiFolderPath is None:
			return False

		if NSFilenamesPboardType not in pboard.types():
			return False

		filesArray = pboard.propertyListForType_(NSFilenamesPboardType)
		
		if len(filesArray) != 1:
			return False

		package = filesArray[0]
		
		if os.path.isdir(package):
			NSLog("Munki package cannot be a directory")
			return False

		if package.lower().endswith('.dmg') or package.lower().endswith('.pkg'):
			return True
		
		NSLog("Not a valid Munki package (DMG or PKG only)")
		return False

	def addPackage(self, pkg):
		NSLog("Attempting to add package - sending AppleScript")
		basename = os.path.basename(pkg)
		ascr = NSAppleScript.alloc().initWithSource_('''
tell application "Terminal"
	activate
	set curWin to do script "cp -pv '%s' '%s/pkgs'"
	do script "/usr/local/munki/makepkginfo '%s/pkgs/%s' > '%s/pkgsinfo/%s.pkginfo'" in curWin
	do script "open -R '%s/pkgsinfo/%s.pkginfo'" in curWin
end tell
''' % (pkg, self.munkiFolderPath, self.munkiFolderPath, basename, self.munkiFolderPath, basename, self.munkiFolderPath, basename))
		ascr.executeAndReturnError_(None)
