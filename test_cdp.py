# -*- coding: utf-8 -*-
import urllib.request
import json
import asyncio
import sys

# Check python websockets or use simple cdp client
# Let's see if we can use a basic python script with raw websockets or inspect tabs
tabs = json.loads(urllib.request.urlopen('http://localhost:9222/json').read().decode())
target = [t for t in tabs if 'radar-icf-utfsm.html' in t.get('url', '')][0]
print("Found target tab:", target['id'], target['webSocketDebuggerUrl'])

# We can connect using asyncio and websockets or standard library socket
import socket
import base64
import os

# Let's write a minimal websocket client to evaluate JS in the page
import urllib.parse
ws_url = target['webSocketDebuggerUrl']
parsed = urllib.parse.urlparse(ws_url)

import websocket

ws = websocket.create_connection(ws_url)
print("Connected to WebSocket CDP!")

# Enable Runtime and Console
ws.send(json.dumps({"id": 1, "method": "Runtime.enable"}))
ws.send(json.dumps({"id": 2, "method": "Log.enable"}))

# Evaluate: check state and simulate click on tabs
def eval_js(expr):
    msg_id = int(time.time() * 1000) % 100000
    ws.send(json.dumps({
        "id": msg_id,
        "method": "Runtime.evaluate",
        "params": {"expression": expr, "returnByValue": True}
    }))
    while True:
        resp = json.loads(ws.recv())
        if resp.get("id") == msg_id:
            return resp.get("result", {}).get("result", {}).get("value")

import time
print("Initial state.kind:", eval_js("state.kind"))
print("Initial grid cards count:", eval_js("document.querySelectorAll('#grid .card').length"))

# Click on tab 'beca'
print("Clicking tab 'beca'...")
eval_js("document.querySelector('[data-k=\"beca\"]').click()")
time.sleep(0.5)
print("After click state.kind:", eval_js("state.kind"))
print("After click grid cards count:", eval_js("document.querySelectorAll('#grid .card').length"))

# Click on tab 'ind'
print("Clicking tab 'ind'...")
eval_js("document.querySelector('[data-k=\"ind\"]').click()")
time.sleep(0.5)
print("After click state.kind:", eval_js("state.kind"))
print("After click grid cards count:", eval_js("document.querySelectorAll('#grid .card').length"))

# Click on tab 'prof'
print("Clicking tab 'prof'...")
eval_js("document.querySelector('[data-k=\"prof\"]').click()")
time.sleep(0.5)
print("After click state.kind:", eval_js("state.kind"))
print("After click grid cards count:", eval_js("document.querySelectorAll('#grid .card').length"))

ws.close()
