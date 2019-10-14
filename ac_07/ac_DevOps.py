import os
from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():
    num = int(input())
        l = []
        ini = 1
        while True:
            if i > 1:
                for ini in range(2,ini):
                    if (ini % i) == 0:
                    
                else:
                    l.append(ini)
            if (len(l) == num):
                print(l)
                
            else:
                ini += 1


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)