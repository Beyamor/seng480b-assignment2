class Analyzer:
        def __init__(self, knowledge_base):
                self.knowledge_base = knowledge_base

        #Use monitor return and check against knowledge base
        def analyze(self, currentStockPrice):
            #Use monitor return and check against knowledge base
            stock_difference = currentStockPrice - self.knowledge_base.lastPrice
            self.knowledge_base.doAnalyze(currentStockPrice)

            direction = None
            if stock_difference > 0:
                    direction = "rising"
            elif stock_difference < 0:
                    direction = "falling"
            else:
                    direction = "holding"

            return {"direction": direction, "magnitude": abs(stock_difference)}
