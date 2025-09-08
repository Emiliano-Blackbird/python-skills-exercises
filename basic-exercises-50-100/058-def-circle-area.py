import math


def circle_area(radius):
    """Calculate the area of a circle given its radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    return math.pi * radius ** 2


result = circle_area(5)
print(f"El área del círculo de radio 5 es: {result}")
