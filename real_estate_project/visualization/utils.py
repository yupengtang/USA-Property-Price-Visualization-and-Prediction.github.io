# visualization/utils.py

import csv
import os
from django.conf import settings

def load_house_data():
    data_file = os.path.join(settings.BASE_DIR, 'data', 'realtor_data.csv')
    houses = []
    with open(data_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            houses.append({
                'bed': int(row['bed']),
                'bath': int(row['bath']),
                'price': float(row['price']),
               
            })
    return houses

def predict_price(bed, bath):
    houses = load_house_data()

    total = 0
    count = 0
    for house in houses:
        if house['bed'] == bed and house['bath'] == bath:
            total += house['price']
            count += 1
    if count == 0:
        return "No data available for the given bed and bath count."
    average_price = total / count
    return f"The average price for {bed} beds and {bath} baths is ${average_price:,.2f}."
