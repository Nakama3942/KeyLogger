def rgb_to_mono(color: str, gray: bool):
    # Source: https://www.had2know.org/technology/rgb-to-gray-scale-converter.html
    # Algorithm:
    # print(f'RGB:  {color}')
    # red = color[0:2]
    # green = color[2:4]
    # blue = color[4:6]
    # if gray:
    #     mono_red = int(red, 16) * 0.299
    #     mono_green = int(green, 16) * 0.587
    #     mono_blue = int(blue, 16) * 0.114
    #
    #     mono_color = hex(round(mono_red + mono_green + mono_blue)).replace('0x', '').zfill(2)
    #     mono_color = mono_color * 3
    # else:
    #     mono_red = hex(round(int(red, 16) * 0.299)).replace('0x', '').zfill(2)
    #     mono_green = hex(round(int(green, 16) * 0.587)).replace('0x', '').zfill(2)
    #     mono_blue = hex(round(int(blue, 16) * 0.114)).replace('0x', '').zfill(2)
    #
    #     mono_color = mono_red + mono_green + mono_blue
    # print(f'MONO: {mono_color}')
    # return mono_color
    if gray:
        return (hex(round((int(color[0:2], 16) * 0.299) + (int(color[2:4], 16) * 0.587) + (int(color[4:6], 16) * 0.114))).replace('0x', '').zfill(2)) * 3
    else:
        return hex(round(int(color[0:2], 16) * 0.299)).replace('0x', '').zfill(2) + hex(round(int(color[2:4], 16) * 0.587)).replace('0x', '').zfill(2) + hex(round(int(color[4:6], 16) * 0.114)).replace('0x', '').zfill(2)


def rgb_to_sepia(color: str):
    # print(f'RGB:  {color}')
    red = color[0:2]
    green = color[2:4]
    blue = color[4:6]

    sepia_red = hex(round((int(red, 16) * 0.393) + (int(green, 16) * 0.769) + (int(blue, 16) * 0.189))).replace('0x', '').zfill(2)
    sepia_green = hex(round((int(red, 16) * 0.349) + (int(green, 16) * 0.686) + (int(blue, 16) * 0.168))).replace('0x', '').zfill(2)
    sepia_blue = hex(round((int(red, 16) * 0.272) + (int(green, 16) * 0.534) + (int(blue, 16) * 0.131))).replace('0x', '').zfill(2)

    sepia_color = sepia_red + sepia_green + sepia_blue
    # print(f'MONO: {sepia_color}')
    return sepia_color


# Converting colors
# if __name__ == '__main__':
#     color = '36471d'
#     print(color)
#     print(rgb_to_mono(color, False))
#     print(rgb_to_mono(color, True))
#     print(rgb_to_sepia(color))
