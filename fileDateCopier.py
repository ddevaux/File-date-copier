# coding: utf8
import os
from collections import OrderedDict
import argparse
import cPickle
 
parser = argparse.ArgumentParser(description = "File date copier")
parser.add_argument("mode", choices=['R','W'], help="Mode Read/Write")
parser.add_argument("path", default=".", nargs="?")
parser.add_argument("-d", "--data", default="dates.dat", help="File to write/read from")
args = parser.parse_args()
 
if args.mode == "R":
 
	pathdates = OrderedDict()
	
	total_files = total_dirs = 0
 
	def save_path(path):
		pathdates[path] = (os.path.getatime(path), os.path.getmtime(path))
 
	for dirpath, dirnames, filenames in os.walk(unicode(args.path)):
		total_files += len(filenames)
		total_dirs += len(dirnames)
		for d in dirnames:
			save_path(os.path.join(dirpath, d))
		
		for f in filenames:
			save_path(os.path.join(dirpath, f))
			
			
	f = open(args.data, "wb")
	cPickle.dump(pathdates, f)
	f.close()
	
	print "Found %d files, %d directories" % (total_files, total_dirs)
	
elif args.mode == "W":
	
	f = open(args.data, "rb")
	pathdates = cPickle.load(f)
	f.close()
	
	os.chdir(args.path)
	
	total_updated = 0
	
	for path, dates in pathdates.iteritems():
		if os.path.exists(path):
			os.utime(path, dates)
			total_updated += 1
		
	print "Updated %d files/directories out of %d entries" % (total_updated, len(pathdates))
	
	
