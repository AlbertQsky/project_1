from flask import Flask, request, jsonify
import sympy as sp
import math
from flask_cors import CORS
import numpy as np

app = Flask(__name__)
CORS(app)

@app.route('/api/calculate', methods=['POST'])
def calculate():
    expression = request.json.get('expression')
    try:
        # 使用math库中的函数
        result = eval(expression, {"__builtins__": None}, {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log,
            "ln": math.log,
            "e": math.e,
            "π": math.pi
        })
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/api/integrate', methods=['POST'])
def integrate():
    function = request.json.get('function')
    limits = request.json.get('limits')
    try:
        function = function.replace('π', 'sp.pi').replace('e', 'sp.E')
        symbols = {limit['variable']: sp.symbols(limit['variable']) for limit in limits}
        integration_limits = [(symbols[limit['variable']], limit['lower'], limit['upper']) for limit in limits]
        result = sp.integrate(function, *integration_limits)
        return jsonify({'result': float(result)})
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/api/plot3d', methods=['POST'])
def plot3d():
    functions = request.json.get('functions')
    try:
        range_val = 8  # 自动设置采样范围
        step = 0.05    # 自动设置采样步长
        epsilon = 0.2  # 自动设置阈值
        x = np.arange(-range_val, range_val + step, step)
        y = np.arange(-range_val, range_val + step, step)
        z = np.arange(-range_val, range_val + step, step)
        X, Y, Z = np.meshgrid(x, y, z)
        all_points = []
        for function in functions:
            # 使用sympy解析函数
            func = sp.sympify(function)
            F = sp.lambdify(('x', 'y', 'z'), func, 'numpy')(X, Y, Z)
            points = np.column_stack((X[np.abs(F) < epsilon], Y[np.abs(F) < epsilon], Z[np.abs(F) < epsilon]))
            all_points.append(points.tolist())
        if all_points == []:
            raise ValueError('没有找到满足条件的点')
        return jsonify({'points': all_points})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

