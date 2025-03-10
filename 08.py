import cv2
vc = cv2.VideoCapture(0)
fps = 30
size = (int(vc.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT)))
vw = cv2.VideoWriter('.venv/video.avi',
                     cv2.VideoWriter_fourcc('X','V','I','D'),
                     fps, size)
success,frame = vc.read(0)
while success:
    vw.write(frame)
    cv2.imshow('MyCamera', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
    success, frame = vc.read()
vc.release()