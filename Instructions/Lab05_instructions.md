# Lab 5: Hash Tables

## 1. Introduction and Objectives

### Overview
Implement a hash table from scratch to understand hash functions, collision handling, and O(1) average lookup time.

### Learning Objectives
- Understand how hash functions work
- Implement a hash table with collision handling
- Use Python dictionaries effectively
- Analyze hash table performance

### Prerequisites
- Complete Labs 1-4
- Read Chapter 5 in "Grokking Algorithms" (pages 77-100)

---

## 2. Algorithm Background

### Hash Function Requirements
1. Consistent: same input → same output
2. Maps different inputs to different outputs (ideally)
3. Returns valid array indices

### Collision Handling
When two keys hash to the same index:
- **Chaining**: Store linked list at each slot
- **Open Addressing**: Find next empty slot

### Time Complexity
| Operation | Average | Worst (all collisions) |
|-----------|---------|------------------------|
| Insert | O(1) | O(n) |
| Lookup | O(1) | O(n) |
| Delete | O(1) | O(n) |

---

## 3. Project Structure

```
lab05_hash_tables/
├── hashtable.py   # Custom hash table implementation
├── main.py        # Main program
└── README.md      # Your lab report
```

---

## 4. Step-by-Step Implementation

### Step 1: Create `hashtable.py`

```python
"""
Lab 5: Hash Table Implementation
Custom hash table with chaining for collision resolution.

From Chapter 5: Hash tables are used for:
1. Lookups - O(1) average
2. Preventing duplicates (like voting)
3. Caching
"""
from typing import Any, List, Optional, Tuple


# ============================================
# VOTING EXAMPLE FROM CHAPTER 5
# ============================================
def check_voter(voted: dict, name: str) -> bool:
    """
    Check if someone has already voted.
    
    From Chapter 5: Using hash tables to prevent duplicates.
    
    voted = {}
    if name in voted:
        print("kick them out!")
    else:
        voted[name] = True
    """
    if name in voted:
        print(f"{name} has already voted - kick them out!")
        return False
    else:
        voted[name] = True
        print(f"{name} can vote")
        return True


class HashTable:
    """
    Hash table implementation using chaining.
    
    Each bucket contains a list of (key, value) tuples
    to handle collisions.
    """
    
    def __init__(self, size: int = 10):
        """Initialize hash table with given number of buckets."""
        self.size = size
        self.buckets: List[List[Tuple[Any, Any]]] = [[] for _ in range(size)]
        self.count = 0
    
    def _hash(self, key: str) -> int:
        """
        Simple hash function for strings.
        Converts key to an array index.
        
        This uses Python's built-in hash(), but you could also:
        - Sum ASCII values: sum(ord(c) for c in key) % size
        - Use polynomial rolling hash
        - Use more sophisticated algorithms (SHA, MD5)
        """
        return hash(key) % self.size
    
    def put(self, key: str, value: Any) -> None:
        """
        Insert or update a key-value pair.
        Time Complexity: O(1) average, O(n) worst case
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        
        # Check if key already exists (update)
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                print(f"Updated '{key}' at bucket {index}")
                return
        
        # Key doesn't exist (insert)
        bucket.append((key, value))
        self.count += 1
        print(f"Inserted '{key}' at bucket {index} (chain length: {len(bucket)})")
    
    def get(self, key: str) -> Optional[Any]:
        """
        Retrieve value for a key.
        Time Complexity: O(1) average, O(n) worst case
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for k, v in bucket:
            if k == key:
                print(f"Found '{key}' at bucket {index}")
                return v
        
        print(f"'{key}' not found (checked bucket {index})")
        return None
    
    def delete(self, key: str) -> bool:
        """
        Remove a key-value pair.
        Time Complexity: O(1) average, O(n) worst case
        """
        index = self._hash(key)
        bucket = self.buckets[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                print(f"Deleted '{key}' from bucket {index}")
                return True
        
        print(f"Cannot delete '{key}' - not found")
        return False
    
    def contains(self, key: str) -> bool:
        """Check if key exists."""
        return self.get(key) is not None
    
    def load_factor(self) -> float:
        """
        Calculate load factor (items / buckets).
        
        Good hash tables keep load factor < 0.7
        Higher load factor = more collisions = slower
        """
        return self.count / self.size
    
    def display(self) -> None:
        """Display the hash table structure."""
        print(f"\nHash Table (size={self.size}, items={self.count}, "
              f"load={self.load_factor():.2f}):")
        print("-" * 40)
        for i, bucket in enumerate(self.buckets):
            if bucket:
                items = ", ".join(f"{k}: {v}" for k, v in bucket)
                print(f"Bucket {i}: [{items}]")
            else:
                print(f"Bucket {i}: [empty]")


class CityCache:
    """
    Practical example: Cache for city lookups.
    Demonstrates hash table use case.
    """
    
    def __init__(self):
        self.cache = {}  # Python dict IS a hash table!
        self.hits = 0
        self.misses = 0
    
    def lookup(self, city_name: str, cities_list: list) -> Optional[dict]:
        """
        Look up city, using cache for O(1) repeat lookups.
        """
        # Check cache first (O(1))
        if city_name in self.cache:
            self.hits += 1
            print(f"Cache HIT for '{city_name}'")
            return self.cache[city_name]
        
        # Cache miss - search list (O(n))
        self.misses += 1
        print(f"Cache MISS for '{city_name}' - searching list...")
        
        for city in cities_list:
            if city['name'].lower() == city_name.lower():
                # Add to cache for future lookups
                self.cache[city_name] = city
                return city
        
        return None
    
    def stats(self) -> str:
        total = self.hits + self.misses
        hit_rate = (self.hits / total * 100) if total > 0 else 0
        return f"Cache stats: {self.hits} hits, {self.misses} misses ({hit_rate:.1f}% hit rate)"
```

