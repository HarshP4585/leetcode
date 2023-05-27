class A:
    def show(self):
        print("in a")

class B:
    def show(self):
        print("in b")

class C(A, B):
    def show(self):
        print("in c")
        super().show()

C().show()
