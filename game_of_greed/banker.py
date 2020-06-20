# Handle banking points
# Define a Banker class
class Banker:

    def __init__(self):
        self.shelf_points = 0
        self.bank_points = 0

    def shelf(self, points):
        self.shelf_points += points

    def bank(self):
        to_be_banked = self.shelf_points
        self.bank_points += self.shelf_points
        self.clear_shelf()
        return to_be_banked

    def clear_shelf(self):
        self.shelf_points = 0


# Add a shelf instance method
# Input to shelf is the amount of points (integer) to add to shelf.
# shelf should temporarily store unbanked points.

# Add a bank instance method
# bank should add any points on the shelf to total and reset shelf to 0.
# bank output should be the amount of points added to total from shelf.

# Add a clear_shelf instance method
# clear_shelf should remove all unbanked points.
