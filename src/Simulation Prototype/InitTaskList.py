import random
from BinTree import BTree
from BinTree import BTNode

HOUR = 60	##Hour Constant
TOTAL_HOUR = 1 ##Total hours of simulation
REQUEST_PER_HOUR = 10 ##Average requests per hour
VAR_PER_HOUR = 5 ##Variance for requests per hour


def initEventList(nodes):
	def createTask():
		#random.seed(1)
		taskTree = BTree()
		for i in range(0,TOTAL_HOUR):
			##Get a random number of tasks in an hour
			numTasks = int(random.normalvariate(REQUEST_PER_HOUR, VAR_PER_HOUR))
			if (numTasks > 0):
				for j in range(0,numTasks):
					##Choose a random start time for each task
					startTime = random.randrange(0, HOUR)
					task = [i,startTime, selectRandomNodes()]
					taskTree.insert(task)
		return taskTree
	
	def selectRandomNodes():
		##Select a random start and end point (cannot be the same)
		startNode = random.choice(nodes)
		endNode = random.choice(nodes)
		while startNode == endNode:
			endNode = random.choice(nodes)
			
		return [startNode, endNode]
	
	##Create the initial event list
	return createTask()
	