# instructions : python main.py <path to config.json>
import os
import json
import sys

jsonpath = "config.json"
if len(sys.argv)>1:
	jsonpath = sys.argv[1]

with open(jsonpath) as r:
	config = json.loads(r.read())

if "python_path" in config:
	pythonpath = config["python_path"]
else:
	pythonpath = "python"

projectname = config["project_path"].split("/")[-1]

# Enter the kgg folder
os.chdir("kgg")

# Run initialize.py
os.system(f"{pythonpath} initialize.py {config['project_path']} {config['output_path']}")

# Run examine.py
os.system(f"{pythonpath} examine.py {config['runs_json_path']} {config['output_path']}")

os.chdir("../")

## Running the query engine (to generate TTL)
os.chdir("qe/")


project_output_folder = os.path.join(config['output_path'], projectname)


for folder in os.listdir(project_output_folder):
	if folder.startswith("exe_"):
		xml_folder = os.path.join(project_output_folder, folder)

		# inputs
		static_file = os.path.join(xml_folder, "final_static.xml")
		dynamic_file = os.path.join(xml_folder, "final_dynamic_0.xml")

		# outputs
		mapping_static_file = os.path.join(xml_folder, "mapping_static.p")
		static_ttl = os.path.join(xml_folder, "final_static.ttl")
		dynamic_ttl = os.path.join(xml_folder, "final_dynamic.ttl")
		final_ttl = os.path.join(xml_folder, "final.ttl")

		# mapping_extra_id
		os.chdir("parseXML")
		os.system(f"{pythonpath} mapping_extra_id.py {static_file} {mapping_static_file}")

		# parseStaticXML
		os.system(f"{pythonpath} parseStaticXML.py {static_file} {static_ttl} {mapping_static_file} {xml_folder} ")

		# parseDynamicXML
		os.system(f"{pythonpath} parseDynamicXML.py {dynamic_file} {dynamic_ttl} {mapping_static_file}")

		# merge TTLs
		os.system(f"{pythonpath} merge_static_dynamic.py {static_ttl} {dynamic_ttl} {final_ttl}")


