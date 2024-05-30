import arcade 
from GameFunctions.Visuals.D6Faces import D6_1

SCWidth = 500
SCHeight = 130
SCTitle = "Dice"
Rad = 15

arcade.open_window(SCWidth, SCHeight, SCTitle)

arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

dice = {}
#change this to render the dice, going to need to take dice as input to display. 
#arcade.draw_rectangle_outline(center_x=100, center_y=65, color=arcade.color.BLACK, width=100, height=100, border_width=5)
arcade.sprite(filename = D6_1)
                 

arcade.finish_render()

arcade.run()