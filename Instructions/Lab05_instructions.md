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

## Your Tasks

### Task 1: Implement `check_voter()`
Implement the voting example from Chapter 5:
- If person already voted, print "kick them out!" and return `False`
- Otherwise, record their vote and return `True`

### Task 2: Implement `HashTable` class
Complete the hash table implementation:

**`_hash(key)`**: Return `hash(key) % self.size`

**`put(key, value)`**:
- Get bucket index using `_hash()`
- If key exists in bucket, update its value
- Otherwise, append `(key, value)` to bucket
- Update `self.count`

**`get(key)`**:
- Get bucket index
- Search bucket for key
- Return value if found, `None` otherwise

**`delete(key)`**:
- Remove key-value pair from bucket
- Update `self.count`
- Return `True` if deleted, `False` if not found

## Example

```python
>>> voted = {}
>>> check_voter(voted, "tom")
True
>>> check_voter(voted, "tom")
kick them out!
False

>>> ht = HashTable()
>>> ht.put("apple", 0.67)
>>> ht.put("milk", 1.49)
>>> ht.get("apple")
0.67
>>> ht.get("banana")
None
```

## Testing
```bash
python -m pytest tests/ -v
```

## Hints
- Python's built-in `hash()` function works on strings
- Each bucket is a list of `(key, value)` tuples
- When searching a bucket, iterate through and compare keys
- Don't forget to increment/decrement `self.count`!

## Load Factor
```python
load_factor = items / buckets
```
- Low load factor (< 0.7): Good performance
- High load factor: More collisions, slower operations
- Solution: Resize the hash table when load factor gets too high

## Submission
Commit and push your completed `hashtable.py` file.
