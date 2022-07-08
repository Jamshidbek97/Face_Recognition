import face_recognition
from PIL import Image, ImageDraw

image_of_ronaldo = face_recognition.load_image_file('images/cristiano-ronaldo.webp')
ronaldo_face_encoding = face_recognition.face_encodings(image_of_ronaldo)[0]

image_of_will = face_recognition.load_image_file('images/Will-Smith.webp')
will_face_encoding = face_recognition.face_encodings(image_of_will)[0]

image_of_neymar = face_recognition.load_image_file('images/neymar.jpg')
neymar_face_encoding = face_recognition.face_encodings(image_of_neymar)[0]

# Create an array of encodings and names
known_face_encodings = [
    ronaldo_face_encoding,
    will_face_encoding,
    neymar_face_encoding
]

known_face_names = [
    'Cristiano Ronaldo',
    'Will Smith',
    "Neymar JR"
]

# Load test image to find faces
test_image = face_recognition.load_image_file('images/team2.jpg')

#  Find faces in test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# Convert to pill format
pil_image = Image.fromarray(test_image)

# Create an ImageDraw instance
draw = ImageDraw.Draw(pil_image)

# Loop through faces in test image
for(top, right, bottom, left), face_encodings in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encodings)

    name = 'Unknown Person'

    # If match
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    # Draw Box
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 0))

    # Draw Label
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 0,), outline=(0, 0, 0))
    draw.text((left + 6, bottom - text_height - 5), name, fill= (255, 255, 255, 255))

del draw

# Display image
pil_image.show()

pil_image.save("identify.jpg")
