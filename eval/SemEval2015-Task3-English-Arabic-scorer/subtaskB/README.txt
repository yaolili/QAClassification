==============================================================
Scorer for SemEval-2015 Task 3, subtask B, English
"Answer Selection in Community Question Answering"
Version 1.1: October 13, 2014
==============================================================

This file contains the basic information regarding the scorer for Scorer for SemEval-2015 Task 3 "Answer Selection in Community Question Answering", subtask B, English.


[1] LIST OF VERSIONS

  v1.2 [2014/11/20]: fixed an issue when running on Linux
  v1.1 [2014/10/13]: added the output for a majority class baseline
  v1.0 [2014/10/2] : initial version of the scorer


[2] CONTENTS OF THE DISTRIBUTION 1.1

We are providing the following files:

* README.txt 
  this file

* SemEval2015-task3-scorer-subtaskB.pl
  PERL script that implements the scorer

* CQA-QL-devel-gold-yn.txt
  sample GOLD file
  
* CQA-QL-devel-predicted-yn-good.txt
  sample PREDICTIONS file

* CQA-QL-devel-predicted-yn-majority-baseline.txt
  another sample PREDICTIONS file (for the majority baseline)

* SemEval2015-task3-scores-subtaskB.txt
  sample output for the above files

* SemEval2015-task3-scores-subtaskB-majority-baseline.txt
  sample output for CQA-QL-devel-predicted-yn-majority-baseline.txt


[3] USE NOTES

Use:
   SemEval2015-task3-scorer-subtaskB.pl <GOLD_FILE> <PREDICTIONS_FILE>

Example use:
   SemEval2015-task3-scorer-subtaskB.pl CQA-QL-devel-gold-yn.txt CQA-QL-devel-predicted-yn-good.txt > SemEval2015-task3-scores-subtaskB.txt
   SemEval2015-task3-scorer-subtaskB.pl CQA-QL-devel-gold-yn.txt CQA-QL-devel-predicted-yn-majority-baseline.txt > SemEval2015-task3-scores-subtaskB-majority-baseline.txt


[4] LICENSE

This distribution is directly downloadable from the official SemEval-2015 Task 3 website http://alt.qcri.org/semeval2015/task3/index.php?id=data-and-tools

Licensing: 
- the script and all above files are free for general research use 
- you should use the following citation in your publications whenever using this resource:

@InProceedings{nakov-EtAl:2015:SemEval,
  author    = {Nakov, Preslav  and  M\`{a}rquez, Llu\'{i}s  and  Magdy, Walid  and  Moschitti, Alessandro  and  Glass, Jim  and  Randeree, Bilal},
  title     = {{SemEval}-2015 Task 3: Answer Selection in Community Question Answering},
  booktitle = {Proceedings of the 9th International Workshop on Semantic Evaluation},
  series    = {SemEval '15},
  month     = {June},
  year      = {2015},
  address   = {Denver, Colorado},
  publisher = {Association for Computational Linguistics},
  pages     = {269--281},
  url       = {http://www.aclweb.org/anthology/S15-2047}
}



[5] DATA FORMAT, OUTPUT

   The scorer takes as input a proposed classification file and an answer key file.
   Both files should contain one prediction per line in the format "<Question_ID>	<Label>"
   with a TAB as a separator, e.g.,

	Q2601	Yes
	Q2602	No
	Q2603	Unsure
	...

   The files have to be sorted in the same way, i.e., their <Question_ID> should match for each line!
   Repetitions of IDs are not allowed in either of the files.

   The scorer calculates and outputs the following statistics:
      (1) confusion matrix, which shows
			- the count for each gold/predicted pair
         - the sums for each row/column: -SUM-
      (2) accuracy
      (3) precision (P), recall (R), and F1-score for each label
      (4) micro-averaged P, R, F1
      (5) macro-averaged P, R, F1

   
   The official score is the macro-averaged F1-score.


[6] CREDITS

Task Organizers:

    Lluís Màrquez
        Arabic Language Technologies (ALT)
        Qatar Computing Research Institute (QCRI), Qatar
    James Glass (CSAIL, MIT)
    Walid Magdy (ALT-QCRI, Qatar)
    Alessandro Moschitti (ALT-QCRI, Qatar)    
    Preslav Nakov (ALT-QCRI, Qatar)
    Bilal Randeree (Qatar Living, Qatar)

Task website: http://alt.qcri.org/semeval2015/task3/

Contact: semeval-cqa@googlegroups.com

Acknowledgements: This research is part of the Interactive sYstems for Answer Search (Iyas) project, conducted by the Arabic Language Technologies (ALT) group at the atar Computing Research Institute (QCRI) within the Qatar Foundation. 
