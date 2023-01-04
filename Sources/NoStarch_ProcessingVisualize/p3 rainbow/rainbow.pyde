size(600, 300)

backgroundColor = '#004477'

background(backgroundColor)

noStroke()

colors = [
    (255, 0, 0),
    (255, 127, 0),
    (255, 255, 0),
    (0, 255, 0),
    (0, 255, 255),
    (0, 0, 255),
    (127, 0, 255),
]

centerX = 600 / 2
centerY = 300

ellipseSize = 600

for color in colors:
    fill(color[0], color[1], color[2])
    ellipse(centerX, centerY, ellipseSize, ellipseSize)
    ellipseSize -= 50
    
    
fill(backgroundColor)
ellipse(centerX, centerY, ellipseSize, ellipseSize)
