1. Team ID
   
   alpage

2. Team affiliation

    INRIA - Université Paris 7 Diderot
    
    Team members:

        Djamé Seddah <djame.seddah@gmail.com>
        Eric de la Clergerie <Eric.De_La_Clergerie@inria.fr>
        Corentin Ribeyre <corentin.ribeyre@inria.fr>

3. Contact information

   Djamé Seddah <djame.seddah@gmail.com>

4. Submission, i.e., ZIP file name
    
    alpage.tgz

5. System specs

- 5.1 Core approach

  run1: the parser we used is a modified version of the Shift-Reduce DAG
      dependency parser of Kenji Sagae. It has been extended to support
      partially connected planar graphs and the classification library has
      been extended to support several well-known algorithms : averaged
      perceptron, SVM, and so on.
  
  run2: dyalog-sr is a transition-based dependency parser, using beams
    and dynamic programming techniques. For SemEval14, it has been
    extended to produce dependency graphs rather than dependency
    trees. A simple form of swap transition has been added to cover
    some cases of non-projectivity.

- 5.2 Supervised or unsupervised

  run1: Supervised, with an averaged perceptron

  run2 (dyalogsr): Supervised, with a structured perceptron

  For both run, when Clusters were used, they were extracted from the BNC using 
 the Brown algorithm (1000 Dclusters over words frequency > 100) and
 extended with morph. features (suffices, capitalisation and so on) leading
to a vocabulary of 15k units.

- 5.3 Critical features used

  run1 : Features including lemma and distance between words as long as (for
  the open track massive syntactic information such as spines, paths in the
  PTB trees, ...)

  run2 (dyalogsr): Features related to governors have been added (number of
  governors, and labels to the governors)

- 5.4 Critical tools used
- 5.5 Significant data pre/post-processing
  
  run1: For the closed track on the PCEDT corpus we improve the LP LR LF
  by using mate's predicted label

- 5.6 Other data used (outside of the provided)

  None for the closed track.

  run1: For the open track:
    -  same clusters as for run2
    - different syntactic features (spines, path and so on)

  run2 (dyalogsr): For the open track:
    - Brown clusters extracted from the BNC (americanized and ptb-ized
version). Clusters are extended with morphological suffices 
    - Information from Berkeley parser
    - Information from MATE parser

6 References (if applicable)

  run1: 
  
  SAGAE K. & TSUJII J. Shift-Reduce Dependency DAG Parsing. In Proc.
  of COLING 2008

 CANDITO \& SEDDAH, Parsing Word Clusters, in Proc. of SPMRL 2010 

  run2 (dyalogsr):

  VILLEMONTE DE LA CLERGERIE É. (2013a). Exploring beam-based
  shift-reduce dependency parsing with DyALog : Results from the SPMRL
  2013 shared task. In 4th Workshop on Statistical Parsing of
  Morphologically Rich Languages (SPMRL’2013), Seattle, États-Unis.

  HUANG L. & SAGAE K. (2010). Dynamic programming for linear-time
  incremental parsing. In Proceedings of the 48th Annual Meeting of
  the Associationfor Computational Linguistics, p. 1077–1086 :
  Association for Computational Linguistics.

  SAGAE K. & TSUJII J. Shift-Reduce Dependency DAG Parsing. In Proc.
  of COLING 2008

