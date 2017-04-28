import face_recognition
import cv2
import glob
import os.path

# This is a demo of running face recognition on live video from your webcam.
# It's a little more complicated than the other example, but it includes some
# basic performance tweaks to make things run a lot faster: 1. Process each
# video frame at 1/4 resolution (though still display it at full resolution) 2.
# Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed
# only to read from your webcam.  OpenCV is *not* required to use the
# face_recognition library. It's only required if you want to run this specific
# demo. If you have trouble installing it, try any of the other demos that
# don't require it instead.

# Get a reference to webcam #0 (the default one)
print("Starting Camera... ")
video_capture = cv2.VideoCapture(0)
print("Done.")

print("Loading training data... ")
# Load a sample picture and learn how to recognize it.
people = glob.glob("source_images/*.*")
source_encodings = []
for filename in people:
    print(filename)
    image = face_recognition.load_image_file(filename)
    encoding = face_recognition.face_encodings(image)[0]
    name = os.path.basename(filename).split(".")[0]
    source_encodings.append((name, encoding))

print("Done.")
# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

def first_matching_encoding(name_encoding_tuples, face_encoding):
    for name, encoding in name_encoding_tuples:
        if face_recognition.compare_faces([encoding], face_encoding)[0]:
            return name
    return "Unknown"

print("Processing video... ")
while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            face_names.append(first_matching_encoding(source_encodings, face_encoding))

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        # cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
print("Done.")
