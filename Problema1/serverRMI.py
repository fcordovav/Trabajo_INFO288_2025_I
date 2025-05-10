import Pyro4

@Pyro4.expose
class LogServer:
    def __init__(self):
        self.log_file = "log_central.txt"

    def add_log(self, log_line):
        with open(self.log_file, "a") as f:
            f.write(log_line + "\n")
        print(f"Log agregado: {log_line}")
        return True

def main():
    daemon = Pyro4.Daemon()  # abre un servidor Pyro
    ns = Pyro4.locateNS()
    uri = daemon.register(LogServer)
    ns.register("log.server", uri)

    print("Servidor RMI de logs corriendo.")
    daemon.requestLoop()

if __name__ == "__main__":
    main()
