"""
Lab 05: Hash Tables
Implement hash table concepts from Chapter 5.

Hash tables are used for:
1. Lookups - O(1) average
2. Preventing duplicates (voting example)
3. Caching
"""
from typing import Any, Optional, Dict


def check_voter(voted: Dict[str, bool], name: str) -> bool:
    """
    Check if someone has already voted.
    
    From Chapter 5: Using hash tables to prevent duplicates.
    
    Args:
        voted: Dictionary tracking who has voted
        name: Person trying to vote
    
    Returns:
        True if they can vote, False if already voted
    
    Example:
        >>> voted = {}
        >>> check_voter(voted, "tom")
        True
        >>> check_voter(voted, "tom")
        False
    """
    # TODO: Implement check_voter
    # 1. If name in voted, print "kick them out!" and return False
    # 2. Otherwise, add name to voted and return True
    pass


class HashTable:
    """
    Simple hash table implementation.
    
    Uses chaining for collision resolution.
    """
    
    def __init__(self, size: int = 10):
        self.size = size
        self.buckets = [[] for _ in range(size)]
        self.count = 0
    
    def _hash(self, key: str) -> int:
        """Hash function: convert key to array index."""
        # TODO: Return hash(key) % self.size
        pass
    
    def put(self, key: str, value: Any) -> None:
        """Insert or update a key-value pair. O(1) average."""
        # TODO: Implement put
        # 1. Get bucket index using _hash
        # 2. Check if key exists in bucket (update if so)
        # 3. Otherwise append (key, value) to bucket
        pass
    
    def get(self, key: str) -> Optional[Any]:
        """Retrieve value for a key. O(1) average."""
        # TODO: Implement get
        # 1. Get bucket index
        # 2. Search bucket for key
        # 3. Return value if found, None otherwise
        pass
    
    def delete(self, key: str) -> bool:
        """Remove a key-value pair. Returns True if deleted."""
        # TODO: Implement delete
        pass
    
    def load_factor(self) -> float:
        """Calculate load factor (items / buckets)."""
        return self.count / self.size
