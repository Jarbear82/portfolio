extends Area2D

#Textures:
var bit0_texture = preload("res://images/bit0.png")
var bit1_texture = preload("res://images/bit1.png")

const DEFAULT_SPEED = 500

var _speed = DEFAULT_SPEED
var direction = Vector2.LEFT
var _bit_dir

@onready var _initial_pos = position


func _process(delta):
	_speed += delta * 2
	position += _speed * delta * direction


func reset():
	direction = Vector2.LEFT
	position = _initial_pos
	_speed = DEFAULT_SPEED


func _on_area_entered(area):
	
	if area.name == "Ldisc":
		_bit_dir = 1
	elif area.name == "Rdisc":
		_bit_dir = -1
		
		# Assign new direction
	if area.name == "Rdisc" or area.name == "Ldisc":
		direction = Vector2(_bit_dir, randf() * 2 - 1).normalized()
		
	# Enters a goal
	if area.name == "Goal0":
		Global.score0 += 1
	elif area.name == "Goal1":
		Global.score1 += 1
