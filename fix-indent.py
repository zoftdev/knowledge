import os
import re

def fix_indent():
    #interate file .md under content dir
    for root, dirs, files in os.walk("content"):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                print(file_path)
                with open(file_path, "r") as f:
                    lines = f.readlines()
                
                modified_lines = []
                prev_line_num = 0
                prev_indent=""
                in_block=False
                for line_num, line in enumerate(lines):    
                    if in_block:
                        if len(prev_indent) > 0:                                                         
                            modified_lines.append(prev_indent + line )
                        if re.match(r"^\s*```", line):
                            in_block=False                        
                        continue

                    #if line start with ! without indent then add indent equal to preceding line
                    if re.match(r"^\s*!", line):
                        if len(prev_indent) > 0:                                                         
                            modified_lines.append(prev_indent +"  "+ line )
                        else:
                            modified_lines.append(line )
                        continue

                    #print(line)
                    #if line start with ` and no indent then add indent equal to preceding line
                    if re.match(r"^\s*`", line):
                        #check if line contain only ```
                        if re.match(r"^\s*```", line):
                            in_block=True
                            

                        print("line: ", line)
                        print("prev_line", lines[prev_line_num])
                        if len(prev_indent) > 0:                                                         
                            modified_lines.append(prev_indent + line )
                        else:
                            modified_lines.append(line )
                    else:
                        modified_lines.append(line)
                        if  line.strip():
                            prev_line_num = line_num    
                            indent= re.match(r"^\s*", line).group()
                            print("len,line: ", len(indent),line)
                            print(line)
                            prev_indent= re.match(r"^\s*", line).group()
                            print("prev_indent: ", len(prev_indent))
                    
                    
                    
                
                with open(file_path, "w") as f:
                    f.writelines(modified_lines)
 
if __name__ == "__main__":
    fix_indent()