from PIL import Image, ImageDraw, ImageFont
import os
import random
import textwrap


class MemeEngine:
    """Class that uses Pillow to generate images"""

    def __init__(self, out_dir ) -> None:
        self.out_dir = out_dir

        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        pass

    def make_meme(self, img_path, body=None, author=None, width=500) -> str:
        """Function that crops and writes on the image"""
        colors =("#f0e68c",'#b8860b','white','#fffaf0','#f5deb3')
        img = Image.open(img_path)

        if width is not None:
            ratio = width / float(img.size[0])
            height = int(ratio * float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

        if body is not None:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype("./_data/fonts/Poppins-Bold.ttf", 30)
            wrapper = textwrap.TextWrapper(width=20)
            caption = wrapper.fill(text=body)
            draw.text((10, 60), f"{caption}-{author}", font=font, fill=random.choice(colors))

        new_file = os.path.join(
            f"./static/dog_meme_{random.randint(0,1000000)}.jpg"
        )

        img.save(new_file, "JPEG")
        return new_file
