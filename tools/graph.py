from PIL import Image,ImageDraw
w,h = 1000,1000
img = Image.new("RGB",(w,h),"black")
draw = ImageDraw.Draw(img)
f = open("dataset", "r")
datapoints = f.read()
f.close()
point_array = datapoints.split("\n")
point_array.pop()
i = 1
scaling =  input("Scaling: ")
spacing = input("Spacing: ")
while i - 1  < len(point_array):
    point_distance = point_array[i - 1]
    point_distance = int(point_distance)
    point_distance = point_distance -int(scaling)
    x_coordinate = i +int(spacing)
    draw.point((point_distance, x_coordinate), fill="white")
    i = i + 1
img.save("graph.jpg")