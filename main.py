import shutil
import os

directory = '/Users/jack/downloads'

def list_extensions(directory):
    extensions = set()
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            _, ext = os.path.splitext(file)
            extensions.add(ext.lower())

    return extensions

extensions = list_extensions(directory)

for file in os.listdir(directory):
    extension = os.path.splitext(file)[1]
    if extension in extensions:
        extension_dir = os.path.join(directory, extension.lstrip('.'))  
        os.makedirs(extension_dir, exist_ok=True)

        shutil.move(os.path.join(directory, file), os.path.join(extension_dir, file))


