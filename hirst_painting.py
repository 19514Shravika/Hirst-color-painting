import colorgram
colors=colorgram.extract('Hirst-severed-spots.jpg',20)
rgb_colors=[]
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    result=(r,g,b)
    rgb_colors.append(result)
print(rgb_colors)