from PIL import Image
import os

path="./val/"
save_path="./val_cropped/"

for i in os.listdir(path+"A"):
    imgA=Image.open(path+"A/"+i)
    imgB=Image.open(path+"B/"+i)
    label=Image.open(path+"label/"+i)

    j=0
    for x in range(4):
        for y in range(4):
            cropped_A=imgA.crop((x*256,y*256,(x+1)*256,(y+1)*256))
            cropped_B=imgB.crop((x*256,y*256,(x+1)*256,(y+1)*256))
            cropped_label=label.crop((x*256,y*256,(x+1)*256,(y+1)*256))
            cropped_A.save(save_path+"A/"+i.split(".")[0]+"_"+str(j)+".png")
            cropped_B.save(save_path+"B/"+i.split(".")[0]+"_"+str(j)+".png")
            cropped_label.save(save_path+"label/"+i.split(".")[0]+"_"+str(j)+".png")
            j+=1
    
            