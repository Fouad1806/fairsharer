from fairsharer import fair_sharer

def test_fair_sharer():
    assert fair_sharer([0, 1000, 800, 0], 1) == [100, 800, 900, 0]
    assert fair_sharer([0, 1000, 800, 0], 2) == [100, 890, 720, 90]
    assert fair_sharer([700, 1000, 800, 0], 1) == [800, 890, 720, 90]
    
