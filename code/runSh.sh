#!/bin/sh
# AUTHOR:   yaolili
# FILE:     runSh.sh
# ROLE:     TODO (some explanation)
# CREATED:  2015-12-14 09:12:56
# MODIFIED: 2015-12-14 09:13:04


# print "sys.argv[1]: original file path!"
# print "sys.argv[2}: w2v file"
# print "sys.argv[3]: w2v dimension"
# print "sys.argv[4]: topic model file"
# print "sys.argv[5]: topic model dimension"
# print "sys.argv[6]: qcInfo"
# print "sys.argv[7]: format result file"
# print "sys.argv[8]: tfidf file"
# print "sys.argv[9]: prefix order file"

#train feature vector
python getFeatureVector.py  ../pre/trainDirectory_2/ ../w2v/w2vTrain.vector 200 ../topicModel/trainDocTopics30.txt 30 ../info/qcInfo.train ../result/formatResult12D_4Double.txt ../tfidf/tfidfTrain.txt ../order/prefixTrain_45.txt 0

echo "train feature done!"

#dev feature vector
python getFeatureVector.py ../pre/devDirectory/ ../w2v/w2vDev.vector 200 ../topicModel/devDocTopics30.txt 30 ../info/qcInfo.dev ../result/formatResultDev12D_4Double.txt ../tfidf/tfidfDev.txt ../order/prefixDev_45.txt 1

echo "dev feature done!"

# print "sys.argv[1]: classifier"
# print "sys.argv[2]: trainFile"
# print "sys.argv[3]: devFile"
# print "sys.argv[4]: outputFile"


#classification
python runClassification.py gbdt ../result/formatResult12D_4Double.txt ../result/formatResultDev12D_4Double.txt ../order/labelDevGBDT_45.txt

echo "gbdt classification done!"

python runClassification.py svm ../result/formatResult12D_4Double.txt ../result/formatResultDev12D_4Double.txt ../order/labelDevSVM_45.txt

echo "svm classification done!"

python runClassification.py knn ../result/formatResult12D_4Double.txt ../result/formatResultDev12D_4Double.txt ../order/labelDevKNN_45.txt

echo "knn classification done!"

python runClassification.py essemble ../result/formatResult12D_4Double.txt ../result/formatResultDev12D_4Double.txt ../order/labelDevESSEMBLE_45.txt

echo "essemble classification done!"

python runClassification.py tree ../result/formatResult12D_4Double.txt ../result/formatResultDev12D_4Double.txt ../order/labelDevTREE_45.txt

echo "tree classification done!"

# print "sys.argv[1]: prefix order file"
# print "sys.argv[2]: label order file"
# print "sys.argv[3]: output file"


#get dev prediction result
python dealResult.py ../order/prefixDev_45.txt ../order/labelDevGBDT_45.txt ../devPredict/devGBDT_45.txt

echo "gbdt prediction done!"

python dealResult.py ../order/prefixDev_45.txt ../order/labelDevSVM_45.txt ../devPredict/devSVM_45.txt

echo "svm prediction done!"

python dealResult.py ../order/prefixDev_45.txt ../order/labelDevKNN_45.txt ../devPredict/devKNN_45.txt

echo "knn prediction done!"

python dealResult.py ../order/prefixDev_45.txt ../order/labelDevESSEMBLE_45.txt ../devPredict/devESSEMBLE_45.txt

echo "essemble prediction done!"

python dealResult.py ../order/prefixDev_45.txt ../order/labelDevTREE_45.txt ../devPredict/devTREE_45.txt

echo "tree prediction done!"
    
    
