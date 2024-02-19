import argparse
import shutil
import os
import logging
from datetime import datetime


def list_extensions(directory):
    extensions = set()
    for file in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, file)):
            _, ext = os.path.splitext(file)
            extensions.add(ext.lower())

    return extensions

def organise_directory(directory, log_enabled):
    extensions = list_extensions(directory)
    files_moved = 0

    for file in os.listdir(directory):
        extension = os.path.splitext(file)[1]
        if extension in extensions:
            extension_dir = os.path.join(directory, extension.lstrip('.'))
            os.makedirs(extension_dir, exist_ok=True)
            src = os.path.join(directory, file)
            dst = os.path.join(extension_dir, file)

            shutil.move(src, dst)
            files_moved += 1  # Increment the counter

            if log_enabled:
                logging.info(f'Moved {src} to {dst}')

        if log_enabled:
            if files_moved == 0:
                logging.info("No files needed to be moved.")
            else:
                logging.info(f"Completed moving {files_moved} files.")

    

def setup_logging():
    log_dir = os.path.join(os.getcwd(), 'logs')
    os.makedirs(log_dir, exist_ok=True)
    log_filename = datetime.now().strftime('%Y-%m-%d_%H-%M-%S.log')
    logging.basicConfig(filename=os.path.join(log_dir, log_filename), level=logging.INFO,
                        format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')



def main():
    parser = argparse.ArgumentParser(description='Organize files into folders by file extension.')
    parser.add_argument('directory', type=str, help='Directory to organize')
    parser.add_argument('--log', action='store_true', help='Enable logging of actions')

    args = parser.parse_args()

    if args.log:
        setup_logging()

    organise_directory(args.directory, args.log)

if __name__ == '__main__':
    main()
