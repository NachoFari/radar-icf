# -*- coding: utf-8 -*-
import subprocess, time, urllib.request, json, os, shutil, websocket

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
    # find the tab with radar-icf-utfsm.html
    target = [t for t in tabs if 'radar-icf-utfsm.html' in t.get('url', '')][0]
    print("Found tab:", target['url'])
    ws_url = target['webSocketDebuggerUrl']
    ws = websocket.create_connection(ws_url)

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

    print("Title:", eval_expr("document.title"))
    print("state:", eval_expr("typeof state"))
    print("DATA length:", eval_expr("typeof DATA !== 'undefined' ? DATA.length : 'undefined'"))
    print("Cards:", eval_expr("document.querySelectorAll('.card').length"))
    print("Tabs HTML:", eval_expr("document.getElementById('tabs').innerHTML"))

    # Now let's click
    print("Clicking beca...")
    eval_expr("document.querySelector('[data-k=\"beca\"]').click()")
    print("state.kind after click:", eval_expr("state.kind"))
    print("Cards after click:", eval_expr("document.querySelectorAll('.card').length"))
    
    # What was the error if any?
    ws.close()
except Exception as e:
    print("Error:", e)
finally:
    proc.kill()
    time.sleep(0.5)
    shutil.rmtree(temp_profile, ignore_errors=True)
