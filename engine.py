from scripts import utils
from scripts import rule
from PIL import Image
from tqdm import tqdm
import json
import time
import os

class KutaiEngine:

    attributes = {}
    probabilities = {}

    def read_layers(self, project_path):

        # read the layers files
        layers_path = os.path.join(project_path,"layers")
        settings_path = os.path.join(project_path,"settings")

        # create attributes and probabilites files
        layers = find_layers(layers_path)

        for layer in layers:
            trait_type = layer['attribute_name'].split("_")[0]
            value = layer['attribute_name'].split("_")[1]
            try: self.attributes[trait_type].append(value)
            except: self.attributes[trait_type] = [value]

        for trait_type in self.attributes:
            probs = {k:1.0 for k in self.attributes[trait_type]}
            self.probabilities.update({trait_type: probs})
        
        json.dump(
            self.attributes,
            open(os.path.join(settings_path,"attributes.json"), "w"),
            indent=4
        )
        
        json.dump(
            self.probabilities,
            open(os.path.join(settings_path,"probabilities.json"), "w"),
            indent=4
        )

        print("settings\\attributes.json and settings\\probabilities.json has been created")

    def update_attributes(self, project_path):
        settings_path = os.path.join(project_path,"settings")
        self.attributes = json.load(open(os.path.join(settings_path,"attributes.json")))
        self.probabilities = json.load(open(os.path.join(settings_path,"probabilities.json")))
        self.config = json.load(open(os.path.join(settings_path,"config.json")))

    def generate_metadata(self, number, project_path, output_path):

        # read all files in settings folder
        start = time.time()
        self.update_attributes(project_path)

        # define the output folder
        project_path = os.path.join(project_path,"output",output_path)
        utils.check_folder(project_path)

        # define the metadata folder
        metadata_path = os.path.join(project_path,"metadata")
        utils.check_folder(metadata_path)

        # define the backup folder
        backup_path = os.path.join(project_path,"backup")
        utils.check_folder(backup_path)

        # iterate the loop
        self.metadata, uniques = [], []
        while len(self.metadata) < int(number):
            model = {}
            for key in self.attributes:
                model.update(
                    {key: self.choose(key)}
                )
            model_string = ",".join(model.values())
            if model_string not in uniques:
                self.metadata.append(model)
                uniques.append(model_string)

        # dump the metadata into backup folder
        json.dump(
            self.metadata,
            open(os.path.join(backup_path,"metadata.json"), "w"),
            indent=4
        )

        # create all metadata
        utils.create_metadata(
            self.metadata,
            self.config,
            metadata_path
        )

        # print out message
        end = time.time()
        print(number,f"metadata has been generated ({end-start:.2f} sec)")

    def choose(self, key):
        item = rule.choose(
            self.attributes,
            self.probabilities,
            key
        )
        return item

    def export(self, project_path, output_path):

        # read config file
        project_path = os.path.join(project_path)
        config = json.load(open(os.path.join(project_path,"settings","config.json")))
        self.size = (
            config['dimension']['width'],
            config['dimension']['height'],
        )
        
        # read metadata file
        output_path = os.path.join(project_path,"output",output_path)
        metadata = json.load(open(os.path.join(output_path,"backup","metadata.json")))

        # read all layers file
        self.layers = find_layers(os.path.join(project_path,"layers"))

        # merge all images
        i = 1
        for model in tqdm(metadata,"Exporting the Images"):

            # merge all the images
            img = self.model2images(model)

            # save the image
            file_name = os.path.join(output_path,str(i)+".png")
            img.save(file_name)
            i += 1

    def model2images(self, model):
        
        # collect images path based on model
        images = []
        for m in model:
            key, value = m, model[m]
            trait = "_".join([str(key),str(value)])
            for l in self.layers:
                if trait in l['attribute_name']:
                    images.append(l)
        images_path = sorted(images, key=lambda x: x['sequence'])
        images_path = [x['path'] for x in images_path]
        
        # merge the images
        for i,p in enumerate(images_path):
            if i == 0:
                img = Image.open(p).resize(size=self.size).convert("RGBA")
            else:
                top = Image.open(p).resize(size=self.size).convert("RGBA")
                img = Image.alpha_composite(img,top)
        
        return img.convert("RGB")

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

if __name__ == "__main__":

    engine = KutaiEngine()
    engine.export(
        project_path="example",
        output_path="sample"
    )