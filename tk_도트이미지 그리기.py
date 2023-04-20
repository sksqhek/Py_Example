from tkinter import Canvas, Tk

# initialize window
gui = Tk()
the_canvas = Canvas(gui, width=600, height=600, background='light blue',
                    scrollregion="0 -600 600 0")
the_canvas.pack()


def make_square(a_canvas, bottom_left, width, color="white"):
    a_canvas.create_rectangle(
        (bottom_left[0], bottom_left[1]),
        (bottom_left[0] + width, bottom_left[1] + width),
        fill=color)


########################## YOUR CODE BELOW THIS LINE ##############################
clothes = "purple"
accessories = "saddle brown"
tone = "bisque3"
features = "black"
# task 1
overalls = "pink"

# task 2
pixel = 35


# task 3

def get_xy(origin, pixel_size, mario_coord):
    x = origin[0]  # extract the x-coordinate
    y = origin[1]  # extract the y-coordinate

    row = mario_coord[0]  # extract the row number
    col = mario_coord[1]  # extract the col number

    new_x = x + row * pixel_size  # calculate the new x
    new_y = y + col * pixel_size  # calculate the new y

    return (new_x, new_y)  # add this line to return the new x and y values


origin = (0, 0)
x = origin[0]
y = origin[1]


# task 4
def make_mario(a_canvas, bottom_left, pixel=25, clothes="red", overalls="blue"):
    make_square(the_canvas, get_xy(origin, pixel, (3, 14)), pixel, color=clothes)  # pixel (3, 14)
    make_square(the_canvas, get_xy(origin, pixel, (4, 14)), pixel, color=clothes)  # pixel (4, 14)
    make_square(the_canvas, get_xy(origin, pixel, (5, 14)), pixel, color=clothes)  # pixel (5, 14)
    make_square(the_canvas, get_xy(origin, pixel, (6, 14)), pixel, color=clothes)  # pixel (6, 14)
    make_square(the_canvas, get_xy(origin, pixel, (7, 14)), pixel, color=clothes)  # pixel (7, 14)
    make_square(the_canvas, get_xy(origin, pixel, (8, 14)), pixel, color=clothes)  # pixel (8, 14)
    make_square(the_canvas, get_xy(origin, pixel, (3, 14)), pixel, color=clothes)  # pixel (3, 14)
    make_square(the_canvas, get_xy(origin, pixel, (4, 14)), pixel, color=clothes)  # pixel (4, 14)
    make_square(the_canvas, get_xy(origin, pixel, (5, 14)), pixel, color=clothes)  # pixel (5, 14)
    make_square(the_canvas, get_xy(origin, pixel, (6, 14)), pixel, color=clothes)  # pixel (6, 14)
    make_square(the_canvas, get_xy(origin, pixel, (7, 14)), pixel, color=clothes)  # pixel (7, 14)
    make_square(the_canvas, get_xy(origin, pixel, (8, 14)), pixel, color=clothes)  # pixel (8, 14)
    make_square(the_canvas, get_xy(origin, pixel, (2, 13)), pixel, color=clothes)  # pixel (2, 13)
    make_square(the_canvas, get_xy(origin, pixel, (3, 13)), pixel, color=clothes)  # pixel (3, 13)
    make_square(the_canvas, get_xy(origin, pixel, (4, 13)), pixel, color=clothes)  # pixel (4, 13)
    make_square(the_canvas, get_xy(origin, pixel, (5, 13)), pixel, color=clothes)  # pixel (5, 13)
    make_square(the_canvas, get_xy(origin, pixel, (6, 13)), pixel, color=clothes)  # pixel (6, 13)
    make_square(the_canvas, get_xy(origin, pixel, (7, 13)), pixel, color=clothes)  # pixel (7, 13)
    make_square(the_canvas, get_xy(origin, pixel, (8, 13)), pixel, color=clothes)  # pixel (8, 13)
    make_square(the_canvas, get_xy(origin, pixel, (9, 13)), pixel, color=clothes)  # pixel (9, 13)
    make_square(the_canvas, get_xy(origin, pixel, (10, 13)), pixel, color=clothes)  # pixel (10, 13)
    make_square(the_canvas, get_xy(origin, pixel, (11, 13)), pixel, color=clothes)  # pixel (11, 13)
    make_square(the_canvas, get_xy(origin, pixel, (2, 12)), pixel, color=accessories)  # pixel (2, 12)
    make_square(the_canvas, get_xy(origin, pixel, (3, 12)), pixel, color=accessories)  # pixel (3, 12)
    make_square(the_canvas, get_xy(origin, pixel, (4, 12)), pixel, color=accessories)  # pixel (4, 12)
    make_square(the_canvas, get_xy(origin, pixel, (5, 12)), pixel, color=tone)  # pixel (5, 12)
    make_square(the_canvas, get_xy(origin, pixel, (6, 12)), pixel, color=tone)  # pixel (6, 12)
    make_square(the_canvas, get_xy(origin, pixel, (7, 12)), pixel, color=tone)  # pixel (7, 12)
    make_square(the_canvas, get_xy(origin, pixel, (8, 12)), pixel, color=features)  # pixel (8, 12)
    make_square(the_canvas, get_xy(origin, pixel, (9, 12)), pixel, color=tone)  # pixel (9, 12)
    make_square(the_canvas, get_xy(origin, pixel, (2, 13)), pixel, color=clothes)  # pixel (2, 13)
    make_square(the_canvas, get_xy(origin, pixel, (3, 13)), pixel, color=clothes)  # pixel (3, 13)
    make_square(the_canvas, get_xy(origin, pixel, (4, 13)), pixel, color=clothes)  # pixel (4, 13)
    make_square(the_canvas, get_xy(origin, pixel, (5, 13)), pixel, color=clothes)  # pixel (5, 13)
    make_square(the_canvas, get_xy(origin, pixel, (6, 13)), pixel, color=clothes)  # pixel (6, 13)
    make_square(the_canvas, get_xy(origin, pixel, (7, 13)), pixel, color=clothes)  # pixel (7, 13)
    make_square(the_canvas, get_xy(origin, pixel, (8, 13)), pixel, color=clothes)  # pixel (8, 13)
    make_square(the_canvas, get_xy(origin, pixel, (9, 13)), pixel, color=clothes)  # pixel (9, 13)
    make_square(the_canvas, get_xy(origin, pixel, (10, 13)), pixel, color=clothes)  # pixel (10, 13)
    make_square(the_canvas, get_xy(origin, pixel, (11, 13)), pixel, color=clothes)  # pixel (11, 13)
    make_square(the_canvas, get_xy(origin, pixel, (2, 12)), pixel, color=accessories)  # pixel (2, 12)
    make_square(the_canvas, get_xy(origin, pixel, (3, 12)), pixel, color=accessories)  # pixel (3, 12)
    make_square(the_canvas, get_xy(origin, pixel, (4, 12)), pixel, color=accessories)  # pixel (4, 12)
    make_square(the_canvas, get_xy(origin, pixel, (5, 12)), pixel, color=tone)  # pixel (5, 12)
    make_square(the_canvas, get_xy(origin, pixel, (6, 12)), pixel, color=tone)  # pixel (6, 12)
    make_square(the_canvas, get_xy(origin, pixel, (7, 12)), pixel, color=tone)  # pixel (7, 12)
    make_square(the_canvas, get_xy(origin, pixel, (8, 12)), pixel, color=features)  # pixel (8, 12)
    make_square(the_canvas, get_xy(origin, pixel, (9, 12)), pixel, color=tone)  # pixel (9, 12)
    make_square(the_canvas, get_xy(origin, pixel, (1, 11)), pixel, color=accessories)  # pixel (1, 11)
    make_square(the_canvas, get_xy(origin, pixel, (2, 11)), pixel, color=tone)  # pixel (2,11)
    make_square(the_canvas, get_xy(origin, pixel, (3, 11)), pixel, color=accessories)  # pixel (3, 11)
    make_square(the_canvas, get_xy(origin, pixel, (4, 11)), pixel, color=tone)  # pixel (4, 11)
    make_square(the_canvas, get_xy(origin, pixel, (5, 11)), pixel, color=tone)  # pixel (5, 11)
    make_square(the_canvas, get_xy(origin, pixel, (6, 11)), pixel, color=tone)  # pixel (6, 11)
    make_square(the_canvas, get_xy(origin, pixel, (7, 11)), pixel, color=tone)  # pixel (7, 11)
    make_square(the_canvas, get_xy(origin, pixel, (8, 11)), pixel, color=features)  # pixel (8, 11)
    make_square(the_canvas, get_xy(origin, pixel, (9, 11)), pixel, color=tone)  # pixel (9, 11)
    make_square(the_canvas, get_xy(origin, pixel, (10, 11)), pixel, color=tone)  # pixel (10, 11)
    make_square(the_canvas, get_xy(origin, pixel, (11, 11)), pixel, color=tone)  # pixel (11, 11)
    make_square(the_canvas, get_xy(origin, pixel, (1, 10)), pixel, color=accessories)  # pixel (1, 10)
    make_square(the_canvas, get_xy(origin, pixel, (2, 10)), pixel, color=tone)  # pixel (2, 10)
    make_square(the_canvas, get_xy(origin, pixel, (3, 10)), pixel, color=accessories)  # pixel (3, 10)
    make_square(the_canvas, get_xy(origin, pixel, (4, 10)), pixel, color=tone)  # pixel (4, 10)
    make_square(the_canvas, get_xy(origin, pixel, (5, 10)), pixel, color=tone)  # pixel (5, 10)
    make_square(the_canvas, get_xy(origin, pixel, (6, 10)), pixel, color=tone)  # pixel (6, 10)
    make_square(the_canvas, get_xy(origin, pixel, (7, 10)), pixel, color=tone)  # pixel (7, 10)
    make_square(the_canvas, get_xy(origin, pixel, (8, 10)), pixel, color=tone)  # pixel (8, 10)
    make_square(the_canvas, get_xy(origin, pixel, (9, 10)), pixel, color=features)  # pixel (9, 10)
    make_square(the_canvas, get_xy(origin, pixel, (10, 10)), pixel, color=tone)  # pixel (10, 10)
    make_square(the_canvas, get_xy(origin, pixel, (11, 10)), pixel, color=tone)  # pixel (11, 10)
    make_square(the_canvas, get_xy(origin, pixel, (12, 10)), pixel, color=tone)  # pixel (12, 10)
    make_square(the_canvas, get_xy(origin, pixel, (1, 9)), pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (2, 9)), pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (3, 9)), pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (4, 9)), pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (5, 9)), pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (6, 9)), pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (7, 9)), pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (8, 9)), pixel, color=features)
    make_square(the_canvas, get_xy(origin, pixel, (9, 9)), pixel, color=features)
    make_square(the_canvas, get_xy(origin, pixel, (10, 9)), pixel, color=features)
    make_square(the_canvas, get_xy(origin, pixel, (11, 9)), pixel, color=features)
    make_square(the_canvas, get_xy(origin, pixel, (2, 8)), pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (3, 8)), pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (4, 8)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (5, 8)), pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (6, 8)), pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (7, 8)), pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (8, 8)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (1, 7)), pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (2, 7)), pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (3, 7)), pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (4, 7)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (5, 7)), pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (6, 7)), pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (7, 7)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (8, 7)), pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (9, 7)), pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (10, 7)), pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (0, 6)), pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (1, 6)), pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (2, 6)), pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (3, 6)), pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (4, 6)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (5, 6)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (6, 6)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (7, 6)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (8, 6)), pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (9, 6)), pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (10, 6)), pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (11, 6)), pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (0, 5)), pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (1, 5)), pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (2, 5)), pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (3, 5)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (4, 5)), pixel, color='gold')
    make_square(the_canvas, get_xy(origin, pixel, (5, 5)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (6, 5)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (7, 5)), pixel, color='gold')
    make_square(the_canvas, get_xy(origin, pixel, (8, 5)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (9, 5)), pixel, color=clothes)
    make_square(the_canvas, get_xy(origin, pixel, (10, 5)), pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (11, 5)), pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (0, 4)), pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (2, 4)), pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (3, 4)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (4, 4)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (5, 4)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (6, 4)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (7, 4)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (8, 4)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (9, 4)), pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (10, 4)), pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (11, 4)), pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (0, 3)), pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (1, 3)), pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (2, 3)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (3, 3)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (4, 3)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (5, 3)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (6, 3)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (7, 3)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (8, 3)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (9, 3)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (10, 3)), pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (11, 3)), pixel, color=tone)
    make_square(the_canvas, get_xy(origin, pixel, (2, 2)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (3, 2)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (4, 2)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (7, 2)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (8, 2)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (9, 2)), pixel, color=overalls)
    make_square(the_canvas, get_xy(origin, pixel, (0, 1)), pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (1, 1)), pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (2, 1)), pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (3, 1)), pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (6, 1)), pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (7, 1)), pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (8, 1)), pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (9, 1)), pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (0, 0)), pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (1, 0)), pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (2, 0)), pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (3, 0)), pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (4, 0)), pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (6, 0)), pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (7, 0)), pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (8, 0)), pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (9, 0)), pixel, color=accessories)
    make_square(the_canvas, get_xy(origin, pixel, (10, 0)), pixel, color=accessories)


