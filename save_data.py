import csv

from app import db
from app.module.models import Metal_schingle

def base():
    with open('base.csv', 'r', encoding='Windows 1251') as f:
        names = ['name', 'size_metal', 'price', 'description', 'unique_number']
        products = {}
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            esc = dict(zip(names, row))
            #print(esc)
            #save_products(name, size_metal, price, description, unique_number)
            for row in esc:
                name = esc['name']
                size_metal = esc['size_metal']
                price = esc['price']
                description = esc['description']
                unique_number = esc['unique_number']
                save_products(name, size_metal, price, description, unique_number)
            #print(esc)





def save_products(name, size_metal, price, description, unique_number):
    product_exists = Metal_schingle.query.filter(Metal_schingle.unique_number == unique_number).count()
    #print(product_exists)
    if not product_exists:
        products_temp = Metal_schingle(name=name, size_metal=size_metal, price=price, description=description, unique_number=unique_number)
        db.session.add(products_temp)
        db.session.commit()


base()