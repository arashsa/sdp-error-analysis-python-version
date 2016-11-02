
SemEval 2015 Task 18: Broad-Coverage Semantic Dependency Parsing: DM Background

Version 1.1; March 19, 2016


Overview
========

This directory contains the data from which the DM bi-lexical dependency graphs
have been derived: (a) Elementary Dependency Structures (EDS) and (b) Minimal
Recursion Semantics formulae (MRS).  As described by Miyao et al. (2014) and
Oepen & Lønning (2006), the DM graphs originate from a two-step lossy conversion
of scopally underspecified MRS logical-form meaning representations.  General
background on the EDS and MRS representations is available on-line:

  http://moin.delph-in.net/EdsTop
  http://moin.delph-in.net/MrsRfc


File Organization
=================

For ease of indexing, EDS and MRS representations (as well as the underlying
‘raw’ strings) are provided as separate files, named after the SDP identifier
scheme and using suffixes ‘.eds’, ‘.mrs’, and ‘.txt’, respectively.  Thus, file
‘20102003.eds’, for example, provides the EDS for the third sentence in the
second document of Section 01 of the WSJ Corpus; ‘20102003.mrs’ contains the
MRS from which the EDS was derived, and ‘20102003.txt’ the underlying string.
These are the same identifiers as used in the SDP files proper.  To ease the
(quantitative) comparison to the derived DM representation, covert quantifiers
and the ERG ‘discourse’ relations have been suppressed from the EDS graphs, 
using the following ‘:filter’ pattern /^[^_].*_q$|^focus_d$|^parg_d$/.  These
are nodes that, arguably, are predictable from independent properties of the
underlying underspecified logical forms (for example quantifiers binding the
variables introduced by pronouns, proper names, and the modifier elements in
nominal compounds).  EDS nodes matching the expression that occur as arguments
to other parts of the graph, however, are retained.

For some cross-framework interoperability, the EDS graphs are also provided in
two additional formats, viz. in the syntax of Abstract Meaning Representation
(AMR) and in a machine-readable JSON serialization.  Both alternative formats
are described at the above EDS web page (‘EdsTop).  The files ‘train.amr.gz’
and ‘test.amr.gz’ provide the corresponding sets of EDS graphs automatically
converted into the single-rooted, tree-like format (with node re-entrancies, as
needed) of AMR, where the top node is at the root of the tree, and inverse
roles (like, for example, ARG1-of) serve to indicate incoming edges to nodes.
In this serialization of EDS, the characterization pointers are rendered as a
pseudo-role ‘:lnk’, and the variable property information (e.g. tense and
number) is omitted.  Furthermore, there is a small proportion (1.5 percent) of
‘fragmented’ EDS graphs, meaning that there are nodes (or connected sub-graphs)
that are not reachable via an undirected path from the top node; the AMR
serialization format is limited to connected graphs and, hence, for these
fragmented EDSs the unconnected nodes are not included in AMR serialization.
Finally, the parallel files ‘train.json.gz’ and ‘test.json.gz’ render the same
sets of EDS graphs, but this time including variable properties and all nodes.


Known Errors
============

None, for the time being.


Release History
===============

[Version 1.1; March 19, 2016]

+ Re-generated EDS graphs, now via eds-output-psoa() to filter covert nodes.

[Version 1.0; October 11, 2015]

+ Initial release of DM background data, including raw WSJ and Brown strings.


Contact
=======

For questions or comments on the EDS and MRS background data to DM, please do
not hesitate to contact:

Stephan Oepen <oe@ifi.uio.no>
Dan Flickinger <danf@stanford.edu>


References
==========

Copestake, A., Flickinger, D., Pollard, C., and Sag, I. A.  (2005).  Minimal
  Recursion Semantics. An introduction.  Research on Language and Computation,
  3(4), 281–332.

Flickinger, D., Zhang, Y., and Kordoni, V.  (2012).  DeepBank. A Dynamically
  Annotated Treebank of the Wall Street Journal.  In Proceedings of the 11th
  International Workshop on Treebanks and Linguistic Theories (p. 85–96).
  Lisbon, Portugal.

Miyao, Y., Oepen, S., & Zeman, D.  (2014).  In-House. An Ensemble of
  Pre-Existing Off-the-Shelf Parsers.  In Proceedings of the 8th International
  Workshop on Semantic Evaluation (p. 63–72).  Dublin, Ireland.

Oepen, S., and Lønning, J. T.  (2006).  Discriminant-Based MRS Banking.  In 
  Proceedings of the 5th International Conference on Language Resources and
  Evaluation (p. 1250–1255).  Genoa, Italy.

