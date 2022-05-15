#!/usr/bin/env python

import sys
from pathlib import Path

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


def main():
    if len(sys.argv) == 1:
        print("You must provide version number as an only script argument")
        sys.exit(1)

    version_number = sys.argv[1]

    static_path = (Path(__file__) / "../../static/").resolve()
    template_path = static_path / "blog_thumbnail_template.png"
    output_path = static_path / "thumbnails" / f"post_{version_number}.png"

    template = Image.open(template_path)
    template_w, template_h = template.size

    text = ImageFont.truetype(
        (static_path / "Spartan-Bold.ttf").as_posix(),
        size=130
    )
    font_w, font_h = text.getsize(version_number)

    draw_x = template_w // 2 - font_w // 2
    draw_y = (template_h // 2 - font_h // 2) + 80

    draw = ImageDraw.Draw(template)
    draw.text(
        (draw_x, draw_y),
        version_number,
        font=text,
        fill="#6b8469",
    )
    template.save(output_path.as_posix())


if __name__ == "__main__":
    main()
