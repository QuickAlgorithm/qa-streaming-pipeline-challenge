from flask import Flask, request, jsonify, render_template
import sqlite3 as sqlite
import sys
import os
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return """<h1>Streaming API</h1>
    """

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/api/v1/data', methods=['GET'])
def api_filter():
    query_parameters = request.args

    page = int(query_parameters.get('page'))

    query = build_query(page)
    conn = sqlite.connect('../data/main.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    results = cur.execute(query).fetchall()
    return jsonify(results)

def build_query(page):
    n_per_page = 10
    offset = page * n_per_page
    # Possibly vulnerable to SQL injection.
    query = "SELECT * FROM data LIMIT 10 OFFSET " + str(offset)
 
    return query 


if __name__ == '__main__':
    if os.environ.get('PORT') is not None:
        app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT'))
    else:
        app.run(debug=True, host='0.0.0.0')

