# import turtle
# import time
# pen = turtle.Turtle()
# pen.color('red')
# pen.begin_fill()
# pen.pensize(3)
# pen.left(50)
# pen.forward(133)
# pen.circle(50, 200)
# pen.right(140)
# pen.circle(50, 200)
# pen.forward(133)
# pen.end_fill()
# time.sleep(10)

# Import turtle package
import turtle
import time

# Creating a turtle object(pen)
pen = turtle.Turtle()

# Defining a method to draw curve
def curve():
	for i in range(200):

		# Defining step by step curve motion
		pen.right(1)
		pen.forward(1)

# Defining method to draw a full heart
def heart():

	# Set the fill color to red
	pen.fillcolor('red')

	# Start filling the color
	pen.begin_fill()

	# Draw the left line
	pen.left(140)
	pen.forward(113)

	# Draw the left curve
	curve()
	pen.left(120)

	# Draw the right curve
	curve()

	# Draw the right line
	pen.forward(112)

	# Ending the filling of the color
	pen.end_fill()

# Defining method to write text
def txt():

	# Move turtle to air
	pen.up()

	# Move turtle to a given position
	pen.setpos(-68, 95)

	# Move the turtle to the ground
	pen.down()

	# Set the text color to lightgreen
	pen.color('white')

	# Write the specified text in
	# specified font style and size
	pen.write("Happy Val's Day", font=(
	"Verdana", 12, "bold"))


# Draw a heart
heart()

# Write text
txt()
time.sleep(1)
# To hide turtle
pen.ht()
