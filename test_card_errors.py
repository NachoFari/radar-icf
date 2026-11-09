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

    print("Checking each card for errors...")
    errors = eval_expr("""
      DATA.map((o, i) => {
        try {
          card(o);
          return null;
        } catch(e) {
          return 'Item ' + i + ' (' + o.name + '): ' + e.toString();
        }
      }).filter(Boolean)
    """)
    print("Errors in card():", errors)

    print("Calling render() manually...")
    render_res = eval_expr("""
      try {
        render();
        'OK, cards count: ' + document.querySelectorAll('.card').length;
      } catch(e) {
        'RENDER ERROR: ' + e.toString() + ' at ' + e.stack;
      }
    """)
    print("Render result:", render_res)

    ws.close()
except Exception as e:
    print("Error:", e)
finally:
    proc.kill()
    time.sleep(0.5)
    shutil.rmtree(temp_profile, ignore_errors=True)
