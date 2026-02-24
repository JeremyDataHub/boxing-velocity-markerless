"""
Video Frame Extractor

Extracts a single frame from a video file and saves it as an image.
Used to generate calibration images from GoPro recordings for Pose2Sim.

Author : Jérémy Birba
Project: REVEA — M2S Laboratory × French Boxing Federation
"""

import cv2


def extract_frame(video_path: str, frame_number: int, output_path: str) -> None:
    """Extract a specific frame from a video and save it as an image.

    Args:
        video_path: Path to the input video file.
        frame_number: Index of the frame to extract (0-based).
        output_path: Path where the extracted frame will be saved.

    Returns:
        None. Saves the frame to disk if successful.
    """
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: could not open video at {video_path}")
        return

    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    ret, frame = cap.read()

    if ret:
        cv2.imwrite(output_path, frame)
        print(f"Frame {frame_number} saved to {output_path}")
    else:
        print(f"Error: could not read frame {frame_number}")

    cap.release()


if __name__ == "__main__":

    VIDEO_PATH = "videos/cam01.mp4"
    FRAME_NUMBER = 28531
    OUTPUT_PATH = "calibration/extrinsics/ext_cam01_img/ext_cam01_img.png"

    extract_frame(VIDEO_PATH, FRAME_NUMBER, OUTPUT_PATH)
