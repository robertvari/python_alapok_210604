from utilities.Photo import Photo


def main():
    photo = Photo()
    photo.open(r"C:\Work\_PythonSuli\python_alapozo\photos\IMG_1069.JPG")
    photo.report()


if __name__ == '__main__':
    main()