extends Area2D


@export var _bounce_direction = 1


func _on_wall_area_entered(area):
	if area.name == "Bit":
		if name == "TopWall" or name == "BottomWall":
			area.direction = (area.direction + Vector2(0, _bounce_direction)).normalized()
		elif name == "LeftWall":
			area.direction = (area.direction + Vector2(_bounce_direction, 0).normalized())
		elif name == "RightWall":
			area.direction = (area.direction - Vector2(_bounce_direction, 0).normalized())
