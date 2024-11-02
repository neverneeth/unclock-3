from flask import Blueprint, render_template, jsonify
import random

timer_bp = Blueprint('timer', __name__)

@timer_bp.route('/')
def timer():
    weather = random.choice(["sunny", "rainy", "cloudy"])
    accuracy = {"sunny": 95, "cloudy": 70, "rainy": 30}[weather]  # % accuracy
    output = f"Weather: {weather}, Accuracy: {accuracy}%"
    return render_template('feature.html', feature="Timer", output=output)
