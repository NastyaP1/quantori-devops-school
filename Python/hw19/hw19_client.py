import socket


if __name__ == '__main__':
    host = 'localhost'
    port = 9999
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        option = int(input("Enter 0 if you want to check the domain.\nEnter 1 If you want to update domain.\nEnter 2 If "
              "you want to close session.\n"))
        if option == 0:
            data = input("Inter domain name:\n")
            client_socket.sendto(data.encode(), (host, port))
            server_data, sender = client_socket.recvfrom(512)
            print("Result is {}".format(server_data.decode()))
        elif option == 1:
            data = input("Inter domain name and new ip address like - domain:address\n")
            data = 'ADD ' + data.replace(" ", "")
            client_socket.sendto(data.encode(), (host, port))
            server_data, sender = client_socket.recvfrom(512)
            print("Result is {}".format(server_data.decode()))
        elif option == 2:
            exit(0)
        else:
            print("No such option, please, try again")
            exit(2)

        print('----------------------------------------------')
