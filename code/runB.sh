#!/bin/sh
# AUTHOR:   yaolili
# FILE:     runB.sh
# ROLE:     TODO (some explanation)
# CREATED:  2015-12-17 11:07:14
# MODIFIED: 2015-12-17 11:07:43

echo "=================dev classification==================="

python runClassification.py gbdt data/yn/formatResult/finalFormat/baseQAllFeature_train.txt data/yn/formatResult/finalFormat/baseQAllFeature_dev.txt data/yn/order/orderYNDevGBDT.txt

python runClassification.py essemble data/yn/formatResult/finalFormat/baseQAllFeature_train.txt data/yn/formatResult/finalFormat/baseQAllFeature_dev.txt data/yn/order/orderYNDevESSEMBLE.txt

python runClassification.py tree data/yn/formatResult/finalFormat/baseQAllFeature_train.txt data/yn/formatResult/finalFormat/baseQAllFeature_dev.txt data/yn/order/orderYNDevTREE.txt

python runClassification.py knn data/yn/formatResult/finalFormat/baseQAllFeature_train.txt data/yn/formatResult/finalFormat/baseQAllFeature_dev.txt data/yn/order/orderYNDevKNN.txt

python runClassification.py svm data/yn/formatResult/finalFormat/baseQAllFeature_train.txt data/yn/formatResult/finalFormat/baseQAllFeature_dev.txt data/yn/order/orderYNDevSVM.txt

echo "=================dev prediction result==================="

python dealResultYN.py data/yn/prefix/prefixDevYN.txt data/yn/order/orderYNDevGBDT.txt data/yn/devPredict/devGBDTYN.txt

python dealResultYN.py data/yn/prefix/prefixDevYN.txt data/yn/order/orderYNDevESSEMBLE.txt data/yn/devPredict/devESSEMBLEYN.txt

python dealResultYN.py data/yn/prefix/prefixDevYN.txt data/yn/order/orderYNDevTREE.txt data/yn/devPredict/devTREEYN.txt

python dealResultYN.py data/yn/prefix/prefixDevYN.txt data/yn/order/orderYNDevKNN.txt data/yn/devPredict/devKNNYN.txt

python dealResultYN.py data/yn/prefix/prefixDevYN.txt data/yn/order/orderYNDevSVM.txt data/yn/devPredict/devSVMYN.txt
