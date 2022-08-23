# Dimensions of the display window measured in pixels
size(500, 500)

print('Hello, world!') #Writes hello world to the console area.

background("#004477")

# Stroke
stroke("#FFFFFF")
strokeWeight(3)

fill('#FF0000')
rect(100, 150, 200, 300) # x, y, width, height

# Small red rectangle
rect(10, 15, 20, 30)

# Orange square
fill("#FF9900")
rect(50, 100, 150, 150)

# Fill-less square
noFill()
square(250, 100, 150)
