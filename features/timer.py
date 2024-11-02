from flask import Blueprint, render_template, request
import requests

timer_bp = Blueprint('timer', __name__)

def calculate_dilation_factor(latitude, longitude):
    """Calculates a time dilation factor based on weather data.

    Args:
        latitude (float): Latitude of the location.
        longitude (float): Longitude of the location.

    Returns:
        float: Time dilation factor.
    """

    # Use OpenWeather's free API (limited to free-tier capabilities)
    api_key = '9b6e6a702e186c37bbc599a575b139b2'  # Replace with your actual API key
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric'

    response = requests.get(url)
    if response.status_code != 200:
        return 1.0  # Default dilation factor in case of failure

    data = response.json()

    # Extract weather parameters
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    precipitation = data['rain']['1h'] if 'rain' in data and '1h' in data['rain'] else 0
    pressure = data['main']['pressure']

    # Normalize parameters (adjust ranges as needed)
    normalized_temperature = (temperature - 10) / 30
    normalized_humidity = humidity / 100
    normalized_wind_speed = wind_speed / 20
    normalized_precipitation = precipitation / 10
    normalized_pressure = (pressure - 1013) / 30

    # Calculate weighted average (adjust weights as needed)
    severity_index = (
        0.3 * normalized_temperature +
        0.25 * normalized_humidity +
        0.2 * normalized_wind_speed +
        0.15 * normalized_precipitation +
        0.1 * normalized_pressure
    )

    # Map severity index to dilation factor (adjust ranges as needed)
    if severity_index < 0.25:
        dilation_factor = 0.3  # Slightly faster
    elif severity_index < 0.5:
        dilation_factor = 0.67  # Slightly slower
    else:
        dilation_factor = 2.00  # Significantly slower

    return dilation_factor

@timer_bp.route('/')
@timer_bp.route('/timer', methods=['GET'])
def timer():
    latitude = request.args.get('lat', default=0.0, type=float)
    longitude = request.args.get('lon', default=0.0, type=float)
    duration = 3600  # Example: 1-hour timer
    dilation_factor = calculate_dilation_factor(latitude, longitude)

    return render_template('timer.html', duration=duration, dilation_factor=dilation_factor)

@timer_bp.route('/set_timer', methods=['POST'])
def set_timer():
    # Get the duration from the request form
    duration = int(request.form.get('duration'))

    # You can implement logic here to store the timer duration
    # in a session or database (optional)

    # Render the timer page with the set duration and dilation factor
    return render_template('timer.html', duration=duration)
