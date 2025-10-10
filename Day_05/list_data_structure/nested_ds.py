s_order_data = {
    "student": {
        "s_name": "Talha Tashahud",
        "sk_id": "svs20502010",
        "course": "nextgenssc27"
    },
    "Items": [
       {"i_name":"Jersey",
        "price": 429.00,
        "i_id": "falcon1.0"
        },
       {
        "i_name": "Notebook",
        "price": 260.00,
        "i_id": "Notebook.1"
        }
    ]
}
c_details = f" Student Name: {s_order_data['student']['s_name']}, Student ID: {s_order_data['student']['sk_id']}, Course: {s_order_data['student']['course']}"
print("Customer Details:", c_details)

#using comprehension method
Total_cost = sum(product["price"] for product in s_order_data["Items"])
print("The total price is :",Total_cost)

#Using linear for loop
#total_cost = 0
#for product in s_order_data["Items"]:
    #total_cost += product["price"]

   # print("The total price is :",total_cost)