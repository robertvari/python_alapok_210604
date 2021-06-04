import os
from PIL import Image, ExifTags


class Photo:
    def __init__(self):
        self._file_name = None
        self._size = None
        self._date = None
        self._img = None

    def open(self, file_path):
        assert os.path.exists(file_path), f"File does not exist: {file_path}"
        assert file_path.lower().endswith(".jpg"), "File must be .jpg"

        self._file_name = os.path.basename(file_path)

        self._img = Image.open(file_path)
        self._size = self._img.size

        # collect data from image meta
        self._get_exif_data()

    def _get_exif_data(self):
        if not self._img:
            return

        exif_data = self._img._getexif()

        if not exif_data:
            return

        for key, value in exif_data.items():
            tag_name = ExifTags.TAGS.get(key)

            if tag_name == "DateTime":
                self._date = value

    def report(self):
        print("-"*50)

        print(f"File: {self._file_name}")
        print(f"Size: {self._size}")
        print(f"Date: {self._date}")

        print("-" * 50)

    def __str__(self):
        return self._file_name