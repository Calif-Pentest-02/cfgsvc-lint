import sqlite3, os
from flask import Flask, request, jsonify

app = Flask(__name__)
DB = os.path.join(os.path.dirname(__file__), 'data.db')

def get_db():
    return sqlite3.connect(DB)

@app.route('/api/config')
def get_config():
    key = request.args.get('key', '')
    try:
        db = get_db()
        try:
            rows = db.execute("SELECT value FROM config WHERE key LIKE ?", ('%' + key + '%',)).fetchall()
        finally:
            db.close()
    except sqlite3.Error:
        app.logger.exception("config lookup failed")
        return jsonify({"error": "internal error"}), 500
    return jsonify([r[0] for r in rows])

@app.route('/api/health')
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(debug=False, port=5000)
