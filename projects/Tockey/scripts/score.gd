extends Node

func _process(delta):
	if name == "User0Score":
		self.text = "User 0 : " + str(Global.score0)
	if name == "User1Score":
		self.text = "User 1 : " + str(Global.score1)
