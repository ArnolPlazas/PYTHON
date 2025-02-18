class UserSession:
    _instance = None

    id: int = None
    username: str = None
    name: str  = None
    email: str  = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(UserSession, cls).__new__(cls)
        return cls._instance
    

    def __str__(self):
        return f'{self.username} {self.name} {self.email}'
    

    def start_session(self, id, username, name, email):
        self.id = id
        self.username = username
        self.name = name
        self.email = email


    def clear_user_session(self):
        self.id = None
        self.username = None
        self.name = None
        self.email = None

session1 = UserSession()
session1.start_session(1, 'jose', 'Jose', 'jose@mail.com')
print(session1)

session2 = UserSession()
print(session2)

session3 = UserSession()
session3.clear_user_session()
print(session3)
print(session1)
    
    

