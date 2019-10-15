from visual import *
import glob


class ImageManager:
    def get_files(self):
        image_files = glob.glob("./assets/*.jpg")
        print(image_files)

        print(f'opening: {image_files[0]}')
        Visualer().visualize(image_files[0])


if __name__ == '__main__':
    ImageManager().get_files()
