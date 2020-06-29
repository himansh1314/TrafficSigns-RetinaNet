# TrafficSigns-RetinaNet
Traffic sign detection by training RetinaNet on GTSDB dataset

# Requirements
> - tensorflow-gpu
> - keras
> - matplotlib

# Files included
> - train.ipynb for training retinanet on GTSDB.
> - class_to_label.py is used for creating csv file where classes are mapped to labels.
> - convert_csv.py is used to convert gt.txt file to csv along with replacing ';' with ',' to make it compatible for .csv file format.
> - preprocess_csv.py  is used for preprocessing the csv file provided by GTSDB dataset. Should be used only after replacing ':' with commas in the file. File for the same included.

# Results
It is advised to train this model on google colab's GPU as training takes a very long time, even on Colab's GPU, it takes nearly an hour to train for one epoch.
The mean Average Precision of the trained model after 10 epochs was 0.48, which is just okay. This may be attributed to the fact that there are very less training samples(~900).
A larger dataset may lead to even better results.

# Medium Blog
I will soon be writing a blog on medium about this. Will update the link here when it's done.
