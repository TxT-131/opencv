import cv2
vc = cv2.VideoCapture('少歌剥夺.mp4')
fps = vc.get(cv2.CAP_PROP_FPS)
size = (vc.get(cv2.CAP_PROP_FRAME_WIDTH),
        vc.get(cv2.CAP_PROP_FRAME_HEIGHT))
print('帧速率:',fps)
print('大小:',size)
success, frame = vc.read()
while success:
    cv2.imshow('my video',frame)
    success, frame = vc.read()
    key = cv2.waitKey(25)
    if key == 27:
        break
vc.release()

size=(int(vc.get(cv2.CAP_PROP_FRAME_WIDTH)),
      int(vc.get(cv2.CAP_PROP_FRAME_HEIGHT)))