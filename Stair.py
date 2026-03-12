import turtle

width_stair = 24
angle_stair = 90

t = turtle.Turtle()

def draw_stair(num_stair):
    """Draw a staircase with num_stair steps."""
    for i in range(num_stair):
        t.forward(width_stair)
        t.left(angle_stair)
        t.forward(width_stair)
        t.right(angle_stair)

def main():
    draw_stair(30)  # Draw 30 stairs
    turtle.done()

if __name__ == "__main__":
    main()
