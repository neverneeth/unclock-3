from flask import Blueprint, render_template, jsonify, session
from datetime import datetime, timedelta, timezone
import random
import units

stopwatch_bp = Blueprint('stopwatch', __name__)

def pick_unit():
    unit_name = random.choice(units.unit_list)
    unit_val = units.unit_dict.get(unit_name, 0.1)  # Default to 0.1 if not found
    return unit_val, unit_name

@stopwatch_bp.route('/')
def stopwatch():
    # Initialize session variables if they don't exist
    if 'elapsed_time' not in session:
        session['elapsed_time'] = 0  # Store as seconds
    if 'running' not in session:
        session['running'] = False
    if 'unit' not in session:
        session['unit'], session['unitname'] = pick_unit()
    return render_template('stopwatch.html')

@stopwatch_bp.route('/start', methods=['POST'])
def start():
    if not session.get('running', False):
        session['start_time'] = datetime.now(timezone.utc)  # Set timezone-aware datetime
        session['running'] = True
        session['unit'], session['unitname'] = pick_unit()
    return jsonify(success=True)

@stopwatch_bp.route('/stop', methods=['POST'])
def stop():
    if session.get('running', False):
        # Calculate elapsed time in seconds and add it to stored time
        elapsed = (datetime.now(timezone.utc) - session.get('start_time', datetime.now(timezone.utc))).total_seconds()
        session['elapsed_time'] += elapsed
        session['running'] = False
    return jsonify(success=True)

@stopwatch_bp.route('/reset', methods=['POST'])
def reset():
    session['elapsed_time'] = 0  # Reset to 0 seconds
    session['running'] = False
    return jsonify(success=True)

@stopwatch_bp.route('/get_time', methods=['GET'])
def get_time():
    if session.get('running', False):
        # Calculate current time in seconds
        elapsed = (datetime.now(timezone.utc) - session['start_time']).total_seconds()
        current_time = session['elapsed_time'] + elapsed
    else:
        current_time = session['elapsed_time']
    
    # Convert to display time based on selected unit
    displayed_time = int(current_time / session['unit'])

    return jsonify(time=displayed_time, unitname=session['unitname'])
