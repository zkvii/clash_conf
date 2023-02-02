fin = open("config.yaml", "rt")
#read file contents to string
data = fin.read()
#replace all occurrences of the required string
data = data.replace('789', '1089')
data = data.replace('9090','10090')
data = data.replace('# external-ui: folder','external-ui: ui')
#close the input file
fin.close()
#open the input file in write mode
fin = open("config.yaml", "wt")
#overrite the input file with the resulting data
fin.write(data)
#close the file
fin.close()