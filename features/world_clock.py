# features/world_clock.py
from flask import Blueprint, jsonify, render_template
import random
from datetime import datetime
import pytz
from timezonefinder import TimezoneFinder

world_clock_bp = Blueprint('world_clock', __name__)
tf = TimezoneFinder()

@world_clock_bp.route('/')
def world_clock():
    return render_template('world_clock.html')

@world_clock_bp.route('/add_clock', methods=['POST'])
def add_clock():
    lat = random.uniform(-90, 90)
    lon = random.uniform(-180, 180)

    timezone = tf.timezone_at(lng=lon, lat=lat)
    if timezone:
        timezone_obj = pytz.timezone(timezone)
        current_time = datetime.now(timezone_obj).strftime('%H:%M:%S')
        coordinates = f"Lat: {lat:.2f}, Lon: {lon:.2f}"

        return jsonify({
            'success': True,
            'timezone': timezone,
            'coordinates': coordinates,
            'current_time': current_time
        })
    else:
        return jsonify({'success': False, 'error': 'Could not find timezone for the given coordinates'})
