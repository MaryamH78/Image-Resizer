import cv2
import os

def resize_and_save_image(image_path, scale):
    # Read the image from the input path
    image = cv2.imread(image_path)
    
    if image is None:
        print("Image not found.")
        return

    # Get the current dimensions of the image
    height, width = image.shape[:2]

    # Calculate new dimensions based on the input scale
    new_width = int(width * scale)
    new_height = int(height * scale)
    new_size = (new_width, new_height)

    # Resize the image
    resized_image = cv2.resize(image, new_size, interpolation=cv2.INTER_LINEAR)

    # Create output path with a fixed name
    base_name = os.path.basename(image_path)
    name, ext = os.path.splitext(base_name)
    output_path = f"{name}_resized{ext}"

    # Save the resized image to the output path
    cv2.imwrite(output_path, resized_image)
    print(f"Resized image saved at {output_path}")

    # Display the resized image
    cv2.imshow('Resized Image', resized_image)
    cv2.waitKey(0)  # Wait for a key press to close the window
    cv2.destroyAllWindows()  # Close all OpenCV windows

# Get the image path and scale from user input
image_path = input("Enter the image path: ")
scale = float(input("Enter the scale factor: "))

resize_and_save_image(image_path, scale)
