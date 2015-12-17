#!/bin/sh
# AUTHOR:   yaolili
# FILE:     runSh.sh
# ROLE:     run all command
# CREATED:  2015-12-14 09:12:56
# MODIFIED: 2015-12-14 09:13:04


#train feature vector
python getFeatureVector.py  ../pre/trainDirectory/ data/w2v/w2vTrain.vector 200 data/topicModel/trainDocTopics30.txt 30 data/qcInfo/qcInfo.train ../result/formatResult12D_4.txt data/tfidf/tfidfTrain.txt data/order/prefixTrain.txt 0 data/url/hasUrlTrain.txt data/categoryAnsProTrain.txt

echo "train feature done!"

#dev feature vector
python getFeatureVector.py  ../pre/devDirectory/ data/w2v/w2vDev.vector 200 data/topicModel/devDocTopics30.txt 30 data/qcInfo/qcInfo.dev ../result/formatResultDev12D_4.txt data/tfidf/tfidfDev.txt data/order/prefixDev.txt 1 data/url/hasUrlDev.txt data/categoryAnsProTrain.txt

echo "dev feature done!"

#test feature vector
python getFeatureVector.py  ../pre/testDirectory/ data/w2v/w2vTest.vector 200 data/topicModel/testDocTopics30.txt 30 data/qcInfo/qcInfo.test ../result/formatResultTest12D_4.txt data/tfidf/tfidfTest.txt data/order/prefixTest.txt 1 data/url/hasUrlTest.txt data/categoryAnsProTrain.txt

echo "test feature done!"

echo "===============dev classification================="

#classification for dev
python runClassification.py gbdt ../result/formatResult12D_4.txt ../result/formatResultDev12D_4.txt data/order/labelDevGBDT12D_4.txt

echo "gbdt classification done!"

python runClassification.py svm ../result/formatResult12D_4.txt ../result/formatResultDev12D_4.txt data/order/labelDevSVM12D_4.txt

echo "svm classification done!"

python runClassification.py knn ../result/formatResult12D_4.txt ../result/formatResultDev12D_4.txt data/order/labelDevKNN12D_4.txt

echo "knn classification done!"

python runClassification.py essemble ../result/formatResult12D_4.txt ../result/formatResultDev12D_4.txt data/order/labelDevESSEMBLE12D_4.txt

echo "essemble classification done!"

python runClassification.py tree ../result/formatResult12D_4.txt ../result/formatResultDev12D_4.txt data/order/labelDevTREE12D_4.txt

echo "tree classification done!"


#get dev prediction result
python dealResult.py data/order/prefixDev.txt data/order/labelDevGBDT12D_4.txt ../devPredict/devGBDT12D_4.txt

echo "gbdt prediction done!"

python dealResult.py data/order/prefixDev.txt data/order/labelDevSVM12D_4.txt ../devPredict/devSVM12D_4.txt

echo "svm prediction done!"

python dealResult.py data/order/prefixDev.txt data/order/labelDevKNN12D_4.txt ../devPredict/devKNN12D_4.txt

echo "knn prediction done!"

python dealResult.py data/order/prefixDev.txt data/order/labelDevESSEMBLE12D_4.txt ../devPredict/devESSEMBLE12D_4.txt

echo "essemble prediction done!"

python dealResult.py data/order/prefixDev.txt data/order/labelDevTREE12D_4.txt ../devPredict/devTREE12D_4.txt

echo "tree prediction done!"


echo "===============test classification================="

#classification for test
python runClassification.py gbdt ../result/formatResult12D_4.txt ../result/formatResultTest12D_4.txt data/order/labelTestGBDT12D_4.txt

echo "gbdt classification done!"

python runClassification.py svm ../result/formatResult12D_4.txt ../result/formatResultTest12D_4.txt data/order/labelTestSVM12D_4.txt

echo "svm classification done!"

python runClassification.py knn ../result/formatResult12D_4.txt ../result/formatResultTest12D_4.txt data/order/labelTestKNN12D_4.txt

echo "knn classification done!"

python runClassification.py essemble ../result/formatResult12D_4.txt ../result/formatResultTest12D_4.txt data/order/labelTestESSEMBLE12D_4.txt

echo "essemble classification done!"

python runClassification.py tree ../result/formatResult12D_4.txt ../result/formatResultTest12D_4.txt data/order/labelTestTREE12D_4.txt

echo "tree classification done!"
    
    
#get test prediction result
python dealResult.py data/order/prefixTest.txt data/order/labelTestGBDT12D_4.txt ../testPredict/testGBDT12D_4.txt

echo "gbdt prediction done!"

python dealResult.py data/order/prefixTest.txt data/order/labelTestSVM12D_4.txt ../testPredict/testSVM12D_4.txt

echo "svm prediction done!"

python dealResult.py data/order/prefixTest.txt data/order/labelTestKNN12D_4.txt ../testPredict/testKNN12D_4.txt

echo "knn prediction done!"

python dealResult.py data/order/prefixTest.txt data/order/labelTestESSEMBLE12D_4.txt ../testPredict/testESSEMBLE12D_4.txt

echo "essemble prediction done!"

python dealResult.py data/order/prefixTest.txt data/order/labelTestTREE12D_4.txt ../testPredict/testTREE12D_4.txt

echo "tree prediction done!" 
