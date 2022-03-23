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
    choices=["merge","generate"],
    help="Main command line"
)

parser.add_argument(
    "-n", "--number",
    type=int,
    nargs=1,
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

# if args.command == "merge" and "layers" in args.path:
#     raise argparse.ArgumentError(path, "Path for Merge command should be Layers path")

if args.command == "generate":
        
    project_folder = os.path.join("project",args.path)
    util.check_folder(project_folder)

    generator(number=args.number, output_path=project_folder)

elif args.command == "merge":
    
    layers_merger(source_path=args.merge_path, size_type=args.size_path)

