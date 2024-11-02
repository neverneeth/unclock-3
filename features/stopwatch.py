from flask import Blueprint, render_template, jsonify
import random

stopwatch_bp = Blueprint('stopwatch', __name__)

@stopwatch_bp.route('/')
def stopwatch():
    time_units = ["wobbles", "flutters", "twirls"]
    unit = random.choice(time_units)
    time_value = random.randint(1, 100)  # Random number in the absurd unit
    output = f"{time_value} {unit}"
    return render_template('feature.html', feature="Stopwatch", output=output)
