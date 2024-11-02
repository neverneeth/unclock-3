from flask import Blueprint, render_template, jsonify, session
from datetime import datetime, timezone
import units

stopwatch_bp = Blueprint('stopwatch', __name__)

def pick_unit():
    unit_name, unit_val, unit_phenomena = units.unitgen()  # Default to 0.1 if not found
    return unit_val, unit_name, unit_phenomena

@stopwatch_bp.route('/')
def stopwatch():
    # Initialize session variables if they don't exist
    if 'elapsed_time' not in session:
        session['elapsed_time'] = 0  # Store as seconds
    if 'running' not in session:
        session['running'] = False
    if 'unit' not in session or 'unitname' not in session or 'unitphenon' not in session:
        session['unit'], session['unitname'], session['unitphenon'] = pick_unit()
        session['unitname'] = "Second"
        session['unitphenon'] = "The time taken for a human to realize that he's reading this sentence pointlessly."
    return render_template('stopwatch.html')

@stopwatch_bp.route('/start', methods=['POST'])
def start():
    if not session.get('running', False):
        session['start_time'] = datetime.now(timezone.utc)  # Set timezone-aware datetime
        session['running'] = True
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
    session['unit'], session['unitname'], session['unitphenon'] = pick_unit()
    return jsonify(success=True)

@stopwatch_bp.route('/get_time', methods=['GET'])
def get_time():
    # Ensure all required session keys are set
    if 'unit' not in session or 'unitname' not in session or 'unitphenon' not in session:
        session['unit'], session['unitname'], session['unitphenon'] = pick_unit()

    if session.get('running', False):
        # Calculate current time in seconds
        elapsed = (datetime.now(timezone.utc) - session['start_time']).total_seconds()
        current_time = session['elapsed_time'] + elapsed
    else:
        current_time = session['elapsed_time']
    
    # Convert to display time based on selected unit
    displayed_time = "{:.3f}".format(current_time / session['unit']) if session['unit'] > 3 else "{:.0f}".format(current_time / session['unit'])

    return jsonify(time=displayed_time, unitname=f"""{session['unitname']}s have passed""", unitphenon=session['unitphenon'])
