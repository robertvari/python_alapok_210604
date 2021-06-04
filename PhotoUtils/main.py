from utilities.Photo import Photo


def main():
    photo = Photo()
    photo.open(r"C:\Work\_PythonSuli\python_alapozo\photos\cedric-letsch-ie2xdSo3POc-unsplash.jpg")
    photo.create_report()
    photo.watermark()


if __name__ == '__main__':
    main()