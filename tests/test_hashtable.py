"""Lab 05: Test Cases for Hash Tables"""
import pytest
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from hashtable import check_voter, HashTable


class TestCheckVoter:
    def test_first_vote(self):
        voted = {}
        assert check_voter(voted, "tom") == True
        assert "tom" in voted
    
    def test_double_vote(self):
        voted = {}
        check_voter(voted, "tom")
        assert check_voter(voted, "tom") == False
    
    def test_multiple_voters(self):
        voted = {}
        assert check_voter(voted, "tom") == True
        assert check_voter(voted, "mike") == True
        assert check_voter(voted, "tom") == False


class TestHashTable:
    def test_put_and_get(self):
        ht = HashTable()
        ht.put("apple", 1.50)
        assert ht.get("apple") == 1.50
    
    def test_get_nonexistent(self):
        ht = HashTable()
        assert ht.get("banana") is None
    
    def test_update(self):
        ht = HashTable()
        ht.put("apple", 1.50)
        ht.put("apple", 2.00)
        assert ht.get("apple") == 2.00
    
    def test_delete(self):
        ht = HashTable()
        ht.put("apple", 1.50)
        assert ht.delete("apple") == True
        assert ht.get("apple") is None
    
    def test_delete_nonexistent(self):
        ht = HashTable()
        assert ht.delete("banana") == False
    
    def test_load_factor(self):
        ht = HashTable(size=10)
        ht.put("a", 1)
        ht.put("b", 2)
        assert ht.load_factor() == 0.2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
