import random
import json

class InventoryAllocator:
    def __init__(self):
        self.inventory = {"A": 150, "B": 150, "C": 100, "D": 100, "E": 200}
        self.orders = []

    def generate_order(self, header):
        lines = []
        for product in ["A", "B", "C", "D", "E"]:
            quantity = random.randint(0, 5)
            if quantity > 0:
                lines.append({"Product": product, "Quantity": quantity})
        if not lines:
            return None  # Invalid order
        return {"Header": header, "Lines": lines}

    def process_order(self, order):
        allocation = {"Header": order["Header"], "Lines": []}
        for line in order["Lines"]:
            product = line["Product"]
            requested = line["Quantity"]
            available = self.inventory.get(product, 0)
            allocated = min(requested, available)
            backordered = requested - allocated
            self.inventory[product] -= allocated
            allocation["Lines"].append({
                "Product": product,
                "Requested": requested,
                "Allocated": allocated,
                "Backordered": backordered
            })
        self.orders.append(allocation)

    def run(self, num_orders=100):
        header = 1
        while any(self.inventory.values()) and header <= num_orders:
            order = self.generate_order(header)
            if order:
                self.process_order(order)
                header += 1

    def print_summary(self):
        for order in self.orders:
            print(f"Order {order['Header']}:")
            for line in order["Lines"]:
                print(f"  {line['Product']}: Requested={line['Requested']}, Allocated={line['Allocated']}, Backordered={line['Backordered']}")
        print("Final Inventory:", self.inventory)


# Run the inventory allocator
allocator = InventoryAllocator()
allocator.run()
allocator.print_summary()
