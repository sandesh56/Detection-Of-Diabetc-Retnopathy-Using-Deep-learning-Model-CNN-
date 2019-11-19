# code to transfer content of one folder to other.
import shutil
import os
images0 = os.listdir('/content/remake/level3') #provide path of source folder here
for i,img in enumerate(images0[:20]):
   shutil.move(os.path.join('/content/remake/level3/', img), os.path.join('/content/remake/level4', img))
