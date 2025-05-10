import Pyro4
import time

def tail_file(file_path, callback):
    """Lee líneas nuevas que se escriban al archivo"""
    with open(file_path, "r") as f:
        f.seek(0, 2)  # mover al final
        while True:
            line = f.readline()
            if not line:
                time.sleep(1)
                continue
            callback(line.strip())

def main():
    log_file = "log.txt"
    server = Pyro4.Proxy("PYRONAME:log.server")

    def send_log(line):
        print(f"Enviando log: {line}")
        try:
            server.add_log(line)
        except Exception as e:
            print(f"Error al enviar log: {e}")

    print("Cliente RMI escuchando log.txt...")
    tail_file(log_file, send_log)

if __name__ == "__main__":
    main()
