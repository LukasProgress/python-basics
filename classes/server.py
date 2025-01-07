class Server():
    def __init__(self, name, ip, standort):
        self.name = name
        self.ip = ip
        self.standort = standort
    
    def boot(self):
        print(f"Der Server {self.name} mit {self.ip} wird hochgefahren.")

    def shutdown(self):
        print(f"Der Server wird heruntergefahren.")

my_server = Server("Server1", "192.168.0.1", "Frankfurt")
print(my_server.name)

my_server.programs = []
my_server.programs.append("google")
print(my_server.programs)

my_server.boot()
my_server.shutdown()