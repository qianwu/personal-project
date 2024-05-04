# This is a lib for file operations

class file_solution:
    def __init__(self,file_path):
        self.file_path = file_path
        

    # read file and return the content
    def read_file(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            return file.read()
   
    def read_file_line_by_line(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            return file.readlines()

    # write file
    def write_file(self,data):
        with open(self.file_path, "w") as file:
            file.write(data)
            file.close()
    


file_util = file_solution("test.txt")
# file_util.write_file("Today is a good day! \n I am happy! \n I am learning Python!")
# print(file_util.read_file())
print(file_util.read_file_line_by_line())
