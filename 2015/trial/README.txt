
SemEval 2015 Task 18: Broad-Coverage Semantic Dependency Parsing: Trial Data

Version 1.1; August 3, 2014


Overview
========

This directory contains three files, each providing semantic dependency graphs
for a trial set of 189 sentences, taken from the first 20 documents in Section 
00 of the venerable PTB WSJ Corpus.  These files use the tab-separated format
for the description of general directed graphs, as documented on-line:

  http://sdp.delph-in.net/2015/data.html

Please note that the SDP 2015 format differs from the one used on conjunction
with SemEval 2014 (the first SDP task), in that one additional column has been
added: SENSE (field #7) records semantic sense information for DM and PSD.  An
earlier release (Version 1.0) of the SDP 2015 trial data was lacking this new
column.   To allow scripts to distinguish the 2014 and 2015 formats, current
data indicates the file format using a ‘comment’ line at the start of the file,
i.e.

  #SDP 2015

File names are comprised of an acronym denoting the specific annotation type,
and the common suffix ‘.sdp’ (which we will use on all data for this task).


Known Errors
============

None, for the time being.


Release History
===============

[Version 1.1; August 3, 2014]

+ Upgrade to SDP 2015 format, adding SENSE; discard one cyclic graph.

[Version 1.0; June 1, 2014]

+ Initial release of the trial data for three representations: DM, PAS, PSD.


Contact
=======

For questions or comments, please do not hesitate to email the task organizers
at: ‘sdp-organizers@emmtee.net’.

Dan Flickinger
Jan Hajič
Angelina Ivanova
Marco Kuhlmann
Yusuke Miyao
Stephan Oepen
Yi Zhang
Daniel Zeman
