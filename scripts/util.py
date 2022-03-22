import os
import re
import json

def check_folder(path):
    path = [p for p in path.split("\\") if "." not in p]
    path = os.path.join(*path)
    if not os.path.exists(path):
        os.makedirs(path)

def create_metadata(metadata, output_path):

    # create metadata folder
    output_path = os.path.join(output_path,"metadata")

    # define the configuration data
    config = json.load(open("source\\config.json"))
    project_name = config['project_name']
    description = config['description']

    # reformat metadata in a better way
    all_metadata = []
    for i,m in enumerate(metadata):
        model = {
            "name": " ".join([project_name,"#"+str(i+1)]),
            "description": description,
            "image": str(i+1) + ".png",
            "attributes": []
        }
        for trait_type,value in m.items():
            if value != "None":
                item = {
                    "trait_type": trait_type,
                    "value": value
                }
                model['attributes'].append(item)
        all_metadata.append(model)
        
        # write the individual metadata
        json.dump(model,open(os.path.join(output_path,str(i+1))+".json","w"),indent=4)

    # write all metadata
    json.dump(all_metadata,open(os.path.join(output_path,"_metadata.json"),"w"),indent=4)