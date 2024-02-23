class training:
    def __init__(self,lang):
        self.lang=lang
    def section1(self):
        print("Training section1:",self.lang)
    def section2(self):
        print("Training section2:",self.lang)
obj=training("Python")
obj.section1()
obj.section2()
