#https://github.com/BVLC/caffe/blob/80f44100e19fd371ff55beb3ec2ad5919fb6ac43/python/classify.py
#https://github.com/BVLC/caffe/blob/80f44100e19fd371ff55beb3ec2ad5919fb6ac43/python/caffe/classifier.py
#https://github.com/BVLC/caffe/blob/master/examples/net_surgery.ipynb

import os
import numpy as np
import sys
import argparse
import glob
import time
import caffe

if(len(sys.argv)<6):
    print "python pca_2d.py <IMAGES_FOLDER> <DEPLOY_PROTOTXT> <CAFFE_MODEL> <MEAN_NPY> <POSTFIX>"
    sys.exit()
    
IMAGES_FOLDER= sys.argv[1]
DEPLOY_PROTOTXT= sys.argv[2]
CAFFE_MODEL= sys.argv[3]
MEAN_NPY= sys.argv[4]
POSTFIX= sys.argv[5]

ext=tuple([".jpg",".png",".tif",".bmp"])
os.environ['GLOG_minloglevel'] = '2'
#caffe.set_mode_cpu()
caffe.set_mode_gpu()

net = caffe.Net(DEPLOY_PROTOTXT,
                CAFFE_MODEL,
                caffe.TEST)
               
print("blobs {}\nparams {}".format(net.blobs.keys(), net.params.keys()))

# configure preprocessing
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_mean('data', np.load(MEAN_NPY).mean(1).mean(1))
transformer.set_transpose('data', (2,0,1))
transformer.set_channel_swap('data', (2,1,0))
transformer.set_raw_scale('data', 255.0)

#change the batch size
net.blobs['data'].reshape(1,3,227,227)
    
def extract_features(image_path):
    im = caffe.io.load_image(image_path)
    net.blobs['data'].data[...] = transformer.preprocess('data', im)

    out= net.forward()

    #print "net.blobs['fc7'].data.shape", net.blobs['fc7'].data.shape
    features= np.squeeze(net.blobs['fc7'].data)
    #print "features.shape", features.shape
    
    return features
    
def extract_features_folder(images_folder):
    n_images=0
    n_failed_images=0
    n_folders=0
    n_empty_folders=0
 
    for item in os.listdir(images_folder):
        subdir= os.path.join(images_folder,item)
        if(os.path.isdir(subdir)):
            print 'subdir', subdir
            
            n_folders=n_folders+1
            
            if(len(os.listdir(subdir))==0):
               n_empty_folders=n_empty_folders+1 
            
            for filename in os.listdir(subdir):
                full_filename= os.path.join(subdir,filename)
                if(os.path.isfile(full_filename) and full_filename.endswith(ext)):
                    try:
                        print 'full_filename', full_filename
        
                        features= extract_features(full_filename)
                        
                        features_filename= os.path.splitext(full_filename)[0]+'_'+POSTFIX+'.npy'
                                        
                        print 'features_filename', features_filename
                        
                        np.save(features_filename, features)
                        
                        n_images= n_images+1
                    except: 
                        with open('failed_images_'+POSTFIX+'.txt', "a") as f:
                            full_filename= full_filename+'/n'
                            f.write(full_filename)
                            
                        n_failed_images=n_failed_images+1


                    
                    
    print 'n_images', n_images-n_failed_images,'/',n_images
    print 'n_folders', n_folders-n_empty_folders, '/', n_folders   
    
extract_features_folder(IMAGES_FOLDER)
