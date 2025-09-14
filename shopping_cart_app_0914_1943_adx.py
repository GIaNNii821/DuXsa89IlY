# 代码生成时间: 2025-09-14 19:43:57
from bottle import route, run, request, response, template

# 假设商品数据存储在内存中，实际应用中可以替换为数据库
products = {
    '1': {'name': 'Apple', 'price': 10},
    '2': {'name': 'Banana', 'price': 5},
    '3': {'name': 'Cherry', 'price': 15}
}

# 购物车存储
cart = {}

# 获取所有商品
@route('/products')
def get_products():
    return products

# 获取购物车
@route('/cart')
def get_cart():
    if not cart:
        return {'error': 'Cart is empty'}
    return cart

# 添加商品到购物车
@route('/cart/add/<product_id>')
def add_to_cart(product_id):
    if product_id not in products:
        return {'error': 'Product not found'}
    if product_id not in cart:
        cart[product_id] = {'quantity': 0}
    cart[product_id]['quantity'] += 1
    return {'message': f'Added {products[product_id]['name']} to cart'}

# 从购物车移除商品
@route('/cart/remove/<product_id>')
def remove_from_cart(product_id):
    if product_id not in cart:
        return {'error': 'Product not found in cart'}
    if cart[product_id]['quantity'] > 1:
        cart[product_id]['quantity'] -= 1
    else:
        del cart[product_id]
    return {'message': f'Removed {products[product_id]['name']} from cart'}

# 运行应用
if __name__ == '__main__':
    run(host='localhost', port=8080)
