class names:
    def __init__(self):
        self.names=[]
    def add_names(self):
        for i in range(0,5):
            name=input("enter name")
            self.names.append(name)
    def print_names(self):
        print(self.names)
    def replace_names(self):
        name=input("enter a name in the list")
        n=self.names.index(name)
        choice=input("do you want to replace the name\n")
        if choice=="yes":
            name=input("enter a new name")
            self.names[n]=name
            print(self.names)
        else:
            print(self.names)
#allowing a user to access the program
def main():
    name=names()
    name.add_names()
    name.print_names()
    name.replace_names()
main()
