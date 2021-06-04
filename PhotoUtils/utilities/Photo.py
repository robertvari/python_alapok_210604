import os
from PIL import Image, ExifTags


class Photo:
    def __init__(self):
        self._file_name = None
        self._dir_name = None
        self._size = None
        self._date = None
        self._img = None

    @property
    def path(self):
        return os.path.join(self._dir_name, self._file_name)

    @property
    def date(self):
        if self._date:
            return self._date

        return "Date not found!"

    def open(self, file_path):
        assert os.path.exists(file_path), f"File does not exist: {file_path}"
        assert file_path.lower().endswith(".jpg"), "File must be .jpg"

        self._file_name = os.path.basename(file_path)
        self._dir_name = os.path.dirname(file_path)

        self._img = Image.open(file_path)
        self._size = self._img.size

        # collect data from image meta
        self._get_exif_data()

    def delete(self):
        user_input = input(f"Do you really want to delete: {self._file_name}(y/n)")
        if user_input == "y":
            self._img.close()

            os.remove(self.path)
            print(f"File {self._file_name} was deleted")

            self._file_name = None
            self._dir_name = None
            self._size = None
            self._date = None
            self._img = None

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

    def create_report(self):
        """
        Saves an xlsx file into the photo folder
        :return:
        """
        pass

    def watermark(self):
        """
        Creates a smaller, watermarked version of the photo.
        :return:
        """
        pass