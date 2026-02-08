from collections import defaultdict


class Asset:
    def __init__(self, name, bank, account_num, amount_krw, category="General"):
        self.name = name
        self.bank = bank
        self.account_num = account_num
        self.amount = amount_krw
        self.category = category # e.g., "Savings", "Installment", "Housing"

class Stock(Asset):
    def __init__(self, name, broker, account_num, ticker, quantity, price_per_share):
        super().__init__(name, broker, account_num, quantity * price_per_share, category="Stock")
        self.ticker = ticker
        self.quantity = quantity

class Commodity(Asset):
    def __init__(self, name, bank, account_num, weight_g, price_per_g, category="Precious Metal"):
        # For '리슈' products, the bank acts as the location
        super().__init__(name, bank, account_num, weight_g * price_per_g, category=category)
        self.weight = weight_g

class Portfolio:
    def __init__(self):
        self.assets = []

    def add_asset(self, asset):
        self.assets.append(asset)

    def total_value(self):
        return sum(a.amount for a in self.assets)

    def summary_by_bank(self):
        bank_map = defaultdict(list)
        for asset in self.assets:
            bank_map[asset.bank].append(asset)
            
        print("\n=== Summary by Bank ===")
        for bank, assets in bank_map.items():
            bank_total = sum(a.amount for a in assets)
            print(f"[{bank}] Total: {bank_total:,} KRW")
            for a in assets:
                print(f"  - {a.category:15} | {a.name:20} ({a.account_num:15}): {a.amount:>12,} KRW")