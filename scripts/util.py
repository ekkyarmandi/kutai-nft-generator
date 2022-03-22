import os


def check_folder(path):
    path = [p for p in path.split("\\") if "." not in p]
    path = os.path.join(*path)
    os.makedirs(path)