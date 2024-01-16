deuxethyldeuxmethylhexane = [1,[1,[1,1],[1]],1,1,1]
alcane_inconnu = [1,[1,[1,1]],[1,[1],[1,1]],1,1,1]
methylepropane = [[1,1],1,1]
cinqunmethylpropyldecane = [1,1,1,1,1,methylepropane,1,1,1,1,1]

i = 0
name = []
group = ["error","meth","eth","prop","but","pent","hex","hept","oct","non","dec","undec"]
num = ["error","","di","tri","tetra"]
level = 0
alcane = "C#CCCC(C=C)CC=CC"
length = len(alcane)
remember = 0
def get_branch() :
  global i
  global length
  global name
  global group
  global num
  global level
  global alcane
  global remember
  size = 0
  ram_pos = 0
  is_double = False
  is_triple = False
  double_pos = []
  triple_pos = []
  level += 1
  while i < length :
    cur = alcane[i]
    if cur == " " :
      i += 1
      continue
    elif cur == "(" :
      i += 1
      ram_pos = size
      if level > 1 :
        name.append("(")
        remember = level + 1
      name.append(ram_pos)
      get_branch()
      level -= 1
    elif cur == ")" :
      name.append(group[size])
      if is_double == True :
        for j in range(len(double_pos)) :
          if double_pos[j] > 1 :
            name.append(double_pos[j])
        num_doubles = num[len(double_pos)]
        name.append(num_doubles + "en")
      if is_triple == True :
        for k in range(len(triple_pos)) :
          if triple_pos[k] > 1 :
            name.append(triple_pos[k])
        num_triples = num[len(triple_pos)]
        name.append(num_triples + "yn")
      name.append("yl")
      if level < remember :
        name.append(")")
      return
    elif cur.isalpha() :
      size += 1
    elif cur == "=" :
      double_pos.append(size)
      is_double = True
    elif cur == "#" :
      triple_pos.append(size)
      is_triple = True
    else :
      print "error: unexpected charachter: ", cur, " in position: ", i+1
      quit()
    i += 1
  name.append(group[size])
  if is_double == True :
    for j in range(len(double_pos)) :
      if double_pos[j] > 1 :
        name.append(double_pos[j])
    num_doubles = num[len(double_pos)]
    name.append(num_doubles + "en")
  if is_triple == True :
    for k in range(len(triple_pos)) :
      if triple_pos[k] > 1 :
        name.append(triple_pos[k])
    num_triples = num[len(triple_pos)]
    name.append(num_triples + "yn")
  if is_double == False :
    if is_triple == False :
      name.append("an")
  name.append("e")
  return

get_branch()
print name
