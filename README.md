# Artifact of "DeCon: Detecting Incorrect Assertions via Input-output Examples"



### Generating assertions, postconditions, and codes
The assertions and codes generated using CodeGen, Incoder, Codex, GPT-3.5, and DeepSeek-V3 are located in the ``assertiongeneration`` and ``codegeneration`` folders, respectively. The postconditions generated using  GPT-3.5, GPT-4, and DeepSeek-V3 are located in the ``postconditiongeneration`` folder (the field of generated_postcondition).

### Labeling assertions
By executing, use the candidate solutions provided by HumanEval to label whether the generated assertions are correct. The labeled assertions and its statistics are located in the ``labeled assertion`` folder.

### Extracting input and output from docstring

The source code and results of extracting input and output from docstring are located in the ``ExtractExampleFromDocstring`` folder.

### Postcondition filtering
The postconditions after filtering by input/output examples and the filtering source code are located in the ``postconditiongeneration`` folder(the field of correct_postcondition).

### Assertion filtering:
The assertins after filtering by postconditions are located in the ``output_results_withfiltering`` and ``output_results_withoutfiltering`` folder.


### Bug finding:
All problems with bugs can be find by executing the Python file in ``bugfindings`` folder.

# Executing all Python files in the RQs folder will result in the experimental results for each of our RQs.





