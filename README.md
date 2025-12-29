# LAB 1 — Remote Procedure Call (RPC) Implementation & Deployment on AWS EC2

**Course:** Distributed Computing — Trimester 8  
**Estimated time:** 2–3 hours  
**Submission:** Video demo + GitHub repository

## Overview

This project implements a simple **Remote Procedure Call (RPC)** system using **Python 3**, TCP sockets, and JSON serialization. It consists of:
- A **server** exposing multiple remote functions
- A **client** that sends requests with timeouts, retries, and unique request IDs
- Deployment on **two AWS EC2 instances** (one for client, one for server)

The system demonstrates:
- At-least-once semantics (via client-side retries on timeout)
- Failure handling (artificial delay simulation)

## Implemented Features

- **Multiple remote functions**: `add(a, b)`, `get_time()`, `reverse_string(s)`
- **Request/response format**: JSON with `request_id` (UUID), `method`, `params`
- **Client-side**: 2-second timeout, 3 retries, logging
- **Server-side**: TCP socket, logging for each request/response
- **Error handling**: Method not found, invalid requests
- **Failure demo**: Artificial server delay (5 seconds) to trigger client retries

## EC2 Deployment Details

- **Server Node** (rpc-server-node)  
  Public IP: **50.17.105.244**  
  Runs: `server.py`

- **Client Node** (rpc-client-node)  
  Public IP: (replace with your actual client public IP, e.g., 3.80.125.18)  
  Runs: `client.py`

- **Port**: 5000 (TCP)  
- **Security Group**: Inbound rules allow TCP 5000 from 0.0.0.0/0 (or your client IP)  
- **OS**: Ubuntu 22.04

## Files

- `server.py` — RPC server (listens on port 5000)
- `client.py` — RPC client (sends requests to server)
- `README.md` — This file

## How to Run

### Prerequisites

- Two AWS EC2 instances running Ubuntu 22.04
- Python 3 installed (`sudo apt update && sudo apt install python3 python3-pip -y`)
- Security group allows inbound TCP port 5000

### On the Server Instance (rpc-server-node, IP: 50.17.105.244)

1. SSH into the instance:
   ```bash
   ssh -i rpc-key.pem ubuntu@50.17.105.244
