__author = "Hu Rongyang"
import sys
find_str = sys.argv[1]
realace_str = sys.argv[2]
with open("yesterday2.txt",'r',encoding="utf-8") as f,\
      open("yesterday2.bak",'w',encoding="utf-8") as f_new:
    for line in f:
        if "find_str" in line:
            line = line.replace(find_str,realace_str)
        f_new.write(line)