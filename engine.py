# add local PATH
import os

gtkhome = "GTK3-Runtime Win64\\bin"
os.environ["PATH"] = gtkhome + ";" + os.environ["PATH"]

# import necessary libraries
import cairosvg
from xml.etree import ElementTree as ET
from tqdm import tqdm
from PIL import Image
import json

# import local functions
from scripts import util
from scripts import rule
from scripts.svgmerger import NewSVG

# exclude the namespace
ET.register_namespace("", "http://www.w3.org/2000/svg")

def create_config(output_path="source\\config.json"):
    if not os.path.exists(output_path):
        config = {
            "project_name": "Project Name",
            "description": "Project Description",
            "dimension":{
                "width": 700,
                "height": 700
            }
        }
        json.dump(config,open(output_path,"w"),indent=4)

def layers_merger(source_path="layers", size_type="default"):

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
                "attribute_name": "_".join(file.split("_")[1:]).replace(".png",""),
                "path": img
            }
            layers.append(layer)
        layers = sorted(layers, key=lambda x: x['sequence'])
        return layers
    
    output_path = "source"
    util.check_folder(output_path)

    images = find_images(source_path)
    layers = find_layers(source_path)

    if size_type == "default":
        
        for filepath in images:
            img = Image.open(filepath)
            default_size = img.width, img.height
            break
        
        svg = NewSVG(size=default_size)
        
    elif size_type == "custom":
        
        svg = NewSVG(size=(700,700))
    
    attributes = {}
    for index,layer in enumerate(layers):
        svg.add_image(index, layer)

        trait_type = layer['attribute_name'].split("_")[0]
        value = layer['attribute_name'].split("_")[1]
        try: attributes[trait_type].append(value)
        except: attributes[trait_type] = [value]

    json.dump(attributes,open("source\\attributes.json","w"),indent=4)

    probability = {}
    for trait_type in attributes:
        probs = {k:1.0 for k in attributes[trait_type]}
        probability.update({trait_type: probs})
    
    json.dump(probability,open("source\\probability.json","w"),indent=4)

    create_config(output_path="source\\config.json")
    svg.save(file_path="source\\source.svg")

def generator(number=10, output_path=None, file_name=""):
    def metadata2list(metadata):
        return [f"{k}_{v}" for k, v in metadata.items() if v != "NOTHING"]

    # read the config file
    config = json.load(open("source\\config.json"))

    # define the empty variable
    uniques = []
    metadata = []
    number = int(number) # make sure the number variable is integer
    while len(metadata) < number:

        # read the attributes file
        attributes = json.load(open("source\\attributes.json"))

        # random generate the combination
        instance = {}
        for trait_type in attributes:
            item = rule.choose(attributes, trait_type)
            instance.update({trait_type: item})

        # collect the instance
        instance_str = ",".join(instance.values())
        if instance_str not in uniques:
            uniques.append(instance_str)
            metadata.append(instance)

    # dump the metadata
    metadata_path = os.path.join(output_path,"metadata.json")
    json.dump(metadata, open(metadata_path, "w"), indent=4)
    util.create_metadata(metadata, output_path)

    # export the artworks based on metadata
    i = 0
    file_name = os.path.join(output_path, str(file_name) + "{}.png")
    for j in tqdm(metadata, desc=f"Rendering {len(metadata)} {config['project_name']}", ncols=100):

        # read the svg file
        tree = ET.parse(open("source\\source.svg"))
        root = tree.getroot()

        # apply the metadata
        for element in root.iter():
            if element.tag.split("}")[-1] == "g":
                label = element.get("{http://www.inkscape.org/namespaces/inkscape}label")
                if label in metadata2list(j):
                    style = element.get("style")
                    new_style = style.replace("display:none", "display:inline")
                    element.set("style", new_style)

        # export the ballz
        tree.write("source\\exported.svg", xml_declaration=True)

        # export the svg into png
        cairosvg.svg2png(url="source\\exported.svg", write_to=file_name.format(i+1))
        i += 1

    # remove the export file
    os.remove("source\\exported.svg")
    os.remove(metadata_path)


if __name__ == "__main__":

    project_folder = os.path.join("project","example")
    util.check_folder(project_folder)

    metadata_folder = os.path.join(project_folder,"metadata")
    util.check_folder(metadata_folder)

    generator(output_path=project_folder)