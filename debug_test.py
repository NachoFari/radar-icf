# -*- coding: utf-8 -*-
with open(r'C:\Users\Nacho\Desktop\radar-icf-utfsm.html', encoding='utf-8') as f:
    text = f.read()

print("Contains addEventListener tabs:", 'document.getElementById("tabs").addEventListener' in text)
print("Contains render():", 'function render()' in text)
