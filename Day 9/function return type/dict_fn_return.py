def phonebook():
    phonebook = {
        "Alice": 1234567890,
        "Bob": 9876543210,
        "Charlie": 5555555555
    }
    return phonebook
    
x = phonebook()

print(type(phonebook()))




for k,v in x.items():
    print(f"{k}: {v}")
    
    