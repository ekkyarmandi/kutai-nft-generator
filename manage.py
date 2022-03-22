import os
import sys

from scripts import util
from engine import layers_merger, generator

if sys.argv[1] == "generate":
        
    project_folder = os.path.join("project",sys.argv[3])
    util.check_folder(project_folder)
    
    metadata_folder = os.path.join(project_folder,"metadata")
    util.check_folder(metadata_folder)

    generator(number=sys.argv[2], output_path=project_folder)

elif sys.argv[1] == "compile":
    
    layers_merger(source_path="layers", size_type="default")