from email.mime import image
from PIL import Image


PERFECT_WHITE = (255, 255, 255)
PERFECT_BLUE = (1, 83, 219)

def get_cloud_percent(image_path):
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size

    all_pixels = []
    for x in range(width):
        for y in range(height):
            cpixel = pixels[x, y]
            all_pixels.append(cpixel)
    whites_counter = 0
    blues_counter = 0
    for p in all_pixels:
        current_pixel_white_offset = sum([abs(p[i]-PERFECT_WHITE[i]) for i in range(len(p))])
        current_pixel_blue_offset = sum([abs(p[i]-PERFECT_BLUE[i]) for i in range(len(p))])
        if current_pixel_white_offset > current_pixel_blue_offset:
            blues_counter += 1
        else: 
            whites_counter += 1
    
    return whites_counter*100/(blues_counter+whites_counter)

def main():
    f = input('image:')
    cloud_percent = get_cloud_percent(f)
    print(f'Clouds: {round(cloud_percent, 2)}%')

if __name__ == '__main__':
    main()