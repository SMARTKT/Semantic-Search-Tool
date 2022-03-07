# Semantic-Search-Tool

Instructions : 

1. Create a config.json

The config.json should have the following keys : 

- python_path [optional, default = python] : the path to python. For machines which use python3 to run python scripts, create this key with appropriate value in the json file.

- project_path : Path to the project. It should have a CMakeLists.txt file

- output_path : Path where the output of the Search Tool will be stored

- runs_json_path : Path to the runs json file required by the Search Tool.

The runs_json should have a key called "runs" whose value will be a dictionary whose key is a binary and value will be another dictionary with test input as key and number of times to run as value.

For eg, for libpng the contents of runs_json file would be 

```
{
    "runs": {
        "/home/dewang/smartKT/SmartKTRepo/projects/libpng/build/pngtest": {
            "/home/dewang/smartKT/SmartKTRepo/projects/libpng/pngtest.png" : 1
        }
    }
}
```

Here pngtest is the binary, the path to image is the input, and for this input the binary is run once.



2. Run main.py with argument as the path to config.json

```
python main.py <path to config.json>
```