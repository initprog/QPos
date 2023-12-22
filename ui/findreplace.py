import sys

use_resource_file = False

if len(sys.argv) != 4:
  print("Syntax: findreplace <old-text> <new-text> <infile>")
  quit()

# Open input file in read only mode 
with open(sys.argv[3], 'r') as file: 
  data = file.read() # Read into memory

  if data.find(':/icon') != -1:
     use_resource_file = True

  if sys.argv[1] != sys.argv[2]:
    data = data.replace(sys.argv[1], sys.argv[2])  # quick find-replace
  
if not use_resource_file:
  with open(sys.argv[3], 'w') as file:
    file.write(data)
    exit(0)
    
# if the file uses any resource then add import stmt
lines = data.split('\n')
with open(sys.argv[3], 'w') as file:
  for line in lines:
    if use_resource_file:
      if line.startswith('from ') or line.startswith('import '):
        file.write('from qpos.asset import resource_rc\n')
        use_resource_file = False
    file.write(line + '\n')
