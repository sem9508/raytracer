from PIL import Image

def calc_reflection(normal, incoming):
    dot_product = incoming * normal
    return (incoming - normal * 2 * dot_product)

def clamp_color(color):
    return int(min(255, max(0, color)))

def save_image(image, width, height, filename="output.png", format="PNG"):
    img = Image.new("RGB", (width, height))
    for y in range(height):
        for x in range(width):
            color = image[y][x]
            r, g, b = clamp_color(color.x), clamp_color(color.y), clamp_color(color.z)
            img.putpixel((x, y), (r, g, b))
    img.save(filename, format=format)