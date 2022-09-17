from flask import Flask, render_template, abort
import sqlite3

app = Flask(__name__)


def get_connection():
    conn = sqlite3.connect('example.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/best_selling')
def best_selling_products():
    conn = get_connection()
    temp_list = conn.execute("select * from tracks").fetchall()
    conn.close()
    return render_template('all_tracks.html', temps=temp_list)


@app.route('/best_selling/<int:temp_id>')
def id_temp(temp_id):
    conn = get_connection()
    best_sellers = conn.execute('select invoice_items.TrackId, tracks.Name, '
                                'SUM(invoice_items.UnitPrice * invoice_items.Quantity) '
                                'as best_seller from invoice_items join tracks on invoice_items.TrackId=tracks.TrackId '
                                'group by invoice_items.TrackId  ORDER by SUM(invoice_items.UnitPrice * '
                                'invoice_items.Quantity) '
                                'desc limit ?', (temp_id,)).fetchall()
    conn.close()
    if best_sellers is None:
        abort(404)
    return render_template('detail.html', best_sellers=best_sellers)


app.run(debug=True)
