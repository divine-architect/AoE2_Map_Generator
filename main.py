from PIL import Image, ImageDraw, ImageFont
import json

# Load JSON data from a file
with open("output.json", "r") as file:
    data = json.load(file)

map_width = 120
map_height = 120
tile_width = 5
tile_height = 5
dirt_color = (228,162,82)  # Brown color
new_color = (51, 151, 39)  # #339727 color
dot_radius = 4
water_color =  	(0, 105, 148)
beach_color = (223, 175, 124)
# Calculate the overall image size
image_width = map_width * tile_width
image_height = map_height * tile_height

# Create a new image
minimap = Image.new("RGB", (image_width, image_height))
font = ImageFont.load_default()
draw = ImageDraw.Draw(minimap)

# Fill the image based on terrain values
for tile in data["map"]["tiles"]:
    x_tile = tile["position"]["x"] * tile_width
    y_tile = tile["position"]["y"] * tile_height

    if tile["terrain"] == 6 or tile["terrain"] ==11 or tile["terrain"]==25:
        color = dirt_color
    elif tile["terrain"] == 1:
        color = water_color
    elif tile["terrain"] == 2:
        color = beach_color
    else:
        color = new_color

    draw.rectangle([x_tile, y_tile, x_tile + tile_width, y_tile + tile_height], fill=color)

# Draw a highlighted dot at player positions with "TC" label
for player in data["players"]:
    player_x = int(player["position"]["x"] * (image_width / map_width))
    player_y = int(player["position"]["y"] * (image_height / map_height))
    draw.ellipse((player_x - dot_radius, player_y - dot_radius, player_x + dot_radius, player_y + dot_radius), fill=player["color"])
    
    # Label the player with "TC"
    draw.text((player_x - 10, player_y - 10), "TC", fill="white", font=font)

# Tilt the image left by 45 degrees
minimap = minimap.rotate(45, expand=True)

# Save the minimap as an image
minimap.save("minimap_tilted_with_labeled_dots.png")

# Show the tilted minimap (optional)
minimap.show()
