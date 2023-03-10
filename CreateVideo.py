import os
import cv2

path = "C:/Users/warri/Downloads/project105/Images"
images = []
count = 0

for img in os.listdir(path):
    nam, ext = os.path.splitext(img)
    if ext in ['.gif','.png','.jpg','.jpeg','.jfif']:
        img_name = path + '/' + img
        print(img_name)
        images.append(img_name)
        count += 1

frame = cv2.imread(images[0])
height,width,channels = frame.shape
size = (width, height)
print(size)

out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)
for i in range(0,count-1):
    fr = cv2.imread(images[i])
    out.write(fr)

out.release()
print("Done")


#vid = cv2.VideoCapture('project.avi')

#while True:
#    ret, fra = vid.read()
#    cv2.imshow("project.avi", fra)
#    if cv2.waitKey(1000) == 32:
#        break

#vid.release()
#cv2.destroyAllWindows()
