import sys
import uflash

if len(sys.argv) > 1:
	filename = sys.argv[1]
else:
	print "Missing filename on command line."
	sys.exit(1)

print "File: " + filename

print "Looking for micro:bit..."

microbitPath = uflash.find_microbit()

if microbitPath == None:
	print "Cannot find micro:bit. Check that it is plugged in via USB."
	sys.exit(1)

print "micro:bit found @ " + microbitPath

print "uflash version " + uflash.get_version()

uflash.flash(filename, microbitPath)
