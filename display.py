from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter

font_choice = 5
if font_choice == 1:
    project_font = "font/italic.ttf"
elif font_choice == 2:
    project_font = "font/regular.ttf"
elif font_choice == 3:
    project_font = "font/Font.ttc.ttf"
elif font_choice == 4:
    project_font = "font/aladin.ttf"
elif font_choice == 5:
    project_font = "font/wild-regular.ttf"
elif font_choice == 6:
    project_font = "font/VScript-regular.ttf"
elif font_choice == 7:
    project_font = "font/BethEllen-regular.ttf"
else:
    project_font = "font/Font.ttc.ttf"

quote_font_choice = 1
if quote_font_choice == 1:
    quote_font   = "font/italic.ttf"
elif quote_font_choice == 2:
    quote_font   = "font/regular.ttf"
elif quote_font_choice == 3:
    quote_font   = "font/Font.ttc.ttf"
elif quote_font_choice == 4:
    quote_font   = "font/aladin.ttf"
elif quote_font_choice == 5:
    quote_font   = "font/wild-regular.ttf"
elif quote_font_choice == 6:
    quote_font   = "font/VScript-regular.ttf"
elif quote_font_choice == 7:
    quote_font   = "font/BethEllen-regular.ttf"
else:
    quote_font   = "font/Font.ttc.ttf"

# Set the fonts
font22 = ImageFont.truetype(project_font, 22)
font30 = ImageFont.truetype(project_font, 30)
font35 = ImageFont.truetype(project_font, 35)
font40 = ImageFont.truetype(project_font, 40)
font50 = ImageFont.truetype(project_font, 50)
font60 = ImageFont.truetype(project_font, 60)
font70 = ImageFont.truetype(project_font, 70)
font80 = ImageFont.truetype(project_font, 80)
font90 = ImageFont.truetype(project_font, 90)
font100 = ImageFont.truetype(project_font, 100)
font120 = ImageFont.truetype(project_font, 120)
font130 = ImageFont.truetype(project_font, 130)
font160 = ImageFont.truetype(project_font, 160)

# Set the quote fonts
quote_font22 = ImageFont.truetype(quote_font, 22)
quote_font30 = ImageFont.truetype(quote_font, 30)
quote_font35 = ImageFont.truetype(quote_font, 35)
quote_font40 = ImageFont.truetype(quote_font, 40)
quote_font50 = ImageFont.truetype(quote_font, 50)
quote_font60 = ImageFont.truetype(quote_font, 60)
quote_font70 = ImageFont.truetype(quote_font, 70)
quote_font80 = ImageFont.truetype(quote_font, 80)
quote_font90 = ImageFont.truetype(quote_font, 90)
quote_font100 = ImageFont.truetype(quote_font, 100)
quote_font120 = ImageFont.truetype(quote_font, 120)
quote_font130 = ImageFont.truetype(quote_font, 130)
quote_font160 = ImageFont.truetype(quote_font, 160)

class Display:
    def __init__(self):
        self.im = Image.open("pic/gtr1.png")
        self.im = ImageOps.fit(self.im, (800, 480), method = 0, bleed = 0.0, centering =(0.5, 0.5)) 
        self.background = self.im.filter(ImageFilter.GaussianBlur(1))
        # Initialize the drawing context with template as background
        self.draw_black = ImageDraw.Draw(self.background)
        
    def draw_text(self, x, y, text, font, color):
        w, h = self.draw_black.textsize(text)
        self.draw_black.text((x-w/2, y), text, font=font, fill=color)
        
    def draw_icon(self, x, y, c, l, h, icon):
        im_icon = Image.open("icons/" + icon + ".png")
        im_icon = im_icon.convert("RGBA")
        # print(im_icon.mode)
        im_icon = im_icon.resize((l, h))
        if c == "b":
            self.background.paste(im_icon, (x, y), im_icon)
