from IPython.display import IFrame, Image
from typing import Dict
from pathlib import Path

# TODO automatically convert drawio to png when presentation mode is True. Currently it looks for a png file with specific naming convention
def draw(drawio_file_name, overrides: Dict = {}, presentation_mode=False):
    # defaults
    width=overrides.get("width", 2000)
    height=overrides.get("height", 800)

    
    file = Path(drawio_file_name)
    if presentation_mode:
        png_file = Path(file.stem+"-00.png") #FIXME hardcoded since it stop gap anyways
        if png_file.exists():
            return Image(png_file.name,width=width,height=height)
        else:
            return f'''No accompanying PNG file of name {png_file.absolute()} found for {file.name}'''
    # create a file, if it doesn't exist
    if file.exists() == False:
        file.write_text("")
    return IFrame(
        "/doc/tree/" + file.name, #FIXME hard coded to root folder
        width=width,
        height=height,
    )
    