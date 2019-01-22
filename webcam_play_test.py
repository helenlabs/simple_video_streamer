# -*-coding: utf-8 -*-


import ffmpeg

stream = ffmpeg.input('temp/pipaek.avi')
# stream = ffmpeg.input('webcam')
stream = ffmpeg.filter_(stream,'drawtext',fontfile="fonts/hack/Hack-Regular.ttf",text="%{pts}",box='1', boxcolor='0x00000000@1', fontcolor='white')
stream = ffmpeg.output(stream, 'temp/output6.mp4')
ffmpeg.run(stream)


# import cv2
#
# cap = cv2.VideoCapture(0)
#
# fourcc = cv2.VideoWriter_fourcc(*'DIVX')
# out = cv2.VideoWriter('output.avi', fourcc, 25.0, (640,480))
#
# while (cap.isOpened()):
#     ret, frame = cap.read()
#
#     if ret:
#         # 이미지 반전,  0:상하, 1 : 좌우
#         frame = cv2.flip(frame, 1)
#
#         out.write(frame)
#
#         cv2.imshow('frame', frame)
#
#         if cv2.waitKey(0) & 0xFF == ord('q'):
#             break
#     else:
#         break
#
# cap.release()
# out.release()
# cv2.destroyAllWindows()