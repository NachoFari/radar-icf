# -*- coding: utf-8 -*-
import subprocess, time, urllib.request, json, os, shutil, websocket, sys
sys.stdout.reconfigure(encoding='utf-8')

temp_profile = r'C:\Users\Nacho\Desktop\edge-temp-profile'
if os.path.exists(temp_profile):
    shutil.rmtree(temp_profile, ignore_errors=True)

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
    target = [t for t in tabs if 'radar-icf-utfsm.html' in t.get('url', '')][0]
    ws = websocket.create_connection(target['webSocketDebuggerUrl'])

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
                res = r.get("result", {})
                if "exceptionDetails" in res:
                    return "EXCEPTION: " + str(res["exceptionDetails"])
                return res.get("result", {}).get("value")

    print("Initial cards in DOM:", eval_expr("document.querySelectorAll('#grid .card').length"))

    # Click beca
    eval_expr("document.querySelector('[data-k=\"beca\"]').click()")
    time.sleep(0.2)
    print("After BECAS click: state.kind =", eval_expr("state.kind"), "| cards =", eval_expr("document.querySelectorAll('#grid .card').length"))

    # Click ind
    eval_expr("document.querySelector('[data-k=\"ind\"]').click()")
    time.sleep(0.2)
    print("After PRÁCTICA INDUSTRIAL click: state.kind =", eval_expr("state.kind"), "| cards =", eval_expr("document.querySelectorAll('#grid .card').length"))

    # Click prof
    eval_expr("document.querySelector('[data-k=\"prof\"]').click()")
    time.sleep(0.2)
    print("After PRÁCTICA PROFESIONAL click: state.kind =", eval_expr("state.kind"), "| cards =", eval_expr("document.querySelectorAll('#grid .card').length"))

    # Click desc
    eval_expr("document.querySelector('[data-k=\"desc\"]').click()")
    time.sleep(0.2)
    print("After DESCUENTOS click: state.kind =", eval_expr("state.kind"), "| cards =", eval_expr("document.querySelectorAll('#grid .card').length"))

    # Click all
    eval_expr("document.querySelector('[data-k=\"all\"]').click()")
    time.sleep(0.2)
    print("After TODO click: state.kind =", eval_expr("state.kind"), "| cards =", eval_expr("document.querySelectorAll('#grid .card').length"))

    ws.close()
except Exception as e:
    print("Error:", e)
finally:
    proc.kill()
    time.sleep(0.5)
    shutil.rmtree(temp_profile, ignore_errors=True)
