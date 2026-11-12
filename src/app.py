from flask import Flask, render_template, request, redirect, url_for
from database import get_db_connection, init_db

app = Flask(__name__)

init_db()

@app.route('/')
def index():
    search = request.args.get('search', '').strip()
    category = request.args.get('category', '').strip()

    conn = get_db_connection()

    query = 'SELECT * FROM inventory WHERE 1=1'
    params = []
    if search:
        query += ' AND (name LIKE ? OR sku LIKE ?)'
        params.extend([f'%{search}%', f'%{search}%'])
    if category:
        query += ' AND category = ?'
        params.append(category)
    
    query += ' ORDER BY id DESC'
    items = conn.execute(query, params).fetchall()

    cat_rows = conn.execute('SELECT DISTINCT category FROM inventory WHERE category IS NOT NULL AND category != ""').fetchall()
    categories = [r['category'] for r in cat_rows]

    all_items = conn.execute('SELECT quantity, price FROM inventory').fetchall()
    total_items = len(all_items)
    total_units = sum(item['quantity'] for item in all_items)
    total_value = sum(item['quantity'] * item['price'] for item in all_items)
    low_stock_count = sum(1 for item in all_items if item['quantity'] < 5)

    conn.close()

    return render_template(
        'index.html',
        items=items,
        categories=categories,
        search_query=search,
        selected_category=category,
        total_items=total_items,
        total_units=total_units,
        total_value=total_value,
        low_stock_count=low_stock_count
    )

@app.route('/add', methods=['POST'])
def add_item():
    name = request.form['name']
    sku = request.form['sku']
    category = request.form['category']
    quantity = int(request.form['quantity'])
    price = float(request.form['price'])

    conn = get_db_connection()
    try:
        conn.execute('INSERT INTO inventory (name, sku, category, quantity, price) VALUES (?, ?, ?, ?, ?)',
                     (name, sku, category, quantity, price))
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update_item(id):
    name = request.form['name']
    category = request.form['category']
    quantity = int(request.form['quantity'])
    price = float(request.form['price'])

    conn = get_db_connection()
    conn.execute('UPDATE inventory SET name = ?, category = ?, quantity = ?, price = ? WHERE id = ?',
                 (name, category, quantity, price, id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_item(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM inventory WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
