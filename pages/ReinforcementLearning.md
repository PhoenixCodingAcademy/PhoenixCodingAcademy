<!--
DESCRIPTION: Learn about reinforcement learning, a type of machine learning where agents learn optimal behavior through trial and error interactions with an environment to maximize cumulative rewards.
-->
[TOC]

# Reinforcement Learning

Reinforcement Learning (RL) is subset of [Machine Learning](/pages/ML.md) (ML).
In other ML algorithms, you are given a dataset with labeled input/output data where you try to discover a relationship between the input and output data.
In RL, you are given a simulated environment where you try to learn a sequence of actions that leads to the highest total reward.
Examples are playing board or video games, driving a car autonomously, or a robot learning how to do some task.

It consists of:

* An **environment** (a simulation of some real-world system; e.g. a tic-tac-toe board)
* One or more **agent**s that interact with the environment; like playing a **game** of many turns.
* On each **turn**, each agent chooses one of a set of possible **action**s that changes the state of the environment (like putting an "X" or an "O" on the board) and return a positive **reward** or a negative **penalty**
* Each agent tries to "learn" how to maximize its reward by playing many variations of the game; i.e. interacting with the environment

The general algorithm for a single-agent system is:
```
while learning:
  Reset the starting state of the environment
  model = new neural network
  total_reward = 0
  while playing:
    reward = model.
```

# Glossary

## Advantage Actor Critic (A2C)



## Agent

An agent is the object that interacts with the environment. Suppose chess is the environment. Then each player would be an agent. To use reinforcement learning to play chess, a multi-agent machine learning (or MARL) is used where two agents (the opposite players) take turns sharing the same environment. The reward of one player is the penalty of the other.

## Environment

In reinforcement learning, the agent interacts with the environment by performing actions, and the environment changes its state according to the action applied. Example: the environment is in state S1, then after action A1, the state changes to S2 and some reward is returned to the agent for consideration.

In a **single-agent** environment, there is only one agent interacting with the environment, e.g. a robot balancing a pole, or a robot navigating a maze. In a **multi-agent** environment, multiple agents interact with the environment, e.g. two game players, or a team sport, or predator/prey simulations.

If an agent's previous actions affect the choices of the next action, we call it a **sequential** environment, e.g. playing chess. If the previous actions have no bearing on the next action, then it is called and **episodic** environment, e.g. guessing the roll of a die.

If the environment will eventually terminate, like a game of tic-tac-toe, then it is called an **episodic** environment. Else, it is called a **continuous** environment - one that never terminates, like a stock market simulator.

If the agents know the complete state of the environment, like a chess game, then it is called a **fully observable** environment. Else it is a **partially observable** environment, like a game of poker.

## Markov Decision Process

It is a thing comprised of these components:

