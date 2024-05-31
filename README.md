# PixelPact-PDF-Maker
Certainly! Here is the entire documentation formatted in markdown:

## Overview

The **Image to PDF Converter** is a Python script designed to convert images in various formats into a single PDF file. It supports bulk conversion of images within multiple folders and provides options for setting margins around images in the PDF.

## Supported Image Formats

The script supports the following image formats:
- JPEG (.jpg, .jpeg)
- PNG (.png)
- GIF (.gif)
- BMP (.bmp)
- TIFF (.tiff, .tif)
- WEBP (.webp)
- ICO (.ico)
- HEIF (.heif, .heic)
- SVG (.svg)

## Requirements

- Python 3.x
- Pillow library for image processing

### Installing Pillow

You can install Pillow using pip:

```bash
pip install pillow
```

## How to Use

### Running the Script

1. **Clone or download the script** to your local machine.
2. **Navigate to the script's directory** in your terminal or command prompt.
3. **Run the script** using Python:

```bash
python program.py
```

### Main Menu Options

When you run the script, you will be presented with a menu:

```plaintext
Welcome to the Image to PDF Converter!

MENU:
1. Convert images in a folder to PDF
2. Convert all folders in a folder to bulk PDFs
3. Exit
```

### Setting Margins

Upon starting the script, you will be prompted to enter a margin value in pixels. This margin will be applied to all images in the generated PDFs.

```plaintext
Enter the margin value in pixels (e.g., 10 for a 10-pixel margin, 0 for no margin):
```

### Option 1: Convert Images in a Folder to PDF

1. **Select Option 1** from the menu.
2. **Enter the folder name** containing the images.
3. **Enter the output PDF name** (without the .pdf extension).

The script will convert all supported images in the specified folder to a PDF.

### Option 2: Convert All Folders in a Folder to Bulk PDFs

1. **Select Option 2** from the menu.
2. **Enter the parent folder name** containing the subfolders.
3. The script will process each subfolder and create a PDF for each, named after the subfolder.

### Option 3: Exit

Select this option to exit the program.

## Error Handling

The script includes error handling to manage issues with corrupted or unrecognized image files. If a corrupted image is encountered, the script will skip that file and continue processing the remaining images.

## Example Use Cases

### Converting Images in a Single Folder

```plaintext
Enter the folder name containing the images: sample_images
Enter the name for the output PDF (without the .pdf extension): sample_output
```

This will create a `sample_output.pdf` file in the current directory with images from the `sample_images` folder.

### Bulk Converting Images from Multiple Folders

```plaintext
Enter the folder name containing the folders to convert: bulk_images
```

This will create individual PDF files for each subfolder within the `bulk_images` folder, named after the respective subfolders.

## Conclusion

This script provides a convenient way to convert various image formats into PDFs, with support for bulk operations and configurable margins. Ensure that your image files are not corrupted and that the folder paths are correct to avoid any issues during the conversion process.
```
You can save this content to a markdown file (e.g., `README.md`) for easy reference.
