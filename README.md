# Safe Reinforcement Learning in Pacman

Reinforcement learning algorithms find optimal policies, but they rarely guarantee safety during learning or execution phases. In our report, we present a summary of having a safety shield for reinforcement learning problems. We implement a shield in the domain of Pacman and present our results. We notice that having a safety shield does not affect the convergence of the learning algorithm. The shield also prevents the agent from taking unsafe actions during both learning and execution.

## How to test our implementation?

```
git clone https://github.com/CodeMaxx/Safe-RL-Pacman.git
cd Safe-RL-Pacman/code/
./gen_data.sh
```

This will generate .dat files for Pacman with and without a shield in [data](data) folder. To visualize, use the following script in [plots](plots) folder

```
python plot.py <path to shield data> <path to non-shield data>
```
## Linear Temporal Logic for Shielding

### Idea
Alshiekh, M.; Bloem, R.; Ehlers, R.; Könighofer, B.; Niekum, S.; and Topcu, U. 2017. *"Safe Reinforcement Learning via Shielding"* present the use of linear temporal logic for shielding in reinforcement learning. The idea is to convert a linear temporal logic specification into a safety automaton and abstract the underlying MDP which the agent has to learn into an abstraction automaton. The next step is to convert the safety automaton and the abstraction automaton into a game, which is solved for winning regions. The game and the winning region obtained is translated into a shield, which is nothing but a finite state reactive system. 

### Shield used for Pacman

Even though the inner working of a learning algorithm is often complex, the safety criteria may still be enforced by possibly simpler means. Shielding exploits this possibility.
We borrow the idea of Shielding as described above. We first came up with the linear temporal logic formula for Shielding in Pacman

-------------------

¬ o ♦ ♦ *DeadState*

*It is not the case that for all time instances, the next to next state is a dead state*

-------------------

We inject the code for the shield into the existing Pacman code.

## Metrics used for evaluating our Shield

### Average Score vs Episode
The average reward received so far plotted against the number of episodes

### Average score windowed vs Episode
The average score calculated across a window of 10 episodes vs the number of episodes

### Average Score vs Time
The average score calculated versus the time taken for the execution

### Losses vs Episode
Losses are the number of occurrences when the Pacman has been eaten by the ghost. This metric indicates the losses against the number of episodes.

### Losses windowed vs Episode
This plot is against the losses in a window of 10 learning versus the episode number

### Unsafe actions windowed vs Episode
Unsafe actions in the context of shielding is an action that leads to a state which is at a Manhattan distance of less than 2 from the ghost. The reason behind keeping a distance of 2 is that this is an adversarial game in which the ghost takes an action after Pacman has taken an action. We would like to call any action unsafe that can lead to a state where the Pacman can make a move which can kill the Pacman.

## Results

The results are discussed in our [report](report.pdf) 
