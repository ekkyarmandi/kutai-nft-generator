import os
import sys

from scripts import util
from engine import layers_merger, generator

layers_merger(source_path="layers", size_type="default")

project_folder = os.path.join("project","example")
util.check_folder(project_folder)

metadata_folder = os.path.join(project_folder,"metadata")
util.check_folder(metadata_folder)

generator(output_path=project_folder)
