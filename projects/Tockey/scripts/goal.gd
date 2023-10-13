extends Area2D

# var score1 = get_node("/root/tockey/User1Label/Score1")
#var score2 = PROPERTY_USAGE_STORE_IF_NULL

func _on_goal_area_entered(area):
	if area.name == "Bit":
		area.reset()
		# Update Score
		if name == "Goal0":
			get_node("Score")
		elif name == "Goal1":
			get_node("Score2")
