class Student:
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")
        
    def raise_hand(self):
        print("Pick me!")
    pass

class ChattyStudent(Student):
    def __init__(self,greeting="How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died..."):
        super().__init__()
        self.greeting = greeting
    def hello(self):
        inherited_greetings= super().hello()
        # print(inherited_greetings)
        # print(self.greeting)
        return f"{inherited_greetings}\n {self.greeting}"
    def raise_hand(self):
        for i in range(10):
            super().raise_hand()
    pass
net = ChattyStudent()
print(net.raise_hand())