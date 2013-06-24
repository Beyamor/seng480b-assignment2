class Monitor:
        def __init__(self, stock):
                self.stock = stock

        #Check the current stock value and return any changes to prices
        def monitor(self):
            #Check Managed Element
            return self.stock.checkPrice()
