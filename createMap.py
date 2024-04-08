import os
from PIL import Image, ImageDraw

def createMap(folder_path, target_tile_name):
    tile_size = 100

    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    image_files = sorted(image_files, key = lambda x: int(x.split('.')[0]))
    tiles_per_row = int(len(image_files) ** 0.5)
    if tiles_per_row * tiles_per_row < len(image_files):
        tiles_per_row += 1

    image_size = tiles_per_row * tile_size

    combined_image = Image.new("RGB", (image_size, image_size), "white")

    draw = ImageDraw.Draw(combined_image)

    for i, image_file in enumerate(image_files):
        image = Image.open(os.path.join(folder_path, image_file))
        image = image.resize((tile_size, tile_size), Image.ANTIALIAS)
        x = (i % tiles_per_row) * tile_size
        y = (i // tiles_per_row) * tile_size
        combined_image.paste(image, (x, y))

    target_tile_index = int(target_tile_name.split('.')[0]) - 1
    target_tile_x = (target_tile_index % tiles_per_row) * tile_size
    target_tile_y = (target_tile_index // tiles_per_row) * tile_size
    draw.rectangle([target_tile_x, target_tile_y, target_tile_x + tile_size - 1, target_tile_y + tile_size - 1],
                   outline="red", width=5)

    combined_image.save("combined_image_with_border.png")


createMap("/drive/MyDrive/map_data_n_png", "24.png")
