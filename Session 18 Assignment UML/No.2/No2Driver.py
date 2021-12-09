from No2Class import Circle
from No2Class import Cylinder

def main():
    data = Cylinder(1.0, "red", 1.0)
    print(f"Cylinder Radius = {'{:.1f}'.format(data.getRadius())}")
    print(f"Cylinder Height = {'{:.1f}'.format(data.getHeight())}")
    print(f"Cylinder Area = {'{:.1f}'.format(data.getArea())}")
    print(f"Cylinder Volume = {'{:.1f}'.format(data.getVolume())}")
    print(f"Cylinder Color = {data.getColor()}")
    data.setRadius(3)
    data.setColor("Black")
    data.setHeight(7)
    print()
    print("An updated data: ")
    print(f"Cylinder Radius = {'{:.1f}'.format(data.getRadius())}")
    print(f"Cylinder Height = {'{:.1f}'.format(data.getHeight())}")
    print(f"Cylinder Area = {'{:.1f}'.format(data.getArea())}")
    print(f"Cylinder Volume = {'{:.1f}'.format(data.getVolume())}")
    print(f"Cylinder Color = {data.getColor()}")
main()