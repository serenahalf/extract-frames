"""
Author: Serena Ban
Converts video file into images
"""
import cv2
import os

frame_interval = 1  # increase to only keep every <frame_interval> th frame
# NOTE: file names are case-insensitive
base_name = "INPUT VIDEO NAME"  # change this accordingly
video_path = f'{base_name}.h264'  # name of the video
output_folder = f'Result_{base_name}'  # folder where the output files get saved (created if it doesn't exist already)
overwrite_checker = f"frame_{base_name}"  # to prevent possible overwrite


def video_to_images() -> None:
    # check if a folder already exists
    # if the folder already exists and there is a possibility of overwriting files within it, warn the user
    if os.path.exists(output_folder):
        keyword = overwrite_checker
        check = False
        for fname in os.listdir(output_folder):
            if keyword.lower() in fname.lower():
                check = True
        if check:
            answer = input("The folder already exists! \n"
                           "The files within the folder may get overwritten "
                           "if you haven't changed the <file_base_name>. \n"
                           "Would you like to continue? \n(Y/N)\n")
            while answer.lower() != "y" and answer.lower() != "n":
                print("Please type either Y or N\n")
                answer = input("The folder already exists! \n"
                               "The files within the folder may get overwritten "
                               "if you haven't changed the <file_base_name>. \n"
                               "Would you like to continue? \n(Y/N)\n")
            if answer.lower() == "n":
                print("Program Terminated.")
                return

    # open the video
    cap = cv2.VideoCapture(video_path)

    # make the output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # check if opened successfully
    if not cap.isOpened():
        print(f"Error: Could not open video file {video_path}")
        return

    # frame counter
    frame_count = 0

    # extract every frame
    while True:
        ret, frame = cap.read()

        # break if no more frame
        if not ret:
            break

        # skipping logic
        if frame_count % frame_interval == 0:
            frame_filename = os.path.join(output_folder, f"{overwrite_checker}_{frame_count:04d}.png")
            cv2.imwrite(frame_filename, frame)
            print(f"Saved {frame_filename}")

        frame_count += 1

    # close the opened video
    cap.release()
    print(f"Finished! Extracted {frame_count} frames.")


if __name__ == "__main__":
    video_to_images()
