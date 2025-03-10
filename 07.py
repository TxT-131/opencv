import cv2
vc = cv2.VideoCapture('tomolin.mp4')
fps = vc.get(cv2.CAP_PROP_FPS)
size = (int(vc.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT)))
vw = cv2.VideoWriter('.venv/test1.avi',
                     cv2.VideoWriter_fourcc('X','V','I','D'),
                     fps, size)
success, frame = vc.read()
while success:
    vw.write(frame)
    success, frame = vc.read()
vc.release()