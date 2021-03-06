# SmartappAnalysis

## Program Analysis Final Project -- Yifei Yang

### Static Checking of Samsung Smartapps relationships in a household environment

For a detailed description of implementation details, view `17355ProjectReport.pdf`.

This app simply parses the codefile of Samsung Smartapps, and build a relationship
graph between devices and their different states. The relationship between devices
is created by edges represented by the smartapps. 

i.e.: (A, state 1) ->s (B,state2) in the graph represents that device A at state 1
can change device B to state2 via smartapp s. 

From the relationship graph, we are able to find potential abnormalities within the
househould environment due to the smartapps, 3 types are shown by examples:

1. Circularity: Device A changes to state S will trigger a chain of action to cause 
Device A change back to state S' with smartapps.

Example for such conflict is shown in `Smartapps/Circular`

2. Direct Conflict: Device B and Device C can change Device A to different states at
the same time due to smartapps


Example for such conflict is shown in `Smartapps/DirecConf`

3. Hidden: It is possible for us to change Device A to state S unintendedly. In our
example an app that intends to turn on switch can unlock the door.


Example for such conflict is shown in `Smartapps/Hidden`

To run the analysis, change `analysis.py` to your smartapp files, and specify
what input device each smartapp is going to use, then, running

```python3 analysis.py``` 

will generate the output file `analysisResult.txt` that describes the relationship graph and found conflicts/abnormalities.

Currently, the device input for each environment is manually inputed as a dictionary in 
a format shown in `analysis.py`. One possible future work would be making such device
input more user friendly by creating an interface.

### Limitations:
This app only works for simple smartapps with relationships `if A happens then B happen` due to limitations
in parsing. We would like to work into supporting more complicated relationships. We would like 
to add support to more complicated smartapps with more complicated conditionals in the future. One
example for such is smartapp with rules `if A or C happens then B happen`. This can be done by expanding
our language in lexing and parsing when building our AST.
