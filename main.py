import os
from PIL import Image, ImageOps, UnidentifiedImageError, ImageFile

# Ensure PIL can load truncated images
ImageFile.LOAD_TRUNCATED_IMAGES = True

# Supported image file extensions
SUPPORTED_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.webp', '.ico', '.heif', '.heic', '.svg']

def convert_images_to_pdf(folder_name, output_pdf_name, margin):
    if not os.path.isdir(folder_name):
        print(f"The folder '{folder_name}' does not exist.")
        return
    
    image_files = sorted([f for f in os.listdir(folder_name) if os.path.splitext(f)[1].lower() in SUPPORTED_EXTENSIONS])
    
    if not image_files:
        print(f"No valid image files found in the folder '{folder_name}'.")
        return
    
    images = []
    for file in image_files:
        img_path = os.path.join(folder_name, file)
        try:
            img = Image.open(img_path).convert('RGB')
            if margin > 0:
                img = ImageOps.expand(img, border=margin, fill='white')
            images.append(img)
        except (UnidentifiedImageError, OSError) as e:
            print(f"Skipping corrupted image file {img_path}: {e}")
    
    if images:
        output_pdf_path = os.path.join(os.getcwd(), output_pdf_name)
        images[0].save(output_pdf_path, save_all=True, append_images=images[1:], dpi=(300, 300))
        print(f"PDF created successfully at {output_pdf_path}")
    else:
        print(f"No valid image files found to create PDF in the folder '{folder_name}'.")

def convert_folders_to_bulk_pdf(folder_name, margin):
    if not os.path.isdir(folder_name):
        print(f"The folder '{folder_name}' does not exist.")
        return

    for subfolder in os.listdir(folder_name):
        subfolder_path = os.path.join(folder_name, subfolder)
        if os.path.isdir(subfolder_path):
            output_pdf_name = f"{subfolder}.pdf"
            convert_images_to_pdf(subfolder_path, output_pdf_name, margin)

def main():
    print("Welcome to the PixelPact-PDF-Maker!")
    margin = int(input("Enter the margin value in pixels (e.g., 10 for a 10-pixel margin, 0 for no margin): ").strip())
    while True:
        print("\nMENU:")
        print("1. Convert images in a folder to PDF")
        print("2. Convert all folders in a folder to bulk PDFs")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ").strip()

        if choice == '1':
            folder_name = input("Enter the folder name containing the images: ").strip()
            output_pdf_name = input("Enter the name for the output PDF (without the .pdf extension): ").strip() + ".pdf"
            convert_images_to_pdf(folder_name, output_pdf_name, margin)
        elif choice == '2':
            folder_name = input("Enter the folder name containing the folders to convert: ").strip()
            convert_folders_to_bulk_pdf(folder_name, margin)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter either 1, 2, or 3.")

# Run the main function
main()
