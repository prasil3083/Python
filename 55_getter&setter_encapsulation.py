class student:
    __name="prasil"
    def __init__(a):                            #-->private function and objects are can't br called directli we have to call them by using counstructor
        print(a.__name)
        a.__A1()

    def __A1(a):
        print("hii prasil")

obj=student()
