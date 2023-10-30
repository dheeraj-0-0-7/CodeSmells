def calculate_area(length, width):
    return length * width

def calculate_perimeter(length, width):
    return 2 * (length + width)

def calculate_volume(length, width, height):
    return calculate_area(length, width) * height

def calculate_surface_area(length, width, height):
    base_area = calculate_area(length, width)
    lateral_area = 2 * (length * height + width * height)
    return 2 * base_area + lateral_area
