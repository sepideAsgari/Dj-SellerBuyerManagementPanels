# from PIL import Image
# import os

# def resize_image(image_path, output_path, size=(90, 90)):
#     try:
#         with Image.open(image_path) as img:
#             img = img.convert("RGB")
#             img.thumbnail(size)
#             img.save(output_path)
#         return True
#     except Exception as e:
#         print(f"An error occurred while resizing the image: {e}")
#         return False

# input_image_path = "input_image.png"
# output_image_path = "resized_image.png"
# if resize_image(input_image_path, output_image_path):
#     print("Image resized successfully!")
# else:
#     print("Failed to resize the image.")
