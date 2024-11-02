from flask import Flask, render_template
from features.world_clock import world_clock_bp
from features.stopwatch import stopwatch_bp
from features.timer import timer_bp
from features.alarm import alarm_bp

app = Flask(__name__)
app.secret_key = 'kootukare_ningal_secret_key_kando'

# Register the blueprints for each feature
app.register_blueprint(world_clock_bp, url_prefix='/world_clock')
app.register_blueprint(stopwatch_bp, url_prefix='/stopwatch')
app.register_blueprint(timer_bp, url_prefix='/timer')
app.register_blueprint(alarm_bp, url_prefix='/alarm')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port = 6869)
