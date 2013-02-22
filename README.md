
## A HAProxy Templating Tool

Clustering nodes made me implement this.

All "dirty hacks", but it works.

## Usage


    python main.py "haproxy -f" <your-haproxy-configure-target-path> <node-list-csv>

Will automatically put merged HAProxy configure file to the specific path, and run it.

You may need put some wrapper script with root priviledge in system path, and execute 
this tool via that script to ensure some operations works, like mergeing to system configure, 
or run service with priviledge.

See the "scripts-example" directory for wrapper scripts.


## License

Take or modify it freely under GPLv3.
