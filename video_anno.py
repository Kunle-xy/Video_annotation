import cv2
import json
import shutil
import sys
# import


#TODO:  1. write a script that automatically saves images from videos
    #   2.  Dockerize for usage on other platform

def video_process(file: str):

  cap = cv2.VideoCapture(file)

  if (cap.isOpened() == False):
    print("Unable to read camera feed")

  frame_width = int(cap.get(3))
  frame_height = int(cap.get(4))


  record = False
  i = 0
  while(True):
    ret, frame = cap.read()
    k = cv2.waitKey(1)

    if ret == True:
      cv2.imshow('frame',frame)

      # # press space key to start save
      if k%256 == 32:
          cv2.waitKey(-1)


      # TODO: works for pause and play
      if k == ord("s"):
        cv2.imwrite('image'+str(i)+'.jpg',frame)
        i += 1

      # press q key to close the program
      if k & 0xFF == ord('q'):
          break

    else:
      break

  cap.release()
  # out.release()

  cv2.destroyAllWindows()

if __name__ == "__main__":
  try:
    file = sys.argv[1]
  except Exception as e:
    sys.exit("no video path")
  video_process(file)
