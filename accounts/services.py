import os
from accounts.models import DEFAULT_PROFILE_IMAGE_PATH

def remove_old_image(path):
    if os.path.isfile(path) and path not in [DEFAULT_PROFILE_IMAGE_PATH]:
        os.remove(path)
