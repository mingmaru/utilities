from models import Asset, Stock, Commodity, Portfolio

my_portfolio = Portfolio()

# --- KB (국민은행) ---
my_portfolio.add_asset(Asset("KB나라사랑우대통장", "국민", "942902-00-607835", 2000000, "예금"))
my_portfolio.add_asset(Asset("KB종합통장-저축예금", "국민", "284802-04-076162", 5000000, "예금"))
my_portfolio.add_asset(Asset("KB스타적금III", "국민", "284803-04-158197", 3000000, "적금"))

# --- Shinhan (신한은행) ---
my_portfolio.add_asset(Asset("키즈앤틴즈 통장", "신한", "110-319-919579", 1000000, "입출금"))
my_portfolio.add_asset(Asset("마이홈플랜 주택청약 종합저축", "신한", "223-045-576960",4000000, "예적금"))
# For '리슈' accounts, you can input current weight and market price
my_portfolio.add_asset(Commodity("신한실버리슈실버테크", "신한", "189-000-248436", 221.26, 76.9, "Silver"))
my_portfolio.add_asset(Commodity("신한골드리슈골드테크", "신한", "187-002-098490", 10, 110000, "Gold"))

# --- 주식 ---
# 한국투자증권
my_portfolio.add_asset(Stock("Samsung Electronics", "한투", "63065397-01","005930", 20, 75000))
my_portfolio.add_asset(Stock("Samsung Electronics", "한투", "63065397-01","005930", 20, 75000))
my_portfolio.add_asset(Stock("Samsung Electronics", "한투", "63065397-01","005930", 20, 75000))
my_portfolio.add_asset(Stock("Samsung Electronics", "한투", "63065397-01","005930", 20, 75000))

# 미래에셋증권
my_portfolio.add_asset(Stock("Samsung Electronics", "미래", "63065397-01","005930", 20, 75000))


# --- Output ---
my_portfolio.summary_by_bank()
print(f"\n총계: {my_portfolio.total_value():,} KRW")