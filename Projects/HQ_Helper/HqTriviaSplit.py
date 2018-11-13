from PIL import Image
 
def crop(image_path, coords, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    cropped_image.show()
 
 
if __name__ == '__main__':
    image = '/home/omar/Documents/Python-Concepts/Projects/HQ_Helper/HQ-num24.png'
    crop(image, (100, 330, 1006, 800), '/home/omar/Documents/Python-Concepts/Projects/HQ_Helper/croppedQuestion.jpg')
    crop(image, (150, 800, 900, 1000), '/home/omar/Documents/Python-Concepts/Projects/HQ_Helper/croppedAnswer1.jpg')
    crop(image, (150, 1010, 900, 1210), '/home/omar/Documents/Python-Concepts/Projects/HQ_Helper/croppedAnswer2.jpg')
    crop(image, (150, 1215, 900, 1415), '/home/omar/Documents/Python-Concepts/Projects/HQ_Helper/croppedAnswer3.jpg')
