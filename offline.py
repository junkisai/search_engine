import glob
from PIL import Image

if __name__ == "__main__":
  for img_path in sorted(glob.glob('static/img/*.jpg')):
    print(img_path)
    img = Image.open(img_path).convert('RGB')
    img.show()
    break

  print('owari')
