from PIL import Image
import face_recognition


image = face_recognition.load_image_file("images/colleagues.jpg")

face_locations = face_recognition.face_locations(image)
face_landmarks_list = face_recognition.face_landmarks(image)

for face_location in face_locations:
    top, right, bottom, left = face_location

    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.save(f'saved_images/{top}.jpg')
