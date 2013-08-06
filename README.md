# File-date-copier #

Saves and restores file dates across computers. I needed this after a long FTP transfer completely ignored the last accessed/modified dates.

This tool copy and restore `atime` and `mtime`. Creation time is ignored (on Unix it is not saved anyway)

# Usage #

	usage: fileDateCopier.py [-h] [-d DATA] {R,W} [path]

	File date copier

	positional arguments:
	  {R,W}                 Mode Read/Write
	  path

	optional arguments:
	  -h, --help            show this help message and exit
	  -d DATA, --data DATA  File to write/read from

First, grab the dates :

*The default path is the current directory*

	python fileDateCopier.py R

Copy the `dates.dat` to where you want the dates restored

Then, simple run

	python fileDateCopier.py W



# Requirements #

Python 2.7 with no additional modules (standard library). Uses `argparse` hence the 2.7