### Step 2: Create `main.py`

```python
"""
Lab 5: Main Program
Demonstrates hash table concepts.
"""
import json
from hashtable import HashTable, CityCache


def load_cities(filename: str) -> list:
    with open(filename, 'r') as file:
        return json.load(file)


def main():
    # =========================================
    # PART 1: Voting Example (from Chapter 5)
    # =========================================
    print("=" * 60)
    print("PART 1: PREVENTING DUPLICATES - VOTING (Chapter 5)")
    print("=" * 60)
    
    from hashtable import check_voter
    
    voted = {}  # Hash table to track who voted
    
    print("\nVoting simulation:")
    check_voter(voted, "tom")
    check_voter(voted, "mike")
    check_voter(voted, "tom")  # Already voted!
    check_voter(voted, "sarah")
    check_voter(voted, "mike")  # Already voted!
    
    print(f"\nVoted so far: {list(voted.keys())}")
    
    # =========================================
    # PART 2: Custom Hash Table
    # =========================================
    print("\n" + "=" * 60)
    print("PART 2: CUSTOM HASH TABLE")
    print("=" * 60)
    
    ht = HashTable(size=5)  # Small size to show collisions
    
    # Insert city populations
    cities_data = [
        ("Houston", 2304580),
        ("Dallas", 1304379),
        ("Austin", 978908),
        ("San Antonio", 1547253),
        ("Fort Worth", 909585),
        ("El Paso", 681728),
    ]
    
    print("\nInserting cities:")
    for city, pop in cities_data:
        ht.put(city, pop)
    
    ht.display()
    
    # Lookup
    print("\n--- Lookups ---")
    print(f"Houston population: {ht.get('Houston'):,}")
    print(f"Austin population: {ht.get('Austin'):,}")
    ht.get("Chicago")  # Not in table
    
    # Delete
    print("\n--- Delete ---")
    ht.delete("Dallas")
    ht.display()
    
    # =========================================
    # PART 2: Python Dictionaries
    # =========================================
    print("\n" + "=" * 60)
    print("PART 2: PYTHON DICTIONARIES (BUILT-IN HASH TABLES)")
    print("=" * 60)
    
    # Python dicts ARE hash tables!
    phone_book = {
        "Alice": "555-1234",
        "Bob": "555-5678",
        "Charlie": "555-9012"
    }
    
    print("\nPhone book operations (all O(1) average):")
    print(f"Alice's number: {phone_book.get('Alice')}")
    print(f"'Bob' in phone_book: {'Bob' in phone_book}")
    
    phone_book["Diana"] = "555-3456"
    print(f"Added Diana: {phone_book}")
    
    # =========================================
    # PART 3: Caching Example
    # =========================================
    print("\n" + "=" * 60)
    print("PART 3: CACHING WITH HASH TABLES")
    print("=" * 60)
    
    cities = load_cities('../data/cities.json')
    cache = CityCache()
    
    # First lookups (cache misses)
    print("\nFirst round of lookups:")
    cache.lookup("Houston", cities)
    cache.lookup("Dallas", cities)
    cache.lookup("Austin", cities)
    
    # Repeat lookups (cache hits!)
    print("\nRepeat lookups (should be faster):")
    cache.lookup("Houston", cities)
    cache.lookup("Dallas", cities)
    cache.lookup("Houston", cities)
    
    print(f"\n{cache.stats()}")
    
    # =========================================
    # PART 4: Hash Table Use Cases
    # =========================================
    print("\n" + "=" * 60)
    print("PART 4: COMMON USE CASES")
    print("=" * 60)
    print("""
    Hash tables are used for:
    
    1. LOOKUPS - O(1) by key
       - Phone books, dictionaries
       - Database indexes
       - Symbol tables in compilers
    
    2. DUPLICATE DETECTION
       voted = {}
       if person in voted:
           print("Already voted!")
       voted[person] = True
    
    3. CACHING
       - Store expensive computations
       - Web page caching
       - Memoization (Lab 11!)
    
    4. COUNTING FREQUENCIES
       word_count = {}
       for word in text:
           word_count[word] = word_count.get(word, 0) + 1
    """)


if __name__ == "__main__":
    main()
```

---

## 5. Lab Report Template

```markdown
# Lab 5: Hash Tables

## Student Information
- **Name:** [Your Name]  
- **Date:** [Date]

## Hash Table Concepts

### How Hash Functions Work
[Explain in your own words]

### Collision Handling
[Explain chaining vs open addressing]

### Load Factor
[What is it and why does it matter?]

## Performance Analysis

| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| Insert | O(1) | O(n) |
| Lookup | O(1) | O(n) |
| Delete | O(1) | O(n) |

## Reflection Questions

1. Why is the average case O(1) but worst case O(n)?

2. What makes a good hash function?

3. Give 3 real-world examples where you'd use a hash table.
```

---

## 6. Submission
Save files in `lab05_hash_tables/`, complete README, commit and push.
