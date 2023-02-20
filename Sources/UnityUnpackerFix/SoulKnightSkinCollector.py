import os
import shutil

master_dir = r"C:\Users\xsbug\OneDrive\Desktop\SK503\Assets\Resources\skin\character"
output_dir = r"C:\Users\xsbug\OneDrive\Desktop\SK503\Assets\Resources\skin\character-all"

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# Depth 1
for character in os.listdir(master_dir):
    if '.' not in character:
        character_dir = os.path.join(master_dir, character)
        # Depth 2
        for skin in os.listdir(character_dir):
            if '.' not in skin:
                skin_dir = os.path.join(character_dir, skin)
                # Depth 3 (skins)
                for character_skin in os.listdir(skin_dir):
                    if character in character_skin and character_skin.endswith('.png'):
                        skin_path = os.path.join(skin_dir, character_skin)
                        # Move to output dir
                        shutil.copyfile(skin_path, os.path.join(output_dir, character_skin))
