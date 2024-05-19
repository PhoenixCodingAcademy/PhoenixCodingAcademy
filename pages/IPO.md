[TOC]

# Input-Process-Output (IPO)

Input-Process-Output (IPO) makes up literally everything that humans do on this planet, but definitely everything that computers do.
Even our sentences follow the structure. The subject is the "input". The verb is the "process". The "output" is implied by the dependent clause that follows. "I saw a movie today":

* INPUT: I (before I saw the movie)
* PROCESS: "seeing"
* OUTPUT: I (after I saw the movie, now with memories of the movie)

Sometimes the roles are reversed and the circles represent the nouns and the arrows represent the verbs. What's important is that whatever the nodes represents (nouns or verbs) the arrows represent the other choice. If an arrow means a verb on a diagram, then all arrows mean verbs on that diagram. **Don't mix and match!** It will confuse your audience. Sadly some [TensorFlow](https://iq.opengenus.org/understand-basic-tensorflow-programming/) documents use nodes to represent both variables and functions, with arrows representing weights. Sigh.

# Notation

In a **[graph](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics))** we have circles (called nodes or vertices) and lines (called edges, connections, or links). When we put arrowheads on the lines to make arrows, we call it a **[directed graph](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)#Directed_graph)** because the graph **flows** in a specific direction; with the arrows.

Directed graphs are used to diagram IPO.

There are two methods to diagramming how the nouns related to the verbs.
In all cases, one or more input nouns are fed into a verb to produce exactly one output noun.

**METHOD 1**: We can diagram it like this, where the process can have multiple inputs and outputs:

![](/static/images/ipo4.png)

**METHOD 2**: Or like this, where the process operates on a single input to produce a single output:

![](/static/images/ipo5.png)

Notice that both methods above have two nouns and one verb.




Circles are processes, arrows pointing in are inputs, and arrows pointing out are outputs.

![](/static/images/ipo1.png)

Sometimes the roles of circles and arrows are reversed.

![](/static/images/ipo3.png)

This is true for state diagrams, where each circle represents the "before" state of an object, and arrows represent the operations that transform the "before" state into an "after" state; e.g. "unpainted" vs "painted".

The output arrow of one circle can be the input of another arrow. This is how **composition** can create **meshes** or **networks**.

![](/static/images/ipo2.png)


# Uses

## Mathematics

Suppose we have the expression $y = f(x)$ where x and y are variables (or values) and f is the function.

* INPUT: parameters, variables; e.g. X
* PROCESS: function, operator; e.g. f
* OUTPUT: results; e.g. Y


## Workflow

* INPUT:
* PROCESS:
* OUTPUT:

##
* INPUT:
* PROCESS:
* OUTPUT:
