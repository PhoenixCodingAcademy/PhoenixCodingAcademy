<title>A.I. Glossary</title>

# Neural Networks (NN)

A neural network (NN) is an [IPO](/pages/IPO.md) that can process many columns of data to predict a set of output columns of data. It is trained with a complete table of input columns and output columns.

A NN has these characteristics and components:

* Layers that contain one or more neurons.
* Each neuron has:
  * A set of input connections denoted as arrows pointing into the neuron:
    * Each input connection is:
      * A numeric input value that comes from the environment/data or from the outputs of a previous layer or more inputs
      * A number called a weight or parameter that can be changed only during "training".
  * A set of output connections denoted as arrows pointing out from the neuron:
    * Each output is a value that is calculated from the inputs and the neuron "activation" function.
  * A number called a "bias".
  * A "[activation function](#activation-functions)"
* The outputs of one layer become the inputs of another layer.
* Inputs called an "input layer", or dendrites in biology.
* Outputs called an "output layer", or axons in biology.
* One or more "hidden layers" that denote the process, or soma in biology.
* When a set of input values are put into the NN, there is a formula ("activation function") that calculates the final output values called a "prediction". This calculation is called "Forward Propagation".
* A data table which comes from observations or experiments. As a table, it has columns. Most columns are denoted as input columns, and a few are denoted as output columns. The engineer decides.
* The data table is randomly partitioned into 80% rows for the "training set" and 20% of the rows for "testing set", where each set is a table.
* An algorithm for training the weights of a NN as follows:
  * LOOP:
    * For each row in the training set:
      * Send (or forward propagate) the input columns into the NN - one column per input connection called an "input vector".
      * Get an "output vector", a list of number scores called "logits".
      * Calculate an "error" (or "delta") by comparing the output vector to the output data in some manner.
      * "Back Propagate" that error in the reverse direction through the network to adjust the weights of each neuron.
    * For each row in the test set:
      * Send (or forward propagate) the input columns into the NN - one column per input connection called an "input vector".
      * Get an "output vector", a list of number scores called "logits".
      * Accumulate the total error
    * Exit this LOOP if the total error is small enough, or falls below some chosen threshold, or enough loops have occurred, or some specific amount of time has elapsed, or the error seems to approaching zero too slowly, or the engineer gets bored.
  * PRINT the NN is trained.

In modern techniques, a NN is simply a set of matrices, each matrix represents a layer in the NN.
GPUs can run the matrix operations that quickly train the NN in a loop, and to calculate the forward propagation when using the NN to make predictions.

## Activation Functions

A neural network is a activation function, like f(X) where X is a vector (a list of numbers), where each neuron in the network uses the same function.
To calculate the output of a neuron, this formula is used:

```
output = f(Σ(wᵢ · xᵢ) + b)
```

Or more explicitly:
```
output = f(w₁x₁ + w₂x₂ + ... + wₙxₙ + b)
```

Where:
- **f** = activation function (the same type across all neurons in a layer, often across the entire network)
- **xᵢ** = input values (from previous layer or initial inputs)
- **wᵢ** = weights for each input connection
- **b** = bias term
- **Σ** = summation of all weighted inputs

TYPICAL ACTIVATION FUNCTIONS:

* ReLU (Rectified Linear Unit)
* Leaky ReLU
* Sigmoid
* tanh
* Maxout
* ELU (Exponential Linear Unit)

## References

* [Explain the basic architecture of a Neural Network, model training and key hyper-parameters](https://aiml.com/what-is-the-basic-architecture-of-an-artificial-neural-network-ann/)
* [Activation Functions](https://en.wikipedia.org/wiki/Activation_function)




# Large Language Models

A Large Language Model (LLM) is an application that reads in text and runs it through a Neural Network trained on a large set of sentences to predict the next word.
By repeating this process, an output sentence response is generated.

See [Large Language Models Glossary](/pages/Artificial%20Intelligence/llm-glossary.md)


