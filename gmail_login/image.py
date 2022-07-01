from PIL import Image


def image_to_pdf(image_path, pdf_name):
    img = open(image_path, "rb")

    png = Image.open(img)
    png.load()
    background = Image.new("RGB", png.size, (255, 255, 255))
    background.paste(png, mask=png.split()[3])
    background.save(pdf_name, "PDF", resolution=100.0, save_all=True)
    img.close()
    png.close()
    background.close()
    return
