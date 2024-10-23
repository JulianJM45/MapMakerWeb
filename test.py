import img2pdf
import io

def PDFgen(image_paths):
    # Create an in-memory bytes buffer
    pdf_buffer = io.BytesIO()
    
    # Convert the images to PDF and write to the buffer
    pdf_buffer.write(img2pdf.convert(image_paths))
    
    # Ensure the buffer is positioned at the beginning
    pdf_buffer.seek(0)
    
    return pdf_buffer


def main():
    image_paths = 'MyMaps/MyMap1.png', 'MyMaps/MyMap2.png'

    pdf_buffer = PDFgen(image_paths)
    with open('output.pdf', 'wb') as f:
        f.write(pdf_buffer.read())




if __name__ == '__main__':
    main()