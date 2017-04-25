import os
import sys
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

if(len(sys.argv)<4):
    print "python t_sne_2d.py <IMAGE_SAMPLES_CLASSES_DIR> <IMAGE_SAMPLES_DIR> <POSTFIX>"
    sys.exit()
    
IMAGE_SAMPLES_CLASSES_DIR= sys.argv[1]
IMAGE_SAMPLES_DIR= sys.argv[2]
POSTFIX= sys.argv[3]

def load_txt(filename):
    array = []
    with open(filename, "r") as ins:
        for line in ins:
            array.append(line)
    
    print 'len(array)', len(array)
    
    arr_X = []
    arr_labels = []
    for line in array:       
        img_filename= line.split()[0]
        tokens = img_filename.split(os.sep)
        filename= IMAGE_SAMPLES_DIR+os.sep+tokens[2]+os.sep+tokens[3].split('.')[0]+'_'+POSTFIX+'.npy'
        features= np.load(filename)
        label= int(line.split()[1])
        
        arr_X.append(features)
        arr_labels.append(label)
   
    print 'len(arr_X)', len(arr_X)
    print 'len(arr_labels)', len(arr_labels)

    X= np.array(arr_X)
    y= np.array(arr_labels)
    
    print X.shape
    print y.shape
    
    return X,y
    
def load_data():
    arr_X = []
    arr_y = []
    for filename in os.listdir(IMAGE_SAMPLES_CLASSES_DIR):
        full_filename= os.path.join(IMAGE_SAMPLES_CLASSES_DIR,filename)
        if(os.path.isfile(full_filename) and full_filename.endswith(".txt")):
            print 'list_filename', full_filename

            X,y= load_txt(full_filename)
            
            arr_X.append(X)
            arr_y.append(y)
            
            
    X= np.concatenate(arr_X)
    y= np.concatenate(arr_y)
    
    print 'X.shape', X.shape
    print 'y.shape', y.shape
    
    return X,y

def project_2d(X,y):
    model = TSNE(n_components=2, random_state=0)
    X_proj= model.fit_transform(X)
    
    print 'X_proj.shape',X_proj.shape
    
    legend_patches= []
    names= ['room','outdoor','scheme','bathroom', 'kitchen'] #hardcoded!
    colors=['green','blue','gray','red','yellow']
    k=0
    for name in names:
        legend_patches.append(mpatches.Patch(color=colors[k], label=name))
        k=k+1
           
    plt.legend(handles=legend_patches)
    
    color_arr=[]
    for i in range(0,y.shape[0]):
        color_arr.append(colors[y[i]])
        
    plt.scatter(X_proj[:,0], X_proj[:,1], c=color_arr)
    plt.savefig('t_sne_2d_'+POSTFIX+'.png')
    
X,y= load_data()
project_2d(X,y)
