from PIL import Image, ImageDraw, ImageFont
from tkinter import filedialog
from tkinter import Entry, Button, Label, Tk


def add_watermark(image, wm_text):
    # Creates the Image object
    opened_image = Image.open(image)

    # Get Image size
    w, h = opened_image.size
    x, y = int(w / 2), int(h / 2)
    if x > y:
        font_size = y
    elif y > x:
        font_size = x
    else:
        font_size = x
    # Draw on Image
    draw = ImageDraw.Draw(opened_image)

    # Specify a font size
    font_size = int(font_size / 6)

    # For Windows, change font type to 'arial'
    font = ImageFont.truetype('~/Library/Fonts/timesnewroman.ttf', font_size)

    # Coordinates for where we want the image
    image_width, image_height = opened_image.size
    x, y = int(image_width / 1.5), int(image_height / 1.2)

    # Add the watermark
    draw.text((x, y), wm_text, font=font, color='#FFFFFF', anchor='ms')

    # Show the new image
    opened_image.show()


def gui():
    root = Tk()
    root.title('Watermark an Image')
    root.minsize(width=150, height=50)
    root.config(padx=20, pady=20)

    def button_pressed():
        filename = filedialog.askopenfilename(initialdir='/Users/User101/Downloads', title='Select an Image: ')
        print(filename)
        add_watermark(filename, watermark_text.get())

    wm_label = Label(text="Watermark text:", font=("Arial", 16, "normal"))
    wm_label.grid(column=0, row=0)
    watermark_text = Entry(width=20)
    watermark_text.insert(0, '')
    watermark_text.grid(column=1, row=0)
    button = Button(text="Select an image", command=button_pressed)
    button.grid(column=2, row=0)
    button.config(padx=1, pady=1)
    root.mainloop()


gui()
