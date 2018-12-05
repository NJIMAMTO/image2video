import glob
import cv2

path = "/media/mokugyo/ボリューム/3Dface"
folder = ["F_Angry","F_Disugust","F_Fear","F_Happy","F_Neutral","F_Surprise","F_Unhappy",
        "M_Angry","M_Disgust","M_Fear","M_Happy","M_Neutral","M_Surprise","M_Unhappy"]
V_S = ["V0S","V2L"]
E_S = ["_A","_D","_F","_H","_N","_S","_U"] 

fourcc = cv2.VideoWriter_fourcc('m','p','4','v')

for i in range(0,14):
        for x in range(0, 2):
                #対象文字列(*V_S*)を含むファイルを検索し一覧を取得
                files = glob.glob(path + "/" + folder[i] + "/*"+ V_S[x] + E_S[i%7] +"*.JPG")
                #videoを作成
                video = cv2.VideoWriter( path + "/" + folder[i] + "/" + V_S[x] + E_S[i%7] + '.mp4', fourcc, 30.0, (1200, 1200))
    
                length = len(files)
                #取得したファイル名から画像を読み込み動画化する
                for y in range(0,length):
                        img = cv2.imread(files[y])
                        video.write(img)
                video.release()
