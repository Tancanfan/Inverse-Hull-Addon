#### Inverse Hull Outline Addon
## Description:
The Inverse Hull Outline addon for Blender automatically adds a cartoon-style outline to selected 3D meshes, giving them a stylized, cel-shaded appearance. This can be particularly useful for creating 3D models with a hand-drawn or comic book-like aesthetic.

## What is an Inverse Hull?
An inverse hull is a technique used to generate outlines around 3D objects by duplicating and scaling the mesh slightly outward, then inverting the normals. This process creates a visible outline that simulates the look of traditional cartoon-style drawing.

### Installation
Download or clone the repository.
Open Blender and go to Edit > Preferences > Add-ons.
Click Install... and navigate to the downloaded files, selecting the __init__.py file.
Once installed, enable the addon by checking the box next to its name.
### Usage
Select the 3D objects in your scene that you want to apply the outline to.
Go to View3D > Sidebar > Auto Cartoon.
Click the "Add Outline" button to automatically generate a cartoon-style outline around the selected objects.
### Files Included
__init__.py: The initialization file for the Blender addon.
auto_cartoon.py: The script that handles the outline generation process.
### Notes
The addon works best with solid objects and may require adjustments to the object’s geometry for optimal results.
This tool is designed to be user-friendly, making it accessible even for those new to Blender.
### License
This project is licensed under the MIT License. See the LICENSE file for more details.