# After you're done making your "make_mario" function, invoke it as follows:
make_mario(the_canvas, (0, 9))
# make_mario(the_canvas, (420, 250), clothes='#E0607E', pixel=10)
# make_mario(the_canvas, (55, 415), clothes='green', pixel=15)
# make_mario(the_canvas, (350, 115), pixel=5, clothes='#75B9BE')
# make_mario(the_canvas, (420, 400), clothes='#E5F77D', overalls='#75B9BE', pixel=15)
# make_mario(the_canvas, (420, 10), pixel=15)


##

########################## YOUR CODE ABOVE THIS LINE ##############################
# helper function that draws a grid.
def make_grid(c, w, h):
    interval = 100
    # Creates all vertical lines at intevals of 100
    for i in range(0, w, interval):
        c.create_line(i, 0, i, h, tag='grid_line')
    # Creates all horizontal lines at intevals of 100
    for i in range(0, h, interval):
        c.create_line(0, i, w, i, tag='grid_line')
    # Creates axis labels
    offset = 2
    for y in range(0, h, interval):
        for x in range(0, w, interval):
            c.create_oval(
                x - offset,
                y - offset,
                x + offset,
                y + offset,
                fill='black'
            )
            c.create_text(
                x + offset,
                y + offset,
                text="({0}, {1})".format(x, y),
                anchor="nw",
                font=("Purisa", 8)
            )


make_grid(the_canvas, 600, 600)  # draw the grid

the_canvas.scale("all", 0, 0, 1, -1)
the_canvas.mainloop()