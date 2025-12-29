import socket
import json
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define remote functions
def add(a, b):
    return a + b

def get_time():
    return time.time()

def reverse_string(s):
    return s[::-1]

# Function mapper
functions = {
    "add": add,
    "get_time": get_time,
    "reverse_string": reverse_string
}

# Server setup
HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    logging.info(f"Server listening on {HOST}:{PORT}")
    
    while True:
        conn, addr = s.accept()
        with conn:
            logging.info(f"Connected by {addr}")
            data = conn.recv(1024).decode('utf-8')
            if not data:
                continue
            
            # Parse request
            try:
                request = json.loads(data)
                method = request.get('method')
                params = request.get('params', {})
                request_id = request.get('request_id', 'unknown')
                
                logging.info(f"Received request: method={method}, params={params}, id={request_id}")
                
                # Simulate delay for failure demo (uncomment for Task 3)
                # time.sleep(5)
                
                if method in functions:
                    result = functions[method](**params)
                    response = {
                        "request_id": request_id,
                        "result": result,
                        "status": "OK"
                    }
                else:
                    response = {
                        "request_id": request_id,
                        "result": None,
                        "status": "ERROR: Method not found"
                    }
            except Exception as e:
                response = {
                    "request_id": request_id if 'request_id' in locals() else "unknown",
                    "result": None,
                    "status": f"ERROR: {str(e)}"
                }
            
            # Send response
            conn.sendall(json.dumps(response).encode('utf-8'))
            logging.info(f"Sent response: {response}")
