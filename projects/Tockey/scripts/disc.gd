extends Area2D



const MOVE_SPEED = 500

var _up
var _down
var _right
var _left

@onready var _screen_size_y = get_viewport_rect().size.y
@onready var _screen_size_x = get_viewport_rect().size.x


func _ready():
	var n = "left"
		
	if name == "Rdisc":
		n = "right"
	else:
		n = "left"

	_up    = n + "_move_up"
	_down  = n + "_move_down"
	_right = n + "_move_right"
	_left  = n + "_move_left"


func _process(delta):
	# Move up and down based on input.
	var y_input = Input.get_action_strength(_down) - Input.get_action_strength(_up)
	position.y = clamp(position.y + y_input * MOVE_SPEED * delta, 16, _screen_size_y - 16)
	var x_input = Input.get_action_strength(_right) - Input.get_action_strength(_left)
	position.x = clamp(position.x + x_input * MOVE_SPEED * delta, 16, _screen_size_x - 16)
