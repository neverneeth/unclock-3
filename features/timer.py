from flask import Blueprint, render_template, request

timer_bp = Blueprint('timer', __name__)

@timer_bp.route('/')
def timer():
  return render_template('timer.html')

@timer_bp.route('/set_timer', methods=['POST'])
def set_timer():
  # Get the duration from the request form
  duration = int(request.form.get('duration'))

  # You can implement logic here to store the timer duration 
  # in a session or database (optional)

  # Render the timer page with the set duration
  return render_template('timer.html', duration=duration)