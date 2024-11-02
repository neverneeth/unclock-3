from flask import Blueprint, render_template, jsonify, request

alarm_bp = Blueprint('alarm', __name__)

@alarm_bp.route('/', methods=['GET', 'POST'])
def alarm():
    if request.method == 'POST':
        alarm_time = request.form.get('time')
        confirmation_times = [alarm_time]  # Placeholder logic
        output = f"Alarm set for: {alarm_time}, Confirmation times: {confirmation_times}"
    else:
        output = "Set an alarm time."
    return render_template('feature.html', feature="Alarm", output=output)
