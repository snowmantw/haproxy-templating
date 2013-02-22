
import sys

from template import Driver


if len(sys.argv) < 2:
	print "[ERROR] No haproxy command or path."
	exit(64)

if len(sys.argv) < 3:
	print "[ERROR] No target configure path."
	exit(64)

if len(sys.argv) < 4:
	print "[ERROR] No path of node list."
	exit(64)

haproxy   = sys.argv[1]
config    = sys.argv[2]
nodelist  = sys.argv[3]

(Driver()
.templating(nodelist)
.hapath(config)
.write_cfg()
.start_service(haproxy))
