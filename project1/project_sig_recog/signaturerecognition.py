# import cv2

# # Load the captured signature image
# captured_signature = cv2.imread(
#     "C:/Users/divyanshi mittal/Desktop/project/signature.jpg", cv2.IMREAD_GRAYSCALE)
# captured_signature = cv2.convertScaleAbs(captured_signature, cv2.CV_8U)

# # Create a dictionary to store student names and their reference signatures
# student_signatures = {
#     "Divyanshi": "C:/Users/divyanshi mittal/Desktop/student_data/signature1.jpg",
#     "Harshit": "C:/Users/divyanshi mittal/Desktop/student_data/signature2.jpg",
#     "Gautam": "C:/Users/divyanshi mittal/Desktop/student_data/signature3.jpg",
#     # Add more students and reference signature file paths as needed
# }

# # Initialize a flag to check if any reference signature matches
# signature_matched = False
# matched_student_name = None

# # Initialize the SIFT detector
# sift = cv2.SIFT_create()

# # Define FLANN parameters for matching
# flann_params = dict(algorithm=0, trees=5)
# index_params = dict(algorithm=0, trees=5)
# search_params = dict(checks=50)

# # Create a FLANN (Fast Library for Approximate Nearest Neighbors) matcher
# flann = cv2.FlannBasedMatcher(index_params, search_params)

# # Perform image comparison for each student's reference signature
# for student_name, reference_signature_path in student_signatures.items():
#     reference_signature = cv2.imread(
#         reference_signature_path, cv2.IMREAD_GRAYSCALE)
#     reference_signature = cv2.convertScaleAbs(reference_signature, cv2.CV_8U)


#     # Detect keypoints and compute descriptors using SIFT
#     kp1, des1 = sift.detectAndCompute(reference_signature, None)
#     kp2, des2 = sift.detectAndCompute(captured_signature, None)

#     # Match the descriptors using FLANN
#     matches = flann.knnMatch(des1, des2, k=2)

#     # Apply Lowe's ratio test to select good matches
#     good_matches = []
#     for m, n in matches:
#         if m.distance < 0.7 * n.distance:
#             good_matches.append(m)

#     # Calculate the similarity score based on the number of good matches
#     similarity_score = len(good_matches) / len(kp1)

#     if similarity_score >= 0.2:  # Adjust the threshold as needed
#         print(f"Signature Matched with {student_name}")
#         signature_matched = True
#         matched_student_name = student_name
#         break  # Exit the loop as soon as a match is found

# # If no match was found with any reference signature
# if not signature_matched:
#     print("No Signature Matched")

# # If you want to keep track of the matched student's name for further use, you can access it from the 'matched_student_name' variable.


import cv2

# Load the captured signature image
captured_signature = cv2.imread(
    r"C:\Users\divyanshi mittal\Desktop\projects\project1\signature.jpg", cv2.IMREAD_GRAYSCALE)

if captured_signature is None:
    print("Error: Captured signature image could not be loaded.")
    exit()  # Exit if the image loading fails

# Create a dictionary to store student names and their reference signatures
student_signatures = {
    "Divyanshi": r"C:\Users\divyanshi mittal\Desktop\projects\project1\student_data\signature1.jpg",
    "Harshit": r"C:\Users\divyanshi mittal\Desktop\projects\project1\student_data\signature2.jpg",
    "Gautam": r"C:\Users\divyanshi mittal\Desktop\projects\project1\student_data\signature3.jpg",
    # Add more students and reference signature file paths as needed
}

# Initialize a flag to check if any reference signature matches
signature_matched = False
matched_student_name = None

# Initialize the SIFT detector
sift = cv2.SIFT_create()

# Define FLANN parameters for matching
index_params = dict(algorithm=0, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)

# Perform image comparison for each student's reference signature
for student_name, reference_signature_path in student_signatures.items():
    reference_signature = cv2.imread(
        reference_signature_path, cv2.IMREAD_GRAYSCALE)
    if reference_signature is None:
        print(
            f"Error: Reference signature image for {student_name} could not be loaded.")
        continue

    # Detect keypoints and compute descriptors using SIFT
    kp1, des1 = sift.detectAndCompute(reference_signature, None)
    kp2, des2 = sift.detectAndCompute(captured_signature, None)

    # Check for valid descriptors
    if des1 is None or des2 is None:
        print(
            f"Skipping {student_name}: No descriptors found in one or both images.")
        continue

    # Match the descriptors using FLANN
    matches = flann.knnMatch(des1, des2, k=2)

    # Apply Lowe's ratio test to select good matches
    good_matches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m)

    # Calculate the similarity score based on the number of good matches
    similarity_score = len(good_matches) / len(kp1) if len(kp1) > 0 else 0

    if similarity_score >= 0.2:  # Adjust the threshold as needed
        print(f"Signature Matched with {student_name}")
        signature_matched = True
        matched_student_name = student_name
        break  # Exit the loop as soon as a match is found

# If no match was found with any reference signature
if not signature_matched:
    print("No Signature Matched")

# Matched student's name can be accessed from 'matched_student_name' if needed
