from flask import Flask, render_template, request
from config import language, restrictions, FILE_EXTENSION, FLAG_LIST
import os
import shlex
import subprocess
from secrets import token_hex
import builtins

output_most = restrictions["output_limit"]
timeout = restrictions["time_limit"]

app = Flask(__name__)

@app.route("/")
def hello():
  return render_template("interpreter.html", language=language, restrictions=restrictions, flags=FLAG_LIST, **builtins.__dict__)

@app.route("/interpret/", methods=["POST"])
def interpret():
  code = request.json["code"]
  inp = request.json["input"]
  flag = request.json["flag"]
  dom = "temp_programs/" + token_hex(64)
  no_inp = False
  with open(dom + FILE_EXTENSION, "x") as cod:
    cod.write(code)
  if inp != '':
    with open(dom + ".txt", "x") as inn:
      inn.write(inp)
  else:
      no_inp = True
  c_path = dom + FILE_EXTENSION
  i_path = dom + ".txt"
  p_path = "program.py"
  try:
    data = subprocess.run(shlex.split(f'python "{p_path}" -p "{c_path}" {f"-i {i_path}" if not no_inp else ""} -f {flag}'), capture_output=True, text=True, timeout=timeout)
    out_warning = len(data.stdout) > output_most
    err_warning = len(data.stderr) > output_most
    os.remove(c_path)
    os.remove(i_path)
    return {"output": data.stdout[:output_most], "error": data.stderr[:output_most], "timeout_warning": False, "memory_warning": {"stdout": out_warning, "stderr": err_warning}}
  except subprocess.TimeoutExpired as e:
    out = e.stdout
    if out is None:
      out = ''
    else:
      out = out.decode('utf-8')
    err = e.stderr
    if err is None:
      err = ''
    else:
      err = err.decode('utf-8')
    out_warning = len(data.stdout) > output_most
    err_warning = len(data.stderr) > output_most
    os.remove(c_path)
    os.remove(i_path)
    return {"output": out[:output_most], "error": err[:output_most], "timeout_warning": True, "memory_warning": {"stdout": out_warning, "stderr": err_warning}}
