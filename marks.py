import json
import pathlib
import os 
class Marks:
    def __init__(self, objname):
        
        self.directory = "StuMarks"
        
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
            
        self.file = os.path.join(self.directory, f"Marks_{objname}.json")
    
    def create_marks_file(self):
        if pathlib.Path(self.file).exists():
            pass
        else:
            with open(self.file,"x") as fl:
                json.dump([],fl)


    def marks_file_write(self,a):
        with open(self.file,'w') as fl:
            json.dump(a,fl,indent=3)

    def marks_file_read(self):
        with open(self.file,'r') as fl:
            data = json.load(fl)
        return data