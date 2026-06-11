from discount import calculate_discount

def test_tc01():
    # TC01: Tổng mua trước: 60M, Đơn hàng mới: 2M -> Tổng: 62M >= 50M
    # Kết quả mong đợi (Expected Result): Có chiết khấu 10% (0.1)
    assert calculate_discount(60000000) == 0.1

def test_tc02():
    # TC02: Tổng mua trước: 30M, Đơn hàng mới: 2M -> Tổng: 32M < 50M
    # Kết quả mong đợi (Expected Result): Không chiết khấu (0)
    assert calculate_discount(30000000) == 0

def test_tc03():
    # TC03: Tổng mua trước: 49M, Đơn hàng mới: 2M -> Tổng: 51M >= 50M
    # Kết quả mong đợi từ yêu cầu nghiệp vụ (Expected Result): Có chiết khấu 10% (0.1)
    assert calculate_discount(49000000) == 0.1