class Player:
	"""Maintains Player's faces, name and score"""
	
	kind = 'human'
	searching = false
	
	def __init__(self, name):
		self.name = name
		self.points = int()
		
		
		