
SemEval 2015 Task 18: Broad-Coverage Semantic Dependency Parsing: Companions

Version 1.0; November 22, 2014


Overview
========

This directory contains the so-called ‘companion’ data: syntactic analyses for
the English part of the SDP training data in various (more or less) popular
formats, for use in the ‘open’ and ‘gold’ tracks of the task.

In all cases, we seek to make available gold-standard analyses deriving from
manual annotation or realistic outputs of state-of-the-art tools.  For the
latter, we ran ten-fold jack-knifing on the SDP gold-standard data, splitting
off nine of ten sentences for training and the other ten percent for testing,
ten times.  For each split, we re-trained the syntactic parser on the training
portion and applied the resulting model to the test portion.  Thus, in contrast
to using off-the-shelf models for these parsers, our companion data reflects
typical parser performance on unseen, in-domain test data (however, each parser
is trained on only some 30,000 sentences, i.e. a little less than is common in
statistical parser evaluation over the PTB).  As our SemEval 2015 task moves
into its evaluation period, we will make available the same range of companion
analyses (using models trained over the full SDP training data) for the SDP
test data.

Please see below for the individual companion formats and details on how they
were prepared.  In all cases, the companion data is intended solely for use in
either the open or gold tracks, where one can think of the additional files as
extending our core training files (‘en.dm.sdp’, ‘en.pas.sdp’, and ‘en.psd.sdp’)
‘horizontally’, i.e.  with additional columns.  For convenience of reference we
will number these columns using negative identifiers, starting from -1 and
working backwards.  Companion files are sentence- and token-aligned to our
training data.


Stanford Basic Dependencies: Bohnet & Nivre
===========================================

To provide syntactic analyses in the form of bi-lexical dependencies, we used
the so-called Stanford Basic scheme (de Marneffe & Manning, 2008) and the
parser of Bohnet & Nivre (2012).  The conversion started from simplified PTB
phrase structure trees with the ‘standard’ range of simplifications applied,
viz. removal of function labels and traces; We applied the dependency converter
built into the Stanford Parser (in version 3.3.1) as follows:

  java -cp stanford-parser.jar \
    edu.stanford.nlp.trees.EnglishGrammaticalStructure \
    -treeFile fold${i}-train.mrg -basic -keepPunct -conllx \
    > $(basename fold${i}-train .mrg).conll

Subsequently, the CoNLL-X format output by the converter was padded with extra
columns, to provide the CoNLL-09 format expected by the Bohnet & Nivre Parser
(henceforth BN): for the training files, columns 1 (ID), 2 (FORM), 4 (POS), 7
(HEAD), and 8 (DEPREL) were preserved; for the decoding files, only columns 1
and 2 were provided to the parser (thus, again, the parser did not have access
to gold-standard parts of speech at decoding time).

Parser training and decoding were invoked as follows (in one run per fold):

  java -Xmx30G -cp anna-3.3.jar is2.transitionR6j.Parser \
    -train fold${i}-train.conll \
    -test fold${i}-parse.conll -out fold${i}-bn.conll \
    -model eng-b80-R6j-${i}.mdl -tmodel eng-b80-R6j-${i}.tmdl \
    -i 20 -hsize 500000001 -beam 80 -1st a -2nd abcd -3rd ab \
    -tsize 3 -tnumber 10 -ti 10 -x train:test \
    -thsize 90000001 -tthreshold 0.2 -tx 2 -half 2 -tt 25 -cores 16

For more background, please see:

  https://code.google.com/p/mate-tools/
  http://nlp.stanford.edu/software/stanford-dependencies.shtml
  http://www-nlp.stanford.edu/software/lex-parser.shtml

The companion file ‘en.sb.bn.cpn’ provides three fields:

  (-1) BNPOS    --- PoS tags predicted by the parser
  (-2) BNHEAD   --- head identifiers predicted by the parser
  (-3) BNDEPREL --- dependency labels predicted by the parser


Stanford Basic Dependencies: Penn Treebank
==========================================

The gold-standard companion file ‘en.sb.ptb.cpn’ provides the same dependencies
as described above, for training the Bohnet & Nivre parser, with three fields:

  (-1) PTBPOS    --- PoS tags, as annotated in the Penn Treebank
  (-2) PTBHEAD   --- head identifiers in Stanford conversion
  (-3) PTBDEPREL --- dependency labels in Stanford conversion


DELPH-IN Derivation Tree–Derived Dependencies (DT): DeepBank
============================================================

The gold-standard companion file ‘en.dt.deepbank’ contains syntactic analysis
in the HPSG-derived scheme dubbed DT by Ivanova et al. (2012).  The source of
the data is the same as that of the DM training data, viz. DeepBank 1.1.  For
details, please see:

  http://aclweb.org/anthology/W12-3602
  http://moin.delph-in.net/DeepBank

As for the other files, there are three columns:

  (-4) DEEPBANKPOS    --- PoS tags, as annotated in DeepBank
  (-5) DEEPBANKHEAD   --- head identifiers in DT conversion
  (-6) DEEPBANKDEPREL --- dependency labels in DT conversion


Enju HPSG Dependencies (EH): Enju Treebank
==========================================

The gold-standard companion file ‘en.eh.enju’ contains another HPSG-derived
syntactic dependency scheme, converted from the Enju Treebank.  This specific
reduction of Enju HPSG analyses to bi-lexical dependencies was developed for
the SDP 2015 task by Yusuke Miyao.  For some general background, please see:

  http://aclweb.org/anthology/S14-2056

Again, there are three columns:

  (-7) ENJUPOS    --- PoS tags, as annotated in the Enju Treebank
  (-8) ENJUHEAD   --- head identifiers in EH conversion
  (-9) ENJUDEPREL --- dependency labels in EH conversion


Known Errors
============

System-predicted DT and EH dependencies are not available yet; we will try to
make these available before the end of November, 2014 (using the jack-knifing
procedure sketched above over the gold-standard analyses).

No multi-lingual companion analyses are provided, and it is beginning to look
unlikely that we will be able to put these together still in 2015.


Release History
===============

[Version 1.0; November 22, 2014]

+ Initial release of gold-standard and state-of-the-art system dependencies.


Contact
=======

For questions or comments, please do not hesitate to email the task organizers
at: ‘sdp-organizers@emmtee.net’.

Angelina Ivanova
Marco Kuhlmann
Yusuke Miyao
Stephan Oepen
