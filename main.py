#!/usr/bin/env python3
"""
Lab 05: Hash Tables - Interactive Tutorial
===========================================

🎯 GOAL: Implement hash table functions in hashtable.py

📚 HASH TABLES (Chapter 5):
---------------------------
Hash tables are THE most important data structure for fast lookups!

- Also called: dictionaries (Python), maps (C++/Java), objects (JavaScript)
- Average case: O(1) for insert, lookup, delete
- Used everywhere: databases, caches, duplicate detection

HOW THEY WORK:
1. Hash function converts key → array index
2. Store value at that index
3. Handle collisions (when two keys hash to same index)

HOW TO RUN:
-----------
    python main.py           # Run this tutorial
    python -m pytest tests/ -v   # Run the grading tests
"""

from hashtable import check_voter, HashTable


def print_header(title: str) -> None:
    """Print a formatted section header."""
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


def python_dict_intro() -> None:
    """Introduce Python's built-in dictionary."""
    print_header("PYTHON DICTIONARIES (Built-in Hash Tables)")
    
    print("""
    Python has hash tables built in - they're called dictionaries!
    
    C++:   std::map<string, int> or std::unordered_map<string, int>
    Java:  HashMap<String, Integer>
    Python: dict (or just {})
    
    CREATING A DICTIONARY:
    ----------------------
    # Empty dictionary
    phone_book = {}
    
    # With initial values
    phone_book = {
        "jenny": "867-5309",
        "emergency": "911"
    }
    
    OPERATIONS:
    -----------
    # Add/Update - O(1) average
    phone_book["alice"] = "555-1234"
    
    # Lookup - O(1) average
    number = phone_book["jenny"]  # "867-5309"
    
    # Check if key exists
    if "bob" in phone_book:
        print("Found Bob!")
    
    # Delete - O(1) average
    del phone_book["jenny"]
    
    # Get with default (avoids KeyError)
    number = phone_book.get("unknown", "Not found")
    """)
    
    # Live demo
    print("LIVE DEMO:")
    phone_book = {"jenny": "867-5309", "emergency": "911"}
    print(f"  phone_book = {phone_book}")
    print(f"  phone_book['jenny'] = '{phone_book['jenny']}'")
    print(f"  'emergency' in phone_book = {'emergency' in phone_book}")
    print(f"  phone_book.get('unknown', 'N/A') = '{phone_book.get('unknown', 'N/A')}'")


def demo_check_voter() -> None:
    """Demonstrate the check_voter function."""
    print_header("PART 1: check_voter() - Preventing Duplicates")
    
    print("""
    USE CASE: Voting system that prevents double-voting
    
    From Chapter 5: Hash tables are perfect for checking duplicates!
    
    IMPLEMENTATION:
    ---------------
    def check_voter(voted, name):
        if name in voted:
            print("Kick them out!")
            return False
        else:
            voted[name] = True
            return True
    
    The 'in' operator is O(1) for dictionaries!
    """)
    
    print("Testing check_voter():")
    print("-" * 40)
    
    voted = {}
    
    test_sequence = [
        ("tom", True, "First vote - should be allowed"),
        ("mike", True, "First vote - should be allowed"),
        ("tom", False, "Second vote - should be rejected!"),
        ("alice", True, "First vote - should be allowed"),
    ]
    
    for name, expected, description in test_sequence:
        try:
            result = check_voter(voted, name)
            status = "✅" if result == expected else "❌"
            print(f"  check_voter(voted, '{name}'): {result} {status}")
            print(f"    {description}")
        except Exception as e:
            print(f"  check_voter(voted, '{name}'): ❌ Error: {e}")
    
    print(f"\nFinal voted dict: {voted}")


