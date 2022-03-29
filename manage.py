import json
import os

import argparse
from this import d

from scripts import utils
from engine import KutaiEngine

engine = KutaiEngine()

parser = argparse.ArgumentParser(description='Artwork Random Generative Engine')

subparser = parser.add_subparsers(title="Main command lines")

starting = subparser.add_parser(
    "startproject",
    help="Create your project directory"
)
starting.add_argument(
    "startproject",
    action="store_true",
    default=False
)
starting.add_argument(
    "project_path",
    help="Your project path destination"
)

read = subparser.add_parser(
    "read_layers",
    help="Read layers project directory"
)
read.add_argument(
    "read_layers",
    action="store_true",
    default=False
)
read.add_argument(
    "-p", "--path",
    type=str,
    default="layers",
    help="Project path"
)

generate = subparser.add_parser(
    "generate",
    help="Generate project metadata"
)
generate.add_argument(
    "generate",
    action="store_true",
    default=False
)
generate.add_argument(
    "number",
    metavar="NUMBER",
    type=int,
    help="Desired output"
)
generate.add_argument(
    "-o","--output",
    default="output\\example",
    help="Metadata output destination path"
)

export = subparser.add_parser(
    "export",
    help="Export images based on metadata"
)
export.add_argument(
    "export",
    action="store_true",
    default=False
)
export.add_argument(
    "-o","--output",
    default="output\\example",
    help="Metadata output destination path"
)

# parser.add_argument(
#     "-s", "--size-type",
#     type=str,
#     choices=["default","custom"],
#     default="default",
#     help="Size custom width and height"
# )

args = parser.parse_args()

print(args)

if args.startproject:
    
    # create project folder
    if args.project_path == ".":
        project_path = ""
    else:
        project_path = args.project_path
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
        "project_name": "Your project name",
        "description": "Your project description",
        "external_url": "https://www.example.com",
        "ipfs_cid": "",
        "filename_prefix": "",
        "dimension": {"width": 0, "height": 0}
    }
    json.dump(
        config,
        open(os.path.join(project_path,"settings\\config.json"), "w"),
        indent=4
    )

    # print out the message
    print(project_path,"has been created")

elif args.read_layers:
    engine.read_layers(args.path)

elif args.generate:
    engine.generate_metadata(
        number=args.number,
        project_path=args.path,
        output_path=args.output_path
    )

elif args.export:
    engine.export(
        project_path=args.path,
        output_path=args.output_path
    )
