

def greet(fx):
    def mfx():
        print("good morning")
        fx()
        print("thanks")
    return mfx

@greet
def hello():
    print("hello world")
hello()