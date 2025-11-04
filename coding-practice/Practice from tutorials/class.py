class Human:
    def __init__(self,n,o):
        self.name = n
        self.occupation = o
    def do_work(self):
        if self.occupation == "Engineer":
            print(self.name,"He is Engineer")
        elif self.occupation == "Developer":
            print(self.name,"He is Developer")
    def speek(self):
        print("How are you?")
ani =Human("Anil","Engineer")
ani.do_work()
ani.speek()

manasa =Human("Manasa","developer")
manasa.do_work()
manasa.speek()