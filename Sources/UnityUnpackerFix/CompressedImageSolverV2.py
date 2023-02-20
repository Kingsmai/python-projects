import yaml


# =========================================================
# Read sprite slice information
# =========================================================
def open_meta_file(file_path):
    sprites = {}
    with open(file_path, 'r', encoding='utf-8') as file_stream:
        sprite_infos = yaml.safe_load(file_stream)
        sprite_infos = sprite_infos['TextureImporter']
        sprite_infos = sprite_infos['spriteSheet']
        sprite_infos = sprite_infos['sprites']
        for sprite_info in sprite_infos:
            rect_info = sprite_info['rect']
            sprites[sprite_info['name']] = {
                'x': rect_info['x'],
                'y': rect_info['y'],
                'width': rect_info['width'],
                'height': rect_info['height']
            }
        print('Sprite info read.')
    return sprites

# =========================================================
# Slice the sprite to new file
# =========================================================
