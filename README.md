# Semantic-Search-Tool

Instructions for running the search tool of SmartKT (shown for libpng project): SmartKT applies to projects which are built up on Cmake. 

1. Clone the libpng project from github
   https://github.com/glennrp/libpng
   
   Extract it 

2. Clone the Semantic Search tool project from https://github.com/SMARTKT/Semantic-Search-Tool.git 

Extract the folder. cd to sub folder Semantic-Search-Tool-main. 

Create a config.json (you might already find a config.json file, edit it with your system local paths). This file should be placed under the following 

The config.json should have the following keys : 

- python_path [optional, default = python] : the path to python. For machines which use python3 to run python scripts, create this key with appropriate value in the json file.

- project_path : Path to the project. In this case path to the extracted folder of libpng like /home/user/SmartKT_Search_Tool/libpng

- output_path : Path where the output of the Search Tool will be stored: Create a folder named outputs in any directory like    /home/user/SmartKT_Search_Tool/outputs/

- runs_json_path : Path to the runs json file. To build this file, we should be aware of the executable name and the inputs to a project. For the executable name, look up for the add_executable command in the cmakelists.txt file for a project. 

We show an example for the libpng project, checking up the add_executable command in the cmakelists.txt, we see pngtest, pngimage etc are the executables. We select pngtest and also pngtest.png as the input and write the runs.json file as below

```
{
    "runs": {
        "/home/user/smartKT/SmartKTRepo/projects/libpng/build/pngtest": {
            "/home/user/smartKT/SmartKTRepo/projects/libpng/pngtest.png" : 1
        }
    }
}
```
The number 1 specify that the file should be run with the input once. We might want to run the same file with the same input to understand non-deterministic behaviour in case of mulit-threaded applications


3. cd to folder Semantic-Search-Tool-main.  Run main.py with  config.json.

```
python main.py <path to config.json>
```
