#!/usr/bin/env python3
"""
CLI used to organize files for video editing.
"""

import os
import click

from colorama import init, Fore

@click.command()
@click.option("--audio", default="Audio", help="Directory name for mp3 files.",
              show_default=True)
@click.option("--video", default="Footage", help="Directory name for video files.",
              show_default=True)
@click.option("--image", default="Images", help="Directory name for image files.",
              show_default=True)
def main(audio, video, image):
    """ Program to sort various files into respective folders for video editing use."""
    init(autoreset=True)
    directory_list = [audio, video, image]
    create_directory(directory_list)
    sort_files(directory_list)

def file_to_which_directory(file_extension, directory_list):
    """ Get correct directory name based on the file extension type."""
    audio = directory_list[0]
    video = directory_list[1]
    image = directory_list[2]
    extensions = {
        ".mp3" : audio,
        ".mov" : video,
        ".mp4" : video,
        ".png" : image,
        ".jpg" : image,
    }
    return extensions.get(file_extension)

def sort_files(directory_list):
    """ Sort files in root directory and move to appropiate directory."""
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    if len(files) == 0:
        click.echo(Fore.YELLOW + "No files found in directory!")

    for fil in files:
        name, extension = os.path.splitext(fil)
        directory = file_to_which_directory(extension, directory_list)
        # Extension doesn't exist so it would not be moved
        if directory is None:
            continue

        try:
            os.rename(fil, f"{directory}/{fil}")
            click.echo(Fore.LIGHTCYAN_EX + f"Moving {name} into {directory} directory...")
        except OSError:
            click.echo(Fore.RED + f"Error moving into {name} {directory} directory.")
        else:
            click.echo(Fore.GREEN + f"DONE! Successfully moved {name} into {directory}.")

def create_directory(directory_list):
    """ Create directories with name provided. """
    for directory in directory_list:
        exists = os.path.isdir(directory)
        if exists:
            click.echo(Fore.YELLOW +
                       f"Skipping creation of {directory} directory. Directory already exists.")
            continue
        try:
            os.mkdir(directory)
            click.echo(Fore.LIGHTCYAN_EX + f"Creating {directory} directory...")
        except OSError:
            click.echo(Fore.RED + f"Error creating {directory} directory...")
        else:
            click.echo(Fore.GREEN + f"DONE! {directory} directory successfully created.")

if __name__ == '__main__':
    # pylint: disable=no-value-for-parameter
    main()
    