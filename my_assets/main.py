from models import Asset, Stock, Commodity, Portfolio

my_portfolio = Portfolio()

# --- KB (국민은행) ---
my_portfolio.add_asset(Asset("KB나라사랑우대통장", "국민", 2000000, "Savings"))
my_portfolio.add_asset(Asset("KB종합통장-저축예금", "국민", 5000000, "Savings"))
my_portfolio.add_asset(Asset("KB스타적금III", "국민", 3000000, "Installment"))

# --- Shinhan (신한은행) ---
my_portfolio.add_asset(Asset("키즈앤틴즈통장", "신한", 1000000, "Savings"))
my_portfolio.add_asset(Asset("마이홈플랜주택청약", "신한", 4000000, "Housing"))
# For '리슈' accounts, you can input current weight and market price
my_portfolio.add_asset(Commodity("신한실버리슈", "신한", 100, 1200, "Silver"))
my_portfolio.add_asset(Commodity("신한골드리슈", "신한", 10, 110000, "Gold"))

# --- Stocks ---
my_portfolio.add_asset(Stock("Samsung Electronics", "한투", "005930", 20, 75000))

# --- Output ---
my_portfolio.summary_by_bank()
print(f"\nTotal Overall Assets: {my_portfolio.total_value():,} KRW")