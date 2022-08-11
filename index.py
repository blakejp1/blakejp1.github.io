
import pyodide

def on_clicks(e): 
    outputHandle.innerText= inputHandle *2

changeButtonHandle = document.getElementById('change_me')
inputHandle = document.getElementById('input')
outputHandle = document.getElementById('output')


changeButtonHandle.addEventListener('click',pyodide.create_proxy(on_clicks))


