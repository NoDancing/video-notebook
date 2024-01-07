import cv2

# This was my first attempt to get the video to play.
# It works concurrently with the command line,
# but the sound does not play, and the video plays at the wrong speed.

def play_video(video_path):
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    play_video('testvideo.mkv')