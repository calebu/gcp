#!/usr/bin/python
# Play with json module
# Writes json to an output file tester.txt

import sys, json, logging, yaml

logger = logging.getLogger(__name__)
if len(sys.argv) > 1 and sys.argv[1] == 'check-changes':
    config = ''
    with open('main/test.yml', 'r') as file:
        config = yaml.safe_load(file)

    repo_check = f"""
<html>
	<body>
 		<h3>Changes to be made</h3>
   		<table>
     		<tr><td>Repo</td><td>Branch</td><td>Change</td></tr>
       		<tr><td>Main Repo</td><td>Main</td><td><ul><li>++ line added<li>-- line removed {config}</ul></td></tr>
         </table>
    </body>
</html>
"""
    print(" ".join(repo_check.split()))
    exit()
#print (len(sys.argv[1]))
#print (f"From python code: {sys.argv[1]}")

with open('main/test.yml', 'r') as file:
    config = yaml.safe_load(file)

f = open("tester.txt", "a")
f.write("[]")
f.close()

f = open("tester.txt", "r")
content = f.read()
obj = json.loads(content)
dict = {"name" : "one"}
obj.append(dict)
dict = {"name" : "two"}
obj.append(dict)
dict = {"name" : "three"}
obj.append(dict)
dict = {"name" : "four"}
obj.append(dict)
obj = json.dumps(obj, indent = 2)

logger.info(f"{obj}")

import pandas as pd

# Define a simple dictionary of data
data = {
    'Greeting': ["Hello", "World"],
    'ID': [1, 2]
}

# Create a DataFrame
# Pandas is usually imported under the 'pd' alias
df = pd.DataFrame(data)

# Print the DataFrame
print(df)