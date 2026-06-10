from discount import calculate_discount
def test_vip_customer():
    assert calculate_discount(60000000)==0.1
def test_normal_customer():
    assert calculate_discount(30000000)==0
    