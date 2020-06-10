#!/usr/bin/env python3
import click
import os

@click.command()
@click.option("--audio", default="Audio", help="Directory name for mp3 files.", show_default=True)
@click.option("--video", default="Footage", help="Directory name for video files.",  show_default=True)
@click.option("--image", default="Images", help="Directory name for image files.",  show_default=True)
def main(audio, video, image):
    """ Program to sort various files into respective folders for video editing use."""
    directory_list = [audio, video, image]
    create_directory(directory_list)
    sort_files(directory_list)
    return

def file_to_which_directory(file_extension, directory_list):
    """ Get correct directory name based on the file extension type """
    audio = directory_list[0]
    video = directory_list[1]
    image = directory_list[2]
    extensions = {
        "mp3" : audio,
        "mov" : video,
        "mp4" : video,
        "png" : image,
        "jpg" : image,
    }
    return extensions.get(file_extension, None)

def sort_files(directory_list):
    """ Sort files in root directory and move to appropiate directory."""
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        name, extension = os.path.splitext(f)
        directory = file_to_which_directory(extension, directory_list)
        print(name)
        print(extension)
        # Extension doesn't exist so it would not be moved
        if directory is None:
            pass

        try:
            os.rename(f, f"{directory}/{f}")
            click.echo(f"Moving {name} into {directory} directory...")
        except OSError:
            click.echo(f"Error moving {name} into {f} {directory} directory...")
        else:
            click.echo(f"{name} successfully moved into {directory}!")
    return

def create_directory(directory_list):
    for directory in directory_list:
        exists = os.path.isdir(directory)
        if (exists):
            click.echo(f"Skipping creation of {directory} directory. Directory already exists.")
            continue
        try:
            os.mkdir(directory)
            click.echo(f"Creating {directory} directory...")
        except OSError:
            click.echo(f"Error creating {directory} directory...")
        else:
            click.echo(f"{directory} directory successfully created!")
    return

if __name__ == '__main__':
    # pylint: disable=no-value-for-parameter
    main()