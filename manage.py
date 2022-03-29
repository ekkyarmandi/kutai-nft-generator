import json
import os

import argparse

from scripts import utils
from engine import KutaiEngine

engine = KutaiEngine()

parser = argparse.ArgumentParser(description='Artwork Random Generative Engine')

commands = [
    "startproject",
    "read_layers",
    "update_attributes",
    "generate"
]

parser.add_argument(
    "command",
    type=str,
    choices=commands,
    help="Main command line"
)

parser.add_argument(
    "-n", "--number",
    type=int,
    default=10,
    help="Number of generated output"
)

parser.add_argument(
    "-s", "--size-type",
    type=str,
    choices=["default","custom"],
    default="default",
    help="Size custom width and height"
)

parser.add_argument(
    "-p", "--path",
    type=str,
    default="project\\example",
    help="Project path folder"
)

args = parser.parse_args()

if args.command == "startproject":
    
    # create project folder
    project_path = os.path.join("project",args.path)
    utils.check_folder(project_path)

    # create sub folders
    sub_folders = [
        "layers",
        "output",
        "settings"
    ]
    for sub in sub_folders:
        sub_path = os.path.join(project_path,sub)
        utils.check_folder(sub_path)

    # create config file
    config = {
        "projec_name": "Your project name",
        "description": "Your project description",
        "external_url": "https://www.example.com",
        "ipfs_cid": "",
        "filename_prefix": "",
        "dimension": {
            "width": 0,
            "height": 0,
        }
    }
    json.dump(
        config,
        open(os.path.join(project_path,"settings\\config.json"), "w"),
        indent=4
    )

    # print out the message
    print(project_path,"has been created")

elif args.command == "read_layers":
    engine.read_layers(args.path)

elif args.command == "update_attributes":
    engine.update_attributes(args.path)

elif args.command == "generate":
    engine.generate_metadata(
        number=args.number,
        path=args.path
    )
