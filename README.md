# SmartappAnalysis

## Program Analysis Final Project -- Yifei Yang

### Static Checking of Samsung Smartapps relationships in a household environment

This app simply parses the codefile of Samsung Smartapps, and build a relationship
graph between devices and their different states. The relationship between devices
is created by edges represented by the smartapps. 

i.e.: (A, state 1) ->s (B,state2) in the graph represents that device A at state 1
can change device B to state2 via smartapp s. 

From the relationship graph, we are able to find potential abnormalities within the
househould environment due to the smartapps, 3 types are shown by examples:

1. Circularity: Device A changes to state S will trigger a chain of action to cause 
Device A change back to state S' with smartapps.

2. Direct Conflict: Device B and Device C can change Device A to different states at
the same time due to smartapps

3. Hidden: It is possible for us to change Device A to state S unintendedly. In our
example an app that intends to turn on switch can unlock the door.

To run the analysis, change `analysis.py` to your smartapp files, and specify
what input device each smartapp is going to use, then, running

```python3 analysis.py``` 

will generate the output file `analysisResult.txt` that describes the relationship graph and found conflicts/abnormalities.

### Limitations:
This app only works for simple smartapps with relationships `if A happens then B happen` due to limitations
in parsing. We would like to work into supporting more complicated relationships. We would like 
to add support to more complicated smartapps with more complicated conditionals in the future. One
example for such is smartapp with rules `if A or C happens then B happen`
