import glob
import cv2

path = "/media/mokugyo/ボリューム/3Dface/"
folder = ["F_Angry","F_Disugust","F_Fear","F_Happy","F_Neutral","F_Surprise","F_Unhappy",
        "M_Angry","M_Disgust","M_Fear","M_Happy","M_Neutral","M_Surprise","M_Unhappy"]
V_search = ["V0S","V2L"]
E_search = ["_A","_D","_F","_H","_N","_S","_U"] 

for i in range(0,14):
    files = glob.glob(path + folder[i] + "/" + "*"+ V_search +"*")

fourcc = cv2.VideoWriter_fourcc('m','p','4','v')ter(path + 'V0S_F.mp4', fourcc, 30.0, (1200, 1200))

length = len(files)

for i in range(0,length):
    img = cv2.imread(files[i])
    video.write(img)
video.release()
