import programs.count as count

def test_count():
    assert count.count([0,0,0,3],3) == 1
    assert count.count([3,3,3,3],3) == 4
    assert count.count([1,2,3,4],5) == 0
    assert count.count([4,68,72,43,43],43) == 2