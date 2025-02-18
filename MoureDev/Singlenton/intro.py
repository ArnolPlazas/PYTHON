class Singlenton:
    _instance = None

    # __new__ is responsible for creating and returning a new instance (object). s called before __init__
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singlenton, cls).__new__(cls)
        return cls._instance


singlenton1 = Singlenton()
print(singlenton1)
singlenton2 = Singlenton()
print(singlenton2)

print(singlenton1 is singlenton2)
    
