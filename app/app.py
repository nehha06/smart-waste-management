from flask import Flask, render_template, jsonify
from database import get_connection, initialize_database
from analysis import analyze_waste

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

# Initialize database
initialize_database()


# -------------------------
# Dashboard
# -------------------------
@app.route("/")
def home():

    connection = get_connection()

    bins = connection.execute(
        "SELECT * FROM bins"
    ).fetchall()

    alerts = connection.execute(
        "SELECT * FROM alerts WHERE status = 'OPEN'"
    ).fetchall()

    connection.close()

    total_bins = len(bins)
    total_alerts = len(alerts)

    high_priority = sum(
        1 for bin in bins
        if bin["priority"] == "HIGH"
    )

    normal_bins = sum(
        1 for bin in bins
        if bin["condition"] == "NORMAL"
    )

    return render_template(
        "dashboard.html",
        bins=bins,
        alerts=alerts,
        total_bins=total_bins,
        total_alerts=total_alerts,
        high_priority=high_priority,
        normal_bins=normal_bins
    )


# -------------------------
# API: Get all bins
# -------------------------
@app.route("/api/bins")
def get_bins():

    connection = get_connection()

    bins = connection.execute(
        "SELECT * FROM bins"
    ).fetchall()

    connection.close()

    return jsonify([
        dict(bin)
        for bin in bins
    ])


# -------------------------
# API: Get active alerts
# -------------------------
@app.route("/api/alerts")
def get_alerts():

    connection = get_connection()

    alerts = connection.execute(
        "SELECT * FROM alerts WHERE status = 'OPEN'"
    ).fetchall()

    connection.close()

    return jsonify([
        dict(alert)
        for alert in alerts
    ])


# -------------------------
# API: Waste analysis
# -------------------------
@app.route("/api/analyze/<int:fill_level>/<int:temperature>")
def analyze(fill_level, temperature):

    condition, priority = analyze_waste(
        fill_level,
        temperature
    )

    return jsonify({
        "fill_level": fill_level,
        "temperature": temperature,
        "condition": condition,
        "priority": priority
    })


# -------------------------
# Start application
# -------------------------
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )