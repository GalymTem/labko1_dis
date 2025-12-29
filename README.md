# LAB 1 — Remote Procedure Call (RPC) Implementation & Deployment on AWS EC2

**Course:** Distributed Computing — Trimester 8  
**Estimated time:** 2–3 hours  
**Submission:** Video demo (1–2 min) + GitHub repository

## 1. Lab Objectives

This lab allowed me to:
- Implement a simple RPC protocol in Python
- Understand RPC components: client stub, server stub, marshalling, network transport
- Deploy a real client-server distributed application on **two AWS EC2 instances**
- Observe communication failures, retry logic, and behavior under delays
- Evaluate **at-least-once** semantics (achieved via client retries)

## 2. What I Built

I implemented a minimal RPC system with:
- **Server** (runs on EC2 instance with public IP: `50.17.105.244`)
  - Exposes three remote functions: `add(a, b)`, `get_time()`, `reverse_string(s)`
  - Listens on TCP port 5000
  - Uses JSON for marshalling/unmarshalling

- **Client** (runs on separate EC2 instance)
  - Sends requests with unique UUID request IDs
  - Handles 2-second timeouts + 3 retries
  - Prints results or errors

- **Deployment**: Two t2.micro Ubuntu 22.04 instances in AWS EC2

<img width="1645" height="211" alt="image" src="https://github.com/user-attachments/assets/8e7ec758-7b19-47a4-8a99-c75968d94993" />

## 3. Pre-Lab Setup

- Launched two Ubuntu 22.04 instances:  
  - `rpc-client-node`  
  - `rpc-server-node` (public IP: 50.17.105.244)

- Security Group inbound rules:  
  - SSH (port 22) from my IP  
  - TCP 5000 from anywhere (0.0.0.0/0) for testing

- Installed dependencies on both:
  ```bash
  sudo apt update
  sudo apt install python3 python3-pip -y

  ping 50.17.105.244
  nc -vz 50.17.105.244 5000
<img width="800" height="386" alt="image" src="https://github.com/user-attachments/assets/3e8b53ab-1623-45d7-8080-04971f27395e" />

## 4. Implementation

RPC Message Structure (JSON)
- Request example::
  ```bash
  "request_id": "123e4567-e89b-12d3-a456-426614174000",
  "result": 12,
  "status": "OK"

- Key Features Implemented::
  ```bash
  Multiple methods (add, get_time, reverse_string)
  Unique request IDs (UUID)
  Client-side timeout (2s) + retries (3 attempts)
  Logging on both sides
  Failure demo support (artificial delay)
  
## 5 Result:
<img width="1460" height="298" alt="image" src="https://github.com/user-attachments/assets/c8707a07-6ca0-4397-a25b-ebbafabad60d" />

<img width="1334" height="230" alt="image" src="https://github.com/user-attachments/assets/57cb880b-0083-45de-8987-a56e25bcc2ae" />

https://github.com/GalymTem/labko1_dis/edit/main/README.md
