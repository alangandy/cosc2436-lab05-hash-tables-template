# Lab 05: Hash Tables

## Overview
In this lab, you will implement **Hash Tables** from Chapter 5 of "Grokking Algorithms." Hash tables provide O(1) average-case lookup, insertion, and deletion.

## Learning Objectives
- Understand how hash functions map keys to array indices
- Implement a hash table with chaining for collision resolution
- Use hash tables for common patterns: lookups, duplicate prevention, caching
- Understand load factor and its impact on performance

## Background

### Hash Tables
A hash table combines:
1. **Array**: For fast O(1) access by index
2. **Hash function**: Converts keys to array indices

### Collision Resolution
When two keys hash to the same index (collision), we need a strategy:
- **Chaining**: Store multiple items in a list at each index
- **Open addressing**: Find another empty slot

### Common Use Cases
- **Fast lookups**: Phone book, DNS cache
- **Preventing duplicates**: Voting systems
- **Caching**: Web page caching

---

## Complete Solutions

### Task 1: `check_voter()` - Complete Implementation

```python
def check_voter(voted: Dict[str, bool], name: str) -> bool:
    """
    Check if someone has already voted.
    
    From Chapter 5: Using hash tables to prevent duplicates.
    
    Args:
        voted: Dictionary tracking who has voted
        name: Person trying to vote
    
    Returns:
        True if they can vote, False if already voted
    """
    if name in voted:
        print("kick them out!")
        return False
    else:
        voted[name] = True
        return True
```

**How it works:**
1. Check if `name` is already a key in the `voted` dictionary
2. If yes: they already voted - print warning and return `False`
3. If no: record their vote by adding `voted[name] = True` and return `True`

---

### Task 2: `HashTable` Class - Complete Implementation

```python
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
        return hash(key) % self.size
    
    def put(self, key: str, value: Any) -> None:
        """Insert or update a key-value pair. O(1) average."""
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        
        # Check if key already exists in bucket - update if so
        for i, (existing_key, existing_value) in enumerate(bucket):
            if existing_key == key:
                bucket[i] = (key, value)  # Update existing
                return
        
        # Key doesn't exist - append new entry
        bucket.append((key, value))
        self.count += 1
    
    def get(self, key: str) -> Optional[Any]:
        """Retrieve value for a key. O(1) average."""
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        
        # Search bucket for the key
        for existing_key, value in bucket:
            if existing_key == key:
                return value
        
        # Key not found
        return None
    
    def delete(self, key: str) -> bool:
        """Remove a key-value pair. Returns True if deleted."""
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        
        # Search bucket for the key
        for i, (existing_key, value) in enumerate(bucket):
            if existing_key == key:
                bucket.pop(i)  # Remove the entry
                self.count -= 1
                return True
        
        # Key not found
        return False
    
    def load_factor(self) -> float:
        """Calculate load factor (items / buckets)."""
        return self.count / self.size
```

**How each method works:**

**`_hash(key)`:**
- Uses Python's built-in `hash()` function
- Takes modulo with `self.size` to get a valid bucket index (0 to size-1)

**`put(key, value)`:**
1. Calculate bucket index using `_hash(key)`
2. Get the bucket (a list) at that index
3. Loop through bucket to check if key already exists
4. If found: update the value at that position
5. If not found: append `(key, value)` tuple and increment `count`

**`get(key)`:**
1. Calculate bucket index using `_hash(key)`
2. Get the bucket at that index
3. Loop through bucket looking for matching key
4. If found: return the value
5. If not found: return `None`

**`delete(key)`:**
1. Calculate bucket index using `_hash(key)`
2. Get the bucket at that index
3. Loop through bucket looking for matching key
4. If found: remove with `pop(i)`, decrement `count`, return `True`
5. If not found: return `False`

---

## Example Usage

```python
# Voting example
>>> voted = {}
>>> check_voter(voted, "tom")
True
>>> check_voter(voted, "mike")
True
>>> check_voter(voted, "tom")
kick them out!
False

# Hash table example
>>> ht = HashTable()
>>> ht.put("apple", 0.67)
>>> ht.put("milk", 1.49)
>>> ht.put("bread", 2.50)

>>> ht.get("apple")
0.67

>>> ht.get("milk")
1.49

>>> ht.get("banana")  # Not in table
None

>>> ht.put("apple", 0.79)  # Update existing key
>>> ht.get("apple")
0.79

>>> ht.delete("milk")
True
>>> ht.get("milk")
None

>>> ht.delete("banana")  # Key doesn't exist
False

>>> ht.load_factor()
0.2  # 2 items / 10 buckets
```

---

## Testing
```bash
python -m pytest tests/ -v
```

## Submission
Commit and push your completed `hashtable.py` file.
