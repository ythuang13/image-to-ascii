import cv2
import numpy as np

ascii_choices = '.,-~:;=!*#$@'
# ascii_choices = ascii_choices[::-1]
# ascii_choices = '▁▂▃▄▅▆▇█'

def main():
    original_img = cv2.imread("donut.bmp", cv2.IMREAD_GRAYSCALE)

    # resize
    resize_factor = original_img.shape[0] // 70
    resized_img = cv2.resize(
        original_img,
        (
            original_img.shape[1] // resize_factor,
            original_img.shape[0] // resize_factor // 2,
        ),
    )

    # matrix, convert and print
    m = np.array(resized_img)
    ascii_choices_length = len(ascii_choices)
    ascii_choices_spacing = 256 // ascii_choices_length + 1
    with open("output.txt", "w", encoding="utf-8") as f:
        for row in m:
            for col in row:
                f.write(ascii_choices[col // ascii_choices_spacing])
            f.write('\n')

    # show
    # img_concat = np.concatenate((resized_img, ), axis=1)
    # cv2.imshow(
    #     "images", resized_img
    # )

    # cv2.waitKey(0)


if __name__ == "__main__":
    main()
