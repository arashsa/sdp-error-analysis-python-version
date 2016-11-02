# Team identifier

LiU-Marco

# Team member names and affiliations

Marco Kuhlmann, Linköping University

# Designated contact person and email address

Marco Kuhlmann <marco.kuhlmann@liu.se>

# Inventory of results included in the archive

closed.dm.1.sdp
closed.pas.1.sdp
closed.pcedt.1.sdp

# System characteristics

## Core approach

I have used a pipeline consisting of two components:

(1) a parser that produces dependency graphs
(2) a tagger that decides whether a node in such a graph is a "top" node

The parser (1) can be viewed as a generalization of the MSTParser system
(http://sourceforge.net/projects/mstparser/). At the core of the parser is a
new dynamic programming algorithm (developed and implemented by myself) that
can produce dependency graphs rather than just dependency trees. The parser
uses the same arc-factored feature model as MSTParser and online training
(Perceptron) to learn a weight vector for this model from the data.

The tagger (2) is required because the parser does not know anything about
whether a node is a "top" node in the sense specified by field 5 of the Task's
data format. The tagger implements a simple, binary classifier that is used to
postprocess the output data of the parser (in which no node is classified as a
top node) and fill the "top" columns with more sensible values. Like the
parser, the tagger is trained using online training (Perceptron).

## Important features

The parser uses exactly the same features as MSTParser (arc-factored model).

The tagger uses the following node-specific features. (Lines directly taken
from the Python code.)

	template("T00", node.form)
	template("T01", node.pos)
	template("T02", node.pos, "+" if len(node.incoming_edges) > 0 else "-")
	template("T03", node.pos, "+" if len(node.outgoing_edges) > 0 else "-")
	for edge in node.incoming_edges:
		template("T10", edge.label)
		template("T11", graph.nodes[edge.src].form)
		template("T12", graph.nodes[edge.src].pos)
		template("T13", graph.nodes[edge.src].pos, edge.label)
	for edge in node.outgoing_edges:
		template("T20", edge.label)
		template("T21", graph.nodes[edge.tgt].form)
		template("T22", graph.nodes[edge.tgt].pos)
		template("T23", graph.nodes[edge.tgt].pos, edge.label)

## Critical tools used

None (apart from the parser and the tagger).

## Data pre- or post-processing

None.

## Additional data used

None.

# Bibliographic references

None.
