import cv2
import os


def save_frames(video_path, frame_num, dir_path, basename, ext='jpg'):
    print('Start! ({})'.format(video_path))
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print('ERROR: Could not open video file.')
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    total_frame = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    step_frame = int(total_frame / frame_num)
    digit = len(str(frame_num))

    count = 1

    for n in range(0, total_frame, step_frame):
        if count > frame_num:
            print('Completed! ({})'.format(dir_path))
            return
        cap.set(cv2.CAP_PROP_POS_FRAMES, n)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path, str(count).zfill(digit), ext), frame)
            print('{}/{}'.format(count, frame_num))
            count += 1
        else:
            print('Completed! ({})'.format(dir_path))
            return


save_frames('path/to/video', 10, 'path/to/save/dir', 'basename')