* **S** a set of states (the "state space") of the agent.
* **A** a set of actions (the "action space")
* **P** a function from (a, s, s') -> [0,1] as the probability that action **a** will move state **s** to **s'**.
* **R** a function from (a, s, s') -> Real number as the immediate reward of moving from **s** to **s'** after applying action **a**.



## Multi-Agent Reinforcement Learning (MARL)

This is what you get when you have more than one agent sharing/interacting with the same environment; each agent changing the state of the environement. [WIKI](https://en.wikipedia.org/wiki/Multi-agent_reinforcement_learning)

## Observation

An observation is a subset of the state.
When the agent is able to observe the complete state of the environment, we say that the environment is fully observed. When the agent can only see a partial observation, we say that the environment is partially observed.

## Optimal Policy

A learned policy that guides the agent to a desired outcome.

## Policy

Given the current state of the evolving system, a policy tells the agent which is the next action to take. It is the "brain" of the agent. It is what learns.
When the training begins, the policies are random, and thus not optimized. The agent just picks a random legal action at each state and then evaluates whether this is a good choice or a bad choice.

More formally, a policy (denoted as **μ**) is a function of state that returns an action that the agent should do next.

There are two main types of policies:

* For a **deterministic policy**, the function would be $μ(s) = a$, that is, given state **s**, do action **a**.
* For a **stochastic policy**, the function would be $μ(A|s) = p_i$, that is, given state **s**, then for all possible actions **$a_i$** in **A** where $i \in \{1 ... N\}$, the probability of action $a_i$ being the a good choice is $p_i$ where $\sum_{i=1}^N p_i = 1$. There are two types of stochastic policies:
  * **Categorical** to mean a discrete action state space (or few actions); e.g. {LEFT, RIGHT, UP, DOWN} or {e4, Kb3, Qd3, gxf4, O-O-O...}
  * **Gaussian** to mean a continuous action state space (or lots of actions); e.g. turning a wheel a number of degrees.


## Policy-Based Reinforcement Learning

## State

The **state** of a system is the current values of all the parameters. For example, a bit has two possible values: 0 and 1. So its **state space** is 0 and 1 together, written as {0,1}. It has a size of 2. A system with two bits has a state space of {00, 01, 10, 11}, and the state of that system is always one of those four values.

In reinforcement learning, the agent's state space includes the environment's state space - sometimes interpreted as the agent's understanding of the environment. For example, when teaching an agent to play tic-tac-toe, the state space of the board is $3^9$ because there are 9 squares and each square can contain one of three possible states {BLANK, X, O}. However, not all states are legally possible because many games ends with a win while some squares are still BLANK. So the total number of legal states are much less - 765 to be exact.

The agent's state includes the environment state. In our example, the two tic-tac-toe players are the agents, and the board is the environment. But a agent often includes additional state outside its understanding of the environment. In the game of tic-tac-toe, this additional state might not exist, but as the size of the environment state increases beyond the computer's ability to model it in memory (e.g. the number of possible chess board states exceeds the number of electrons in the known universe), then the agent uses its own state parameters to help navigate the "next best move". Examples of agent state that is not in the environment are:

* The **Policy**, which in tic-tac-toe tends to converge to a **deterministic model** of "always this THIS ACTION if THAT state exists". For more complex environments, a deterministic matrix would be too big to fit in the model, so it learns a **stochastic model** of "probability take THIS ACTION if THAT state is close THIS state." If we had all the time in the universe to train a neural network of $10^200$ neurons, then we might be able to learn a deterministic model of all the estimated $10^120$ possible games of chess (see Shannon's Number).

* A **value function** might predict the expected cumulative reward from each state (or state-action pair), given the current policy. This helps the agent to evaluate how good a state-action pair might to improve the policy.

* **Eligibility Traces**  These are a memory mechanism that help the agent to update the value function for states (or state-action pairs) that are several steps in the past. See SARSA(λ).

* **Replay Buffer** (in methods like DQN) is memory of past state transitions, which is used to provide diverse training samples for the agent's neural network.

* **Exploration vs Exploitation Balance** is a measure of how much the agent should explore the environment by trying random actions, versus exploiting its current knowledge to choose what it thinks is the best action. For an example of exploitation, in an ant trail, most ants follow the pheromone trail to the current source of food. On the other hand, we see exploration when a few ants randomly go off trail in hopes to find new sources of food.
*

## Value-Based Learning

Instead of training a policy, we train a value function whose input is a state and whose output is the expected value of being in that state.
TODO - elaborate



# References

* [TensorFlow: Customizing what happens in fit()](https://www.tensorflow.org/guide/keras/customizing_what_happens_in_fit) - the fit() function loops a fixed number of times; called epochs. This is what happens behind the scenes during each loop.
* [Beginner’s Guide to Policy in Reinforcement Learning](https://machinelearningknowledge.ai/beginners-guide-to-what-is-policy-in-reinforcement-learning/)
* [Baeldung - Reinforcement Learning](https://www.baeldung.com/cs/category/ml/tag/reinforcement-learning)

State-action-reward-state-action (SARSA) is an on-policy reinforcement learning algorithm used to teach a new Markov decision process policy.
* [State–action–reward–state–action](https://en.wikipedia.org/wiki/State%E2%80%93action%E2%80%93reward%E2%80%93state%E2%80%93action)
* [Reinforcement Learning — TD(λ) Introduction(3)](https://towardsdatascience.com/reinforcement-learning-td-%CE%BB-introduction-3-f329bdbf872a) - Extend TD(λ) on Q function with Sarsa(λ)
* [SARSA Reinforcement Learning Algorithm: A Guide](https://builtin.com/machine-learning/sarsa)

## PyTorch

* [Stable-Baselines3 Docs - Reliable Reinforcement Learning Implementations](https://stable-baselines3.readthedocs.io/en/master/)
* [Stable-Baselines3 Installation](https://stable-baselines3.readthedocs.io/en/master/guide/install.html)
```
pip install "stable-baselines3[extra]"
```

## Courses

* [Hugging Face Deep Reinforcement Learning Course](https://huggingface.co/learn/deep-rl-course/unit0/introduction)