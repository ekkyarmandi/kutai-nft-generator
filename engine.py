import sys
import os
from turtle import width

from PIL import Image

from scripts import util
from scripts.svgmerger import SourceSVG


def source_compiler(source_path="layers", size_type="default"):

    def find_images(path):
        images_path = []
        for root, _, files in os.walk(path):
            for file in files:
                if file.lower().endswith("png"):
                    file_path = os.path.join(root,file)
                    images_path.append(file_path)
        return images_path

    def find_layers(path):
        layers = []
        images = find_images(path)
        for img in images:
            file = img.split("\\")[-1]
            layer = {
                "sequence": int(file.split("_")[0]),
                "trait_name": "_".join(file.split("_")[1:]).replace(".png",""),
                "path": img
            }
            layers.append(layer)

        sequences = sorted(layers, key=lambda x: x['sequence'])
        return layers, sequences
    
    output_path = "source"
    util.check_folder(output_path)

    images = find_images(source_path)
    layers, sequences = find_layers(source_path)

    if size_type == "default":
        
        for filepath in images:
            img = Image.open(filepath)
            default_size = img.width, img.height
            break
        
        svg = SourceSVG(size=default_size)
        
    elif size_type == "custom":
        
        svg = SourceSVG(size=(700,700))
        
    for img in layers:
        svg.add_image(img)

if __name__ == "__main__":

    # if sys.argv[1] == "generate":
    #     pass
    # elif sys.argv[1] == "count_max":
    #     pass

    source_compiler()