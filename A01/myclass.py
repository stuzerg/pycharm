class MyClass():
    def f(self):
        return 155


mc2 = MyClass()
print("It's for test too", mc2.f())

if __name__ == "__main__":
    mc = MyClass()
    print("внутри майкласа с проверкой на мэйн", mc.f())
