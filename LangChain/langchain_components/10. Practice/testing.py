import math
import random
from PIL import Image, ImageDraw, ImageFilter, ImageFont


def render_realistic_handwriting(text, output_filename="realistic_notes.png"):
    # Create base notebook canvas
    width, height = 1000, 1400
    canvas = Image.new("RGBA", (width, height), (252, 250, 242, 255))
    draw = ImageDraw.Draw(canvas)

    # 1. Draw Paper Texture / Lined Background
    for y in range(120, height - 50, 42):
        draw.line([(80, y), (width - 60, y)], fill=(200, 215, 230, 200), width=1)
    draw.line([(140, 0), (140, height)], fill=(240, 180, 180, 250), width=2)

    # 2. Setup Base Handwriting Font
    try:
        base_font = ImageFont.truetype("handwriting_base.ttf", size=32)
    except:
        base_font = ImageFont.load_default()

    # Dynamic cursor position
    cursor_x = 160
    cursor_y = 125
    line_spacing = 42

    for char in text:
        if char == "\n":
            cursor_x = 160
            cursor_y += line_spacing
            continue

        # Create temporary canvas for individual character transformation
        char_img = Image.new("RGBA", (60, 60), (0, 0, 0, 0))
        char_draw = ImageDraw.Draw(char_img)

        # A. Ink Pressure Variation (Random Opacity & Blue-Ballpen Shade)
        ink_blue = (
            random.randint(15, 35),
            random.randint(25, 55),
            random.randint(130, 170),
            random.randint(210, 255),
        )

        char_draw.text((10, 10), char, font=base_font, fill=ink_blue)

        # B. Micro-Rotation (Hand Slant Variation: -3 to +3 degrees)
        angle = random.uniform(-3.5, 3.5)
        rotated_char = char_img.rotate(
            angle, resample=Image.BICUBIC, expand=True
        )

        # C. Micro-Jitter Position Offsets (Per-character Floating)
        jitter_x = random.randint(-1, 2)
        jitter_y = random.randint(-2, 2)

        # Composite onto main notebook page
        canvas.paste(
            rotated_char,
            (cursor_x + jitter_x, cursor_y + jitter_y),
            mask=rotated_char,
        )

        # Advance cursor with natural kerning noise
        char_width = 18 + random.randint(-1, 2)
        cursor_x += char_width

        # Line Wrap Logic
        if cursor_x > width - 100:
            cursor_x = 160
            cursor_y += line_spacing

    # 3. Post-Processing: Ink Bleed & Slight Blur Simulation
    canvas = canvas.filter(ImageFilter.GaussianBlur(radius=0.4))

    canvas.save(output_filename)
    print(f"Realistic handwritten page saved: {output_filename}")


sample_text = (
    "Photosynthesis is the biological process used by plants\n"
    "to convert light energy into chemical energy. During this\n"
    "process, oxygen is released as a byproduct."
)

render_realistic_handwriting(sample_text)