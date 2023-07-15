from django.db import models
import os

def get_category_image_path(instance, filename):
    extension = os.path.splitext(filename)[1]
    new_filename = f"{instance.category_name}{extension}"
    return os.path.join("category_images", new_filename)