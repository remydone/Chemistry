deuxethyldeuxmethylhexane = [1,[1,[1,1],[1]],1,1,1]
alcane_inconnu = [1,[1,[1,1]],[1,[1],[1,1]],1,1,1]
methylepropane = [[1,1],1,1]
cinqunmethylpropyldecane = [1,1,1,1,1,methylepropane,1,1,1,1,1]

alcane = "CC=C(CCC)C=C(C C)(C) C#C"

##def group(size):
##  if size == 1 : return "meth"
##  if size == 2 : return "eth"
##  if size == 3 : return "prop"
##  if size == 4 : return "but"
##  if size == 5 : return "pent"
##  if size == 6 : return "hex"
##name = []
##for i in range(len(alcane)):
##  cur = alcane[i]
##  if type(cur) is list: #ramification
##    for j in range(len(cur)-1): #skip the part of the main strain
##      very_cur = cur[j+1] #again
##      name.append(i+1) #placement of the ramification
##      ram = group(very_cur)#get name of ramification
##      name.append(ram + "yl")#add name of ramification to the name of the alcane
##total_size = group(alcane)#get name of alcane's main strain
##name.append(total_size)#add alcane size to alcane name
##name.append("ane")

name = []
ram = []
main = []
is_ram = False
ram_size = 0
size = 0
ram_pos = 0
not_main = 0
is_double = False
is_triple = False
double_pos = []
triple_pos = []
group = ["error","meth","eth","prop","but","pent","hex","hept","oct","non"]
num = ["error","","di","tri","tetra"]
for i in range(len(alcane)) :
  cur = alcane[i]
  if cur == " " :
    not_main += 1
    continue
  elif cur == "(" :
    is_ram = True
    ram_pos = i - not_main
    not_main += 1
  elif cur == ")" :
    is_ram = False
    name.append(ram_pos)
    name.append(group[ram_size] + "yl")
    ram = []
    ram_size = 0
    not_main += 1
  elif cur.isalpha() :
    if is_ram == True :
      ram_size += 1
      not_main += 1
    else : size += 1
  elif cur == "=" :
    if is_ram == False :
      double_pos.append(i - not_main)
      is_double = True
    not_main += 1
  elif cur == "#" :
    if is_ram == False :
      triple_pos.append(i - not_main)
      is_triple = True
    not_main += 1
  else :
    print "error: unexpected charachter: ", cur, " in position: ", i+1
    quit()
name.append(group[size])
if is_double == True :
  for j in range(len(double_pos)) :
    name.append(double_pos[j])
  num_doubles = num[len(double_pos)]
  name.append(num_doubles + "ene")
if is_triple == True :
  for k in range(len(triple_pos)) :
    name.append(triple_pos[k])
  num_triples = num[len(triple_pos)]
  name.append(num_triples + "yne")
if is_double == False :
  if is_triple == False :
    name.append("ane")
print name
