# Two-Sigma-Connect-Rental-Listing-Inquiries-Feature-Visualization

Feature visualization for Two Sigma Connect: Rental Listing Inquiries
- https://www.kaggle.com/c/two-sigma-connect-rental-listing-inquiries

I have used pretrained AlexNet models one of which was trained on ImageNet database and another finetuned on MIT Places database.

This example depends on caffe with python interface(for feature extraction) and sklearn(for pca and t-sne projection).

Network weights can be downloaded from:
- https://github.com/BVLC/caffe/tree/master/models/bvlc_alexnet
- http://places.csail.mit.edu/downloadCNN.html

Results:
![alt tag](https://github.com/mrgloom/Two-Sigma-Connect-Rental-Listing-Inquiries-Feature-Visualization/blob/master/feature_extraction_example/misc/pca_2d_alexnet_imagenet.png)
![alt tag](https://github.com/mrgloom/Two-Sigma-Connect-Rental-Listing-Inquiries-Feature-Visualization/blob/master/feature_extraction_example/misc/pca_2d_alexnet_mit_places.png)
![alt tag](https://github.com/mrgloom/Two-Sigma-Connect-Rental-Listing-Inquiries-Feature-Visualization/blob/master/feature_extraction_example/misc/t_sne_2d_alexnet_imagenet.png)
![alt tag](https://github.com/mrgloom/Two-Sigma-Connect-Rental-Listing-Inquiries-Feature-Visualization/blob/master/feature_extraction_example/misc/t_sne_2d_alexnet_mit_places.png)

