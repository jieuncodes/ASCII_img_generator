from PIL import Image

def image_to_ascii(image_path, output_width=80):
    # Load the image
    image = Image.open(image_path)

    # Calculate aspect ratio
    aspect_ratio = float(image.height) / float(image.width)

    # Calculate new height based on aspect ratio and desired output width
    output_height = int(output_width * aspect_ratio)

    # Resize the image
    image = image.resize((output_width, output_height))

    # Convert the image to grayscale
    image = image.convert("L")

    # Define ASCII characters
    ascii_characters = "@%#*+=-:. "

    # Map grayscale pixels to ASCII characters
    ascii_image = []
    for row in range(output_height):
        ascii_row = []
        for col in range(output_width):
            gray_value = image.getpixel((col, row))
            index = int(gray_value / 255 * (len(ascii_characters) - 1))
            ascii_row.append(ascii_characters[index])
        ascii_image.append("".join(ascii_row))

    return "\n".join(ascii_image)

# Example usage:
image_path = "profile.jpg"
ascii_art = image_to_ascii(image_path)
print(ascii_art)
