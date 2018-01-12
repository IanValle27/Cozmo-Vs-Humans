class Search:
	'''Look around for players and determine how many to add'''
	searching = false
	
	def __init__(self, robot):
		self.robot = robot
		
	def LookForPlayers():
		face = None
	
		while True:
			if face and face.is_visible:
				self.robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()
			else:
				self.robot.set_head_angle(0).wait_for_completed()
			
					try:
						face = self.robot.world.wait_for_observed_face(timeout=30)
					except asyncio.TimeoutError:
						print("Didn't find a face.")
						return
				
				time.sleep(.1)