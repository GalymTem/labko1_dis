import socket
import json
import uuid
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_request(server_host, server_port, method, params, timeout=2, retries=3):
    request_id = str(uuid.uuid4())
    request = {
        "request_id": request_id,
        "method": method,
        "params": params
    }
    request_json = json.dumps(request)
    
    for attempt in range(1, retries + 1):
        try:
            logging.info(f"Attempt {attempt}: Sending {request_json}")
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                s.connect((server_host, server_port))
                s.sendall(request_json.encode('utf-8'))
                
                response_data = s.recv(1024).decode('utf-8')
                response = json.loads(response_data)
                
                logging.info(f"Received: {response}")
                
                if response.get("request_id") != request_id:
                    raise ValueError("Request ID mismatch")
                
                if response["status"] == "OK":
                    print(f"Result: {response['result']}")
                    return response["result"]
                else:
                    print(f"Error: {response['status']}")
                    return None
        except socket.timeout:
            logging.warning(f"Attempt {attempt}: Timeout")
        except Exception as e:
            logging.error(f"Attempt {attempt}: {e}")
        
        time.sleep(1)  # Backoff
    
    print("Max retries reached. Failed.")
    return None

if __name__ == "__main__":
    SERVER_HOST = "50.17.105.244"  # ← Change to your server's public IP if different
    SERVER_PORT = 5000
    
    # Test different functions
    print("Testing add(5, 7):")
    send_request(SERVER_HOST, SERVER_PORT, "add", {"a": 5, "b": 7})
    
    print("\nTesting get_time():")
    send_request(SERVER_HOST, SERVER_PORT, "get_time", {})
    
    print("\nTesting reverse_string('hello'):") 
    send_request(SERVER_HOST, SERVER_PORT, "reverse_string", {"s": "hello"})
