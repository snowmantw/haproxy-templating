import csv
import os
from string import Template

TCP_PORT=5222
WS_PORT =5288

class Templating():

	def __init__(self):
		self.hosts     = []
		self.node_tpl  = Template("")
		self.hacfg_tpl = Template("")
		self.nodes_tcp = [] 
		self.nodes_ws  = []
		self.hacfg	  = ""
		self

	# Read nodes template
	def read_tpl(self, path_node, path_haproxy):

		with open(path_node, 'r') as f:
			self.node_tpl  = Template(f.read())
		f.close
		with open(path_haproxy, 'r') as f:
			self.hacfg_tpl  = Template(f.read())
		f.close
		return self

	# Read nodes from a csv, host must be first field.
	def read_list_nodes(self, path):

		with open(path, 'rb') as f:
			rows = csv.reader(f, delimiter=",")
			self.hosts = map(lambda r: r[0],rows)
		f.close
		return self

	# Template nodes
	def fill_nodes(self):
		self.nodes_tcp  = map(lambda h: self.node_tpl.substitute(host=h, port=TCP_PORT),self.hosts)
		self.nodes_ws   = map(lambda h: self.node_tpl.substitute(host=h, port=WS_PORT ),self.hosts)
		return self

	def fill_haproxy(self): 
		self.hacfg = self.hacfg_tpl.substitute(
			nodes_tcp=("".join(self.nodes_tcp)), 
			nodes_ws=("".join(self.nodes_ws)))
		return self

	def done(self):
		return self.hacfg

class Driver():
	
	def __init__(self):
		self.hacfg  = ""
		self.hacfg_path = ""
		self.basepath = os.path.dirname(os.path.realpath(__file__))

	def templating(self, nodelist): 
		self.hacfg = (Templating().
			read_tpl('%s/node.tpl' % (self.basepath),'%s/haproxy.cfg.tpl' % (self.basepath)).
			read_list_nodes(nodelist).
			fill_nodes().
			fill_haproxy().
			done())
		return self

	def hapath(self, path):
		self.hacfg_path = path
		return self

	def write_cfg(self):
		with open(self.hacfg_path, 'w') as f:
			f.write(self.hacfg)
		f.close
		return self

	# Pass in haproxy command, must with '-f' option to read config file.
	def start_service(self, haproxy):
		os.system("%s %s" % (haproxy, self.hacfg_path) )
		return self

