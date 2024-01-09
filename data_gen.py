import json
import random
from datetime import datetime, timedelta
ORDER_ID_OFFSET=280000;
def generate_data():
    data = []
    for order_id in range(0, 500):
        order_date = datetime(2023, 1, 1) + timedelta(days=random.randint(1, 365))
        order_date_microseconds = int(order_date.timestamp() * 1e6)
        order_amount = round(random.uniform(1000, 4000), 2)
        transaction_fees = 22.0

        order_data = {
            "order_id": ORDER_ID_OFFSET+order_id,
            "order_date": order_date_microseconds,
            "order_amount": order_amount,
            "transactions_fees": transaction_fees
        }
        data.append(order_data)
    return data

def export_to_json(data):
    with open("public/orders_data.json", "w") as json_file:
        json.dump(data, json_file, indent=2)
    print("JSON data exported to 'orders_data.json'")

if __name__ == "__main__":
    orders_data = generate_data()
    export_to_json(orders_data)
