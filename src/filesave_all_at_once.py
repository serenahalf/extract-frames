"""
Author: Serena Ban
Converts multiple video files into images at once in a specific folder
"""
# python3 -m venv stepper_venv
# source stepper_venv/bin/activate 
# python3 -m pip install opencv-python
import cv2
import os
import itertools
import threading
import time
import sys

frame_interval = 1  # increase to only keep every <frame_interval> th frame
# NOTE: file names are case-insensitive
folder_path = "FOLDER_NAME"  # name of the video

output_folder = f'Result_{folder_path}'  # folder where the output files get saved (created if it doesn't exist already)


def video_to_images() -> None:
    done = False
    # animate function

    def animate():
        for c in itertools.cycle([".", "..", "...", "...."]):
            if done:
                break
            sys.stdout.write('\rConverting ' + c)
            sys.stdout.flush()
            time.sleep(0.5)

    # check if a folder already exists
    # if the folder already exists and there is a possibility of overwriting files within it, warn the user
    if os.path.exists(output_folder):
        answer = input("The output folder already exists! \n"
                        "The folders and files within the folder may get overwritten \n"
                        "Would you like to continue? \n(Y/N)\n")
        while answer.lower() != "y" and answer.lower() != "n":
                print("Please type either Y or N\n")
                answer = input("The folder already exists! \n"
                               "The files within the folder may get overwritten \n"
                               "Would you like to continue? \n(Y/N)\n")
        if answer.lower() == "n":
            print("Program Terminated.")
            return

    t = threading.Thread(target=animate)
    t.daemon = True
    t.start()
    # get the files within the input folder
    lst_contents = sorted(os.listdir(folder_path))

    # create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # check if the file is actually a file
    for i in range(len(lst_contents)):
        fname = lst_contents[i]
        path_to_file = folder_path + "/" + fname
        if os.path.isfile(path_to_file):
            # open the video
            cap = cv2.VideoCapture(path_to_file)
            # check if opened successfully
            if not cap.isOpened():
                print(f"Error: Could not open video file {path_to_file}")
                return

            # parse the file name to create a new sub folder name
            split_lst = fname.split("_")
            new_folder_name = "_".join(split_lst[2:-1])
            sub_folder_output = output_folder + "/" + "Result_" + new_folder_name
            if not os.path.exists(sub_folder_output):
                os.makedirs(sub_folder_output)

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
                    frame_filename = os.path.join(sub_folder_output,
                                                  f"frame_{new_folder_name}_{frame_count:04d}.png")
                    cv2.imwrite(frame_filename, frame)

                frame_count += 1

            # close the opened video
            done = True
            cap.release()
            sys.stdout.write(f"\rFinished! Completed converting the video {fname}.\n")
            if i != len(lst_contents) - 1:
                done = False
                t = threading.Thread(target=animate)
                t.daemon = True
                t.start()


if __name__ == "__main__":
    video_to_images()
