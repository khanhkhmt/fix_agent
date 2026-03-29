#!/usr/bin/env python3
"""Quick SSH test using paramiko"""
import paramiko
import sys

HOST = "103.253.20.182"
PORT = 9996
USER = "root"
PASS = "nixxyn-dotta9-Cusfok"

def run(client, cmd, timeout=60):
    print(f"\n>>> {cmd}")
    stdin, stdout, stderr = client.exec_command(cmd, timeout=timeout)
    out = stdout.read().decode()
    err = stderr.read().decode()
    if out:
        print(out)
    if err:
        print("STDERR:", err, file=sys.stderr)
    return out

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(HOST, port=PORT, username=USER, password=PASS, 
                   look_for_keys=False, allow_agent=False, timeout=15)
    print("=== SSH CONNECTION SUCCESSFUL ===")
    run(client, "uname -a")
    run(client, "free -h")
    run(client, "df -h /")
    run(client, "docker --version 2>/dev/null || echo 'Docker NOT installed'")
except Exception as e:
    print(f"ERROR: {e}")
finally:
    client.close()
