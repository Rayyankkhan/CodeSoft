import os
import face_recognition
import numpy as np
import csv
import cv2
from datetime import datetime

# Function to encode known faces and save the encodings to the "encodings" folder
def encode_known_faces():
    known_encodings = []
    known_names = []

    datasets_folder = "datasets"
    for filename in os.listdir(datasets_folder):
        image_path = os.path.join(datasets_folder, filename)
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)[0]

        name = os.path.splitext(filename)[0]
        known_encodings.append(encoding)
        known_names.append(name)

    known_encodings = np.array(known_encodings)
    known_names = np.array(known_names)

    np.save('encodings/known_encodings.npy', known_encodings)
    np.save('encodings/known_names.npy', known_names)

# Function to mark attendance and save records to the CSV file
def mark_attendance(name):
    date_string = datetime.now().strftime('%Y-%m-%d')
    time_string = datetime.now().strftime('%H:%M:%S')

    with open('attendance_records/attendance.csv', 'a', newline='') as file:
        fieldnames = ['Name', 'Date', 'Time']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow({'Name': name, 'Date': date_string, 'Time': time_string})

last_attendance_time = {}

# Main function for real-time face recognition and attendance marking
def main():
    # Load known encodings and names from "encodings" folder
    known_encodings = np.load('encodings/known_encodings.npy', allow_pickle=True)
    known_names = np.load('encodings/known_names.npy', allow_pickle=True)

    # Initialize the webcam or video stream
    video_capture = cv2.VideoCapture(0)  # Use 0 for webcam, or specify the video file path

    while True:
        # Capture each frame from the video stream
        ret, frame = video_capture.read()

        # Find face locations and encodings in the current frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        # Loop through each face found in the frame
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Compare the face encoding with known encodings
            matches = face_recognition.compare_faces(known_encodings, face_encoding)

            name = "Unknown"  # Default name if face is not recognized

            # Check if there is a match with known faces
            if True in matches:
                match_index = np.argmax(matches)
                name = known_names[match_index]

            # Check if this person's attendance was already marked today
            if name != "Unknown" and name not in last_attendance_time:
                mark_attendance(name)
                last_attendance_time[name] = datetime.now()

            elif name != "Unknown":
                # Check if more than 24 hours have passed since the last attendance
                last_attendance = last_attendance_time[name]
                time_difference = datetime.now() - last_attendance
                if time_difference.total_seconds() >= 86400:  # 86400 seconds in 24 hours
                    mark_attendance(name)
                    last_attendance_time[name] = datetime.now()

            # Draw a rectangle around the face and display the name
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255), 1)

        # Display the frame with recognized faces
        cv2.imshow('Face Recognition', frame)
        
        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video stream and close the OpenCV window
    video_capture.release()
    cv2.destroyAllWindows()

# ... (rest of the code) ...
if __name__ == "__main__":
         main()


# Main function for real-time face recognition and attendance marking
# def main():
#     # Load known encodings and names from "encodings" folder
#     known_encodings = np.load('encodings/known_encodings.npy', allow_pickle=True)
#     known_names = np.load('encodings/known_names.npy', allow_pickle=True)

#     # Your code for real-time face recognition and attendance marking here
#     # Use the known_encodings and known_names to recognize faces and mark attendance

# # Run the encode_known_faces function to generate facial encodings
# encode_known_faces()

# # Run the main function for real-time face recognition and attendance marking
# if __name__ == "__main__":
#     main()
# Main function for real-time face recognition and attendance marking
# def main():
#     # Load known encodings and names from "encodings" folder
#     known_encodings = np.load('encodings/known_encodings.npy', allow_pickle=True)
#     known_names = np.load('encodings/known_names.npy', allow_pickle=True)

#     # Initialize the webcam or video stream
#     video_capture = cv2.VideoCapture(0)  # Use 0 for webcam, or specify the video file path

#     while True:
#         # Capture each frame from the video stream
#         ret, frame = video_capture.read()

#         # Find face locations and encodings in the current frame
#         face_locations = face_recognition.face_locations(frame)
#         face_encodings = face_recognition.face_encodings(frame, face_locations)

#         # Loop through each face found in the frame
#         for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
#             # Compare the face encoding with known encodings
#             matches = face_recognition.compare_faces(known_encodings, face_encoding)

#             name = "Unknown"  # Default name if face is not recognized

#             # Check if there is a match with known faces
#             if True in matches:
#                 match_index = np.argmax(matches)
#                 name = known_names[match_index]

#             # Draw a rectangle around the face and display the name
#             cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
#             cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.7, (255, 255, 255), 1)

#             # Mark attendance if a known face is recognized
#             if name != "Unknown":
#                 mark_attendance(name)

#         # Display the frame with recognized faces
#         cv2.imshow('Face Recognition', frame)

#         # Break the loop if 'q' key is pressed
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release the video stream and close the OpenCV window
#     video_capture.release()
#     cv2.destroyAllWindows()

# # Run the encode_known_faces function to generate facial encodings
# encode_known_faces()

# # Run the main function for real-time face recognition and attendance marking
# if __name__ == "__main__":
#     main()