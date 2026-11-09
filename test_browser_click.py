# -*- coding: utf-8 -*-
import subprocess
import time
import urllib.request
import json
import os
import shutil

temp_profile = r'C:\Users\Nacho\Desktop\edge-temp-profile'
if os.path.exists(temp_profile):
    shutil.rmtree(temp_profile, ignore_errors=True)

# Launch Edge with dedicated user data dir and debugging port
msedge_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
if not os.path.exists(msedge_path):
    msedge_path = r'C:\Program Files\Microsoft\Edge\Application\msedge.exe'

cmd = [
    msedge_path,
    '--headless',
    '--remote-debugging-port=9333',
    '--remote-allow-origins=*',
    f'--user-data-dir={temp_profile}',
    'file:///C:/Users/Nacho/Desktop/radar-icf-utfsm.html'
]
proc = subprocess.Popen(cmd)
time.sleep(2)

try:
    tabs = json.loads(urllib.request.urlopen('http://localhost:9333/json').read().decode())
    print("Edge tabs:", len(tabs))
    target = tabs[0]
    ws_url = target['webSocketDebuggerUrl']
    
    import websocket
    ws = websocket.create_connection(ws_url)
    print("Connected to Edge WebSocket!")

    def eval_expr(expr):
        msg = {
            "id": 10,
            "method": "Runtime.evaluate",
            "params": {"expression": expr, "returnByValue": True}
        }
        ws.send(json.dumps(msg))
        while True:
            r = json.loads(ws.recv())
            if r.get("id") == 10:
                return r.get("result", {}).get("result", {}).get("value")

    print("Initial state.kind:", eval_expr("state.kind"))
    print("Initial grid cards:", eval_expr("document.querySelectorAll('#grid .card').length"))

    # Test click on tab 'beca'
    eval_expr("document.querySelector('[data-k=\"beca\"]').click()")
    time.sleep(0.3)
    print("After beca click: state.kind =", eval_expr("state.kind"))
    print("After beca click: cards =", eval_expr("document.querySelectorAll('#grid .card').length"))

    # Test click on tab 'ind'
    eval_expr("document.querySelector('[data-k=\"ind\"]').click()")
    time.sleep(0.3)
    print("After ind click: state.kind =", eval_expr("state.kind"))
    print("After ind click: cards =", eval_expr("document.querySelectorAll('#grid .card').length"))

    # Test click on tab 'prof'
    eval_expr("document.querySelector('[data-k=\"prof\"]').click()")
    time.sleep(0.3)
    print("After prof click: state.kind =", eval_expr("state.kind"))
    print("After prof click: cards =", eval_expr("document.querySelectorAll('#grid .card').length"))

    # Test click on tab 'all'
    eval_expr("document.querySelector('[data-k=\"all\"]').click()")
    time.sleep(0.3)
    print("After all click: state.kind =", eval_expr("state.kind"))
    print("After all click: cards =", eval_expr("document.querySelectorAll('#grid .card').length"))

    ws.close()
except Exception as e:
    print("Error:", e)
finally:
    proc.kill()
    time.sleep(0.5)
    shutil.rmtree(temp_profile, ignore_errors=True)
