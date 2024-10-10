from scipy.optimize import fsolve

# Hàm tính giá trái phiếu dựa trên YTM và các thông số
def calculate_bond_price(coupon_rate, future_value, years_to_maturity, ytm, payments_per_year):
    coupon_payment = 1000 * coupon_rate / payments_per_year
    total_payments = int(years_to_maturity * payments_per_year)  # Đảm bảo total_payments là số nguyên
    semi_ytm = ytm / payments_per_year
    
    bond_price = sum([coupon_payment / (1 + semi_ytm) ** t for t in range(1, total_payments + 1)]) + \
                 future_value / (1 + semi_ytm) ** total_payments
    
    return bond_price

# Hàm tính YTM (Yield to Maturity)
def calculate_ytm(coupon_rate, future_value, market_price, years_to_maturity, payments_per_year):
    coupon_payment = 1000 * coupon_rate / payments_per_year
    total_payments = int(years_to_maturity * payments_per_year)  # Đảm bảo total_payments là số nguyên

    # Phương trình để giải YTM dựa trên giá thị trường
    def bond_price_equation(ytm):
        semi_ytm = ytm / payments_per_year
        price = sum([coupon_payment / (1 + semi_ytm) ** t for t in range(1, total_payments + 1)]) + \
                future_value / (1 + semi_ytm) ** total_payments
        return price - market_price  # So sánh giá tính với giá thị trường hiện tại

    ytm_solution = fsolve(bond_price_equation, 0.05) [0]   # Guess bắt đầu tại 5%
    return ytm_solution

# Hàm tính EAY (Effective Annual Yield)
def calculate_eay(ytm, payments_per_year):
    eay = (1 + ytm / payments_per_year) ** payments_per_year - 1
    return eay

# Hàm  cho phép người dùng nhập số liệu tính YTM và EAY
def YTM():
    # Nhập thông tin từ người dùng
    coupon_rate = float(input("Nhập Coupon Rate (%): ")) / 100  # Tỷ lệ coupon hàng năm
    face_value = float(input("Nhập FutureValue: "))  # Mệnh giá trái phiếu
    market_price = float(input("Nhập Bond Price: "))  # Giá thị trường hiện tại
    years_to_maturity = float(input("Nhập số năm còn lại đến đáo hạn: "))  # Số năm còn lại
    payments_per_year = int(input("Nhập số lần thanh toán mỗi năm (thường là 2 - bán niên): "))  # Số lần thanh toán mỗi năm

    # Tính YTM
    ytm = calculate_ytm(coupon_rate, face_value, market_price, years_to_maturity, payments_per_year)
    print(f"\nYield to Maturity (YTM): {ytm:.4%}")

    # Tính EAY từ YTM
    eay = calculate_eay(ytm, payments_per_year)
    print(f"Effective Annual Yield (EAY): {eay:.4%}")

    # Tính giá hiện tại của trái phiếu từ YTM (kiểm tra lại)
    bond_price = calculate_bond_price(coupon_rate, face_value, years_to_maturity, ytm, payments_per_year)
    print(f"Bond Price (from YTM): {bond_price:.2f} (so với giá thị trường nhập: {market_price:.2f})")

# Hàm cho phép người dùng nhập dữ liệu để tính BondPrice
def BondPrice():
    coupon_rate = float(input("Nhập Coupon Rate (%): ")) / 100  # Tỷ lệ coupon hàng năm
    face_value = float(input("Nhập FutureValue: "))  # Mệnh giá trái phiếu
    interest_rate = float(input("Nhập Interest Rate (%): ")) / 100 
    years_to_maturity = float(input("Nhập số năm còn lại đến đáo hạn: "))  # Số năm còn lại
    payments_per_year = int(input("Nhập số lần thanh toán mỗi năm: "))  # Số lần thanh toán mỗi năm

    # Tính Market Price của Bond
    bond_price = calculate_bond_price(coupon_rate, face_value, years_to_maturity, interest_rate, payments_per_year)
    print(f"Bond Price (from Interest Rate): {bond_price:.2f} ")

if __name__ == "__main__":
    while True:
        n = int(input("\nYTM hay PRICE > "))
        if n == 1:
            YTM()
        elif n == 2:
            BondPrice()
        if n == 3:
            break