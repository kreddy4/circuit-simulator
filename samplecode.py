class Node:
    def __init__( self, _name, _inputs, _outputs, _type ):
        self.name = _name             #used to access the graph dict
        self.inputs = _inputs         #list of keys correspond to the input nodes
        self.outputs = _outputs       #same as above, except for outputs
        self.type = _type             #string
        self.outputReady = False
        self.allInputsReady = False
        self.whichInputsReady = set()
        self.values = []              #array of values, for parallel TV simulation

    def PerformOp( self ):
        pass

def MakeNodes( benchName ):

    netFile = open(benchName, "r")
    circuit = []

    # temporary variables
    node_inputs = []  # array of the input wires
    gate_inputs = []
    output = []  # array of the output wires
    gates = []  # array of the gate list
    inputBits = 0  # the number of inputs needed in this given circuit
    lines = []

    #reading all the lines of netFile
    for line in netFile:
        term = None
        # NOT Reading any empty lines
        if (line == "\n"):
            continue

        # Removing spaces and newlines
        line = line.replace(" ", "")
        line = line.replace("\n", "")

        # NOT Reading any comments
        if (line[0] == "#"):
            continue

        # Read a INPUT wire and add to circuit:
        if (line[0:5] == "INPUT"):
            # Removing everything but the line variable name
            line = line.replace("INPUT", "")
            line = line.replace("(", "")
            line = line.replace(")", "")
            term = Node(line, None, 'INPUT', 'U');
        elif (line[0:6].upper() == "OUTPUT"):
            line = line.replace("OUTPUT", "")
            line = line.replace("(", "")
            line = line.replace(")", "")
            node_inputs.append(line)
            term = Node(line, node_inputs, 'OUTPUT', 'U')
        elif '=' in line:
            lineSpliced=line.split("=")
            lineSpliced = lineSpliced[1].split("(")
            logic = lineSpliced[0].upper()
            gate_inputs = lineSpliced[0]
            lineSpliced[1] = lineSpliced[1].replace(")", "")
            node_inputs = lineSpliced.split(",")
            term = Node(gate_inputs, node_inputs, logic, 'U')

        circuit.append(term)
        return circuit

def GetTestVectors( fileName ):
    pass

def Simulate( circuit, testVectors ):
    pass

def main():
    # Read-in circuit benchmark and create circuit nodes
    print("Circuit Simulator:")
    print("Enter the Circuit Benchmark File:")
    # Select circuit benchmark file, default is circuit.bench
    while True:
        cktFile = "circuit.bench"
        print("\n Read circuit benchmark file: use " + cktFile + "?" + " Enter to accept or type filename: ")
    userInput = input()

    if userInput == "":
        break
    else:
        cktFile = os.path.join(script_dir, userInput)
        if not os.path.isfile(cktFile):
            print("File does not exist. \n")
        else:
            break

    print("\n Reading " + cktFile + " ... \n")
    circuit = MakeNodes(cktFile)
    # Read-in test vectors
    print("Enter the Input file: ")
    userInput = input()
    testVectors = GetTestVectors( userInput )
    # Performance simulation/breadth-first search through the circuit
    # Simultaneously do some other stuff depending on what the assignment calls for?
    # Ex: Calculate the critical path (longest delay path)
    outputs = Simulate( circuit, testVectors )

if __name__ == "__main__":
    main()