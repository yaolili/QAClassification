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
# print "sys.argv[11]: hasUrl file"

#train feature vector
python getFeatureVector.py  ../pre/trainDirectory_2/ ../w2v/w2vTrain.vector 200 ../topicModel/trainDocTopics30.txt 30 ../info/qcInfo.train ../result/formatResult11D7_4.txt ../tfidf/tfidfTrain.txt ../order/prefixTrain.txt 0 hasUrlTrain.txt

echo "train feature done!"

#dev feature vector
python getFeatureVectorDev.py ../pre/devDirectory/ ../w2v/w2vDev.vector 200 ../topicModel/devDocTopics30.txt 30 ../info/qcInfo.dev ../result/formatResultDev11D7_4.txt ../tfidf/tfidfDev.txt ../order/prefixDev.txt 1 hasUrlDev.txt categoryAnsProTrain.txt
echo "dev feature done!"

#test feature vector
# python getFeatureVectorDev.py ../pre/testDirectory/ ../w2v/w2vTest.vector 200 ../topicModel/testDocTopics30.txt 30 ../info/qcInfo.test ../result/formatResultTest11D7_4.txt ../tfidf/tfidfTest.txt ../order/prefixTest.txt 1 hasUrlTest.txt categoryAnsProTrain.txt

# echo "test feature done!"

# print "sys.argv[1]: classifier"
# print "sys.argv[2]: trainFile"
# print "sys.argv[3]: devFile"
# print "sys.argv[4]: outputFile"

echo "===============dev===================="
#classification for dev
python runClassification.py gbdt ../result/formatResult11D7_4.txt ../result/formatResultDev11D7_4.txt ../order/labelDevGBDT11D7_4.txt

echo "gbdt classification done!"

python runClassification.py svm ../result/formatResult11D7_4.txt ../result/formatResultDev11D7_4.txt ../order/labelDevSVM11D7_4.txt

echo "svm classification done!"

python runClassification.py knn ../result/formatResult11D7_4.txt ../result/formatResultDev11D7_4.txt ../order/labelDevKNN11D7_4.txt

echo "knn classification done!"

python runClassification.py essemble ../result/formatResult11D7_4.txt ../result/formatResultDev11D7_4.txt ../order/labelDevESSEMBLE11D7_4.txt

echo "essemble classification done!"

python runClassification.py tree ../result/formatResult11D7_4.txt ../result/formatResultDev11D7_4.txt ../order/labelDevTREE11D7_4.txt

echo "tree classification done!"

# print "sys.argv[1]: prefix order file"
# print "sys.argv[2]: label order file"
# print "sys.argv[3]: output file"

#get dev prediction result
python dealResult.py ../order/prefixDev.txt ../order/labelDevGBDT11D7_4.txt ../devPredict/devGBDT11D7_4.txt

echo "gbdt prediction done!"

python dealResult.py ../order/prefixDev.txt ../order/labelDevSVM11D7_4.txt ../devPredict/devSVM11D7_4.txt

echo "svm prediction done!"

python dealResult.py ../order/prefixDev.txt ../order/labelDevKNN11D7_4.txt ../devPredict/devKNN11D7_4.txt

echo "knn prediction done!"

python dealResult.py ../order/prefixDev.txt ../order/labelDevESSEMBLE11D7_4.txt ../devPredict/devESSEMBLE11D7_4.txt

echo "essemble prediction done!"

python dealResult.py ../order/prefixDev.txt ../order/labelDevTREE11D7_4.txt ../devPredict/devTREE11D7_4.txt

echo "tree prediction done!"


# print "sys.argv[1]: classifier"
# print "sys.argv[2]: trainFile"
# print "sys.argv[3]: testFile"
# print "sys.argv[4]: outputFile"

# echo "===============test===================="

# #classification for test
# python runClassification.py gbdt ../result/formatResult11D7_4.txt ../result/formatResultTest11D7_4.txt ../order/labelTestGBDT11D7_4.txt

# echo "gbdt classification done!"

# python runClassification.py svm ../result/formatResult11D7_4.txt ../result/formatResultTest11D7_4.txt ../order/labelTestSVM11D7_4.txt

# echo "svm classification done!"

# python runClassification.py knn ../result/formatResult11D7_4.txt ../result/formatResultTest11D7_4.txt ../order/labelTestKNN11D7_4.txt

# echo "knn classification done!"

# python runClassification.py essemble ../result/formatResult11D7_4.txt ../result/formatResultTest11D7_4.txt ../order/labelTestESSEMBLE11D7_4.txt

# echo "essemble classification done!"

# python runClassification.py tree ../result/formatResult11D7_4.txt ../result/formatResultTest11D7_4.txt ../order/labelTestTREE11D7_4.txt

# echo "tree classification done!"
    
    
# #get test prediction result
# python dealResult.py ../order/prefixTest.txt ../order/labelTestGBDT11D7_4.txt ../testPredict/testGBDT.txt

# echo "gbdt prediction done!"

# python dealResult.py ../order/prefixTest.txt ../order/labelTestSVM11D7_4.txt ../testPredict/testSVM.txt

# echo "svm prediction done!"

# python dealResult.py ../order/prefixTest.txt ../order/labelTestKNN11D7_4.txt ../testPredict/testKNN11D7_4.txt

# echo "knn prediction done!"

# python dealResult.py ../order/prefixTest.txt ../order/labelTestESSEMBLE11D7_4.txt ../testPredict/testESSEMBLE11D7_4.txt

# echo "essemble prediction done!"

# python dealResult.py ../order/prefixTest.txt ../order/labelTestTREE11D7_4.txt ../testPredict/testTREE11D7_4.txt

# echo "tree prediction done!" 
