from visual import Visualizer
import glob


class ImageManager:
    def get_files(self):
        image_files = glob.glob("./assets/*.jpg")
        image_files.append(glob.glob("./assets/*.png"))
#        print(image_files)

 #       print(f'opening: {image_files[0]}')
        Visualizer().visualize(image_files[0])


if __name__ == '__main__':
    ImageManager().get_files()
