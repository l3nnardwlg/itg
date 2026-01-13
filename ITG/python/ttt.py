import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(10)
t.left(90)  # Point upwards for the tree
t.color("brown")  # Trunk color

def tree(size):
    if size < 5:
        return
    t.forward(size)
    t.right(20)
    tree(size * 0.7)
    t.left(40)
    tree(size * 0.7)
    t.right(20)
    t.backward(size)

# Start drawing the tree
tree(100)

# Optional: Add some leaves at the top
t.color("green")
t.begin_fill()
t.circle(20)
t.end_fill()

turtle.done()
