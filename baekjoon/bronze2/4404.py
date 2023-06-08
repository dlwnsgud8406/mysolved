import math


def can_gopher_escape(gopher_x, gopher_y, dog_x, dog_y, gopher_holes):
    gopher_speed = 1.0  # Assuming a fixed gopher speed of 1 meter per second

    for hole_x, hole_y in gopher_holes:
        distance = math.sqrt((gopher_x - hole_x) ** 2 + (gopher_y - hole_y) ** 2)
        gopher_time = distance / gopher_speed
        dog_time = distance / (2 * gopher_speed)

        if gopher_time < dog_time:
            return f"The gopher can escape through the hole at ({hole_x:.3f},{hole_y:.3f})."

    return "The gopher cannot escape."


# Example usage
gopher_x, gopher_y, dog_x, dog_y = map(float, input().split())
gopher_holes = []

while True:
    try:
        hole_x, hole_y = map(float, input().split())
        gopher_holes.append((hole_x, hole_y))
    except EOFError:
        break

result = can_gopher_escape(gopher_x, gopher_y, dog_x, dog_y, gopher_holes)
print(result)