def demo_hash_table_class() -> None:
    """Demonstrate the HashTable class."""
    print_header("PART 2: HashTable Class")
    
    print("""
    Now implement your own hash table from scratch!
    
    COMPONENTS:
    1. _hash(key) - Convert key to array index
    2. put(key, value) - Insert or update
    3. get(key) - Retrieve value
    4. delete(key) - Remove entry
    
    COLLISION HANDLING (Chaining):
    - Each bucket is a list
    - Multiple items can share the same bucket
    - Search within bucket to find exact key
    
    STRUCTURE:
    buckets = [
        [],                          # bucket 0
        [("apple", 5)],              # bucket 1 - one item
        [("banana", 3), ("cherry", 7)],  # bucket 2 - collision!
        [],                          # bucket 3
        ...
    ]
    """)
    
    print("Testing HashTable class:")
    print("-" * 40)
    
    try:
        ht = HashTable(size=10)
        
        # Test put and get
        print("\n1. Testing put() and get():")
        test_items = [("apple", 5), ("banana", 3), ("cherry", 7)]
        
        for key, value in test_items:
            ht.put(key, value)
            result = ht.get(key)
            status = "✅" if result == value else "❌"
            print(f"   put('{key}', {value}), get('{key}') = {result} {status}")
        
        # Test update
        print("\n2. Testing update (put existing key):")
        ht.put("apple", 10)
        result = ht.get("apple")
        status = "✅" if result == 10 else "❌"
        print(f"   put('apple', 10), get('apple') = {result} {status}")
        
        # Test get non-existent
        print("\n3. Testing get non-existent key:")
        result = ht.get("dragonfruit")
        status = "✅" if result is None else "❌"
        print(f"   get('dragonfruit') = {result} {status}")
        
        # Test delete
        print("\n4. Testing delete():")
        deleted = ht.delete("banana")
        result = ht.get("banana")
        status = "✅" if result is None else "❌"
        print(f"   delete('banana'), get('banana') = {result} {status}")
        
    except Exception as e:
        print(f"   ❌ Error: {e}")


def hash_function_explained() -> None:
    """Explain hash functions."""
    print_header("UNDERSTANDING HASH FUNCTIONS")
    
    print("""
    A hash function converts a key into an array index.
    
    REQUIREMENTS:
    1. Deterministic: same key → same index (always!)
    2. Fast to compute
    3. Distributes keys evenly across buckets
    
    PYTHON'S BUILT-IN HASH:
    -----------------------
    hash("hello")  # Returns a large integer
    hash("hello") % 10  # Convert to index 0-9
    
    YOUR _hash() METHOD:
    --------------------
    def _hash(self, key):
        return hash(key) % self.size
    
    EXAMPLE:
    """)
    
    # Live demo
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    size = 10
    print(f"    Hash table size: {size}")
    print(f"    Bucket assignments:")
    for word in words:
        bucket = hash(word) % size
        print(f"      '{word}' → bucket {bucket}")


def load_factor_explained() -> None:
    """Explain load factor and resizing."""
    print_header("LOAD FACTOR")
    
    print("""
    LOAD FACTOR = (number of items) / (number of buckets)
    
    Example: 7 items in 10 buckets → load factor = 0.7
    
    WHY IT MATTERS:
    - Low load factor (< 0.5): Wasting space, but fast
    - High load factor (> 0.7): More collisions, slower
    - Load factor > 1: Guaranteed collisions!
    
    RULE OF THUMB:
    - Resize when load factor > 0.7
    - Double the size when resizing
    
    PERFORMANCE:
    - O(1) average when load factor is low
    - O(n) worst case when everything collides
    """)


def main():
    """Main entry point."""
    print("\n" + "#️⃣" * 30)
    print("   LAB 05: HASH TABLES")
    print("   O(1) Lookups!")
    print("#️⃣" * 30)
    
    print("""
    📋 YOUR TASKS:
    1. Open hashtable.py
    2. Implement these functions:
       - check_voter()
       - HashTable._hash()
       - HashTable.put()
       - HashTable.get()
       - HashTable.delete()
    3. Run this file to test: python main.py
    4. Run pytest when ready: python -m pytest tests/ -v
    """)
    
    python_dict_intro()
    demo_check_voter()
    demo_hash_table_class()
    hash_function_explained()
    load_factor_explained()
    
    print_header("NEXT STEPS")
    print("""
    When all tests pass, run: python -m pytest tests/ -v
    Then complete the Lab Report in README.md
    """)


if __name__ == "__main__":
    main()
