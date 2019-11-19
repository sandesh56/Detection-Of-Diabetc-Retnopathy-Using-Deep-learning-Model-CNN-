

# As we know in kaggale datasets images of all laebel are placed inside same folder Train. This notebook is for splitting datasets to respective class folder
# Download datasets and csv file from kaggle 


import pandas as pd

df=pd.read_csv('/content/trainLabels.csv') # reads csv file
df.head() # displays metadata formate


#As shown above zipping two heads of metadata. This is becouse our actual images in datasets has the same name as zipped down.
images = df['image']
levels = df['level']
imglevel = list(zip(images, levels))



#to execute this code you must have training images at folder Train
from tqdm import tqdm
import shutil
for img in tqdm(imglevel):
  if img[1] ==0:
    shutil.copy2(os.path.join('/content/Train/', img[0] + '.jpg'), os.path.join('/content/test/level0', img[0] + '.jpg')) #copies images of level0 from Train to test
  elif img[1] == 1:
    shutil.copy2(os.path.join('/content/Train/', img[0] + '.jpeg'), os.path.join('/content/test/level1/', img[0] + '.jpeg'))
  elif img[1] == 2:
    shutil.copy2(os.path.join('/content/Train/', img[0] + '.jpeg'), os.path.join('/content/test/level2/', img[0] + '.jpeg'))
  elif img[1] == 3:
    shutil.copy2(os.path.join('/content/Train/', img[0] + '.jpeg'), os.path.join('/content/test/level3/', img[0] + '.jpeg'))
  elif img[1] == 4:
    shutil.copy2(os.path.join('/content/Train/', img[0] + '.jpeg'), os.path.join('/content/test/level4/', img[0] + '.jpeg'))
  else:
    print('Error')
