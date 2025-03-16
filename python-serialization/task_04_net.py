#!/usr/bin/env python3
"""
This module contains functions to start a server that listens for incoming connections and prints received data,
and to send a dictionary to the server.
"""
import socket
import threading
import pickle

def start_server():
    """
    Start a server that listens for incoming connections and prints received data.
    """

    host = '127.0.0.1'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            data = conn.recv(1024)
            received_dict = pickle.loads(data)
            print("Received Dictionary from Client:")
            print(received_dict)

def send_data(data_dict):
    """
    Send a dictionary to the server.
    
    Parameters:
    data_dict (dict): The dictionary to send.
    """
    
    host = '127.0.0.1'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        serialized_data = pickle.dumps(data_dict)
        client_socket.sendall(serialized_data)
