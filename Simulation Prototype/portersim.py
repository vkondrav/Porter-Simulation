﻿from InitTaskList import initEventList
from BinTree import BTree

class State(object):

	def __init__():
		self.porters = []
		self.wards = []
		self.tasks = []
		
		
class FutureEventList(object):

	def __init__(self):
		self.eventList = BTree
		
	def insert(self,data):
		self.eventList.insert(data)
		
	def pop(self):
		return self.eventList.pop()
		
	def isEmpty(self):
		return self.eventList.isEmpty()

class Porter(object):

	def __init__():
		self.state = 'pending'
		self.ward = None
		
	def setStatePending():
		self.state = 'pending'
		
	def setStateDispatch():
		self.state = 'dispatch'
		
	def setStateInProgress():
		self.state = 'inprogress'
				
	def setStateComplete():
		self.state = 'complete'
		
	
class SpanningTree(object):

	def __init__():
		self.nodes = []
		self.edges = []
		self.numNodes = 0
		self.numEdges = 0

	def addNode():
		pass
		
	def addEdge():
		pass
		
		
class Node(object):
	
	def __init__():
		pass
		
		
class Ward(Node):
	
	def __init__():
		super(self, Node)
		
		
class Dispatcher(object):

	def __init__():
		pass
		
	def assignTask():
		pass
		
		
class Event(object):
	
	def __init__():
		self.func = None
		self.args = []
		
	def trigger():
		self.func(*self.args)
	
		
def main():
	EventList = FutureEventList()
	SpanTree = SpanningTree
	SimState = State
	
	#while not EventList.isEmpty():
	#	event = EventList.pop()
	#	event.log()
	#	event.trigger()
		
main()