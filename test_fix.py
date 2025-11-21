from javsp.file import _normalize_duplicate_avid

def test_normalize():
    # Test single suffix
    assert _normalize_duplicate_avid('ABC-123-C') == 'ABC-123'
    assert _normalize_duplicate_avid('ABC-123-UC') == 'ABC-123'
    
    # Test multiple suffixes
    assert _normalize_duplicate_avid('ABC-123-C-UC') == 'ABC-123'
    assert _normalize_duplicate_avid('ABC-123-UC-C') == 'ABC-123'
    
    # Test recursive/repeated suffixes
    assert _normalize_duplicate_avid('ABC-123-C-C') == 'ABC-123'
    assert _normalize_duplicate_avid('ABC-123-UC-UC') == 'ABC-123'
    
    # Test no suffix
    assert _normalize_duplicate_avid('ABC-123') == 'ABC-123'
    
    # Test None
    assert _normalize_duplicate_avid(None) is None

    print("All tests passed!")

if __name__ == "__main__":
    test_normalize()
