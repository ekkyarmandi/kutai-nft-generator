from scripts import utils
from scripts import rule

import json
import os

import time

class KutaiEngine:

    attributes = probabilities = {}

    def read_layers(self, project_path):

        # read the layers files
        layers_path = os.path.join("project",project_path,"layers")
        settings_path = os.path.join("project",project_path,"settings")

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

        print("attributes.json and probabilities.json has been created.")

    def update_attributes(self, project_path):
        settings_path = os.path.join("project",project_path,"settings")
        self.attributes = json.load(open(os.path.join(settings_path,"attributes.json")))
        self.probabilities = json.load(open(os.path.join(settings_path,"probabilities.json")))
        self.config = json.load(open(os.path.join(settings_path,"config.json")))

    def generate_metadata(self, number, path):

        # record the timestamp
        start = time.time()
        
        # read all files in settings folder
        self.update_attributes(path)

        # define the output folder
        project_path = os.path.join("project",path,"output")
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
            path
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
    engine.update_attributes("example")
    engine.generate_metadata(
        number=10,
        path="example"
    )