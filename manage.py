import os
from random import choices
import sys

import argparse

from scripts import util
from engine import layers_merger, generator

parser = argparse.ArgumentParser(description='Artwork Random Generative Engine')

parser.add_argument(
    "command",
    type=str,
    choices=["startproject","merge","generate"],
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
    "-mp", "--merge-path",
    type=str,
    default="layers",
    help="Layers path folder"
)

parser.add_argument(
    "-p", "--path",
    type=str,
    default="project\\example",
    help="Project path folder"
)

args = parser.parse_args()

# if args.command == "merge" and "layers" not in args.path:
#     raise argparse.ArgumentError(path, "Path for Merge command should be Layers path")

if args.command == "startproject":
    
    # create project folder
    project_path = os.path.join("project",args.path)
    util.check_folder(project_path)

    # create sub folders
    sub_folders = [
        "layers",
        "output\\backup",
        "output\\metadata",
        "source"
    ]
    for sub in sub_folders:
        sub_path = os.path.join(project_path,sub)
        util.check_folder(sub_path)

    # print out the message
    print(project_path,"has been created")

elif args.command == "generate":
        
    pass

elif args.command == "merge":
    
    pass

