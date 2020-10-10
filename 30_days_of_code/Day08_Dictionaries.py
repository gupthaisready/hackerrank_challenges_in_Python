num_phone_book_entries = int(input())
phone_book = {}
while num_phone_book_entries > 0:
    num_phone_book_entries -= 1
    key_name, value_phone = input().split()
    phone_book[key_name] = value_phone

while True:
    try:
        search_name = input()
        if search_name in phone_book:
            print(f"{search_name}={phone_book[search_name]}")
        else:
            print("Not found")
    except:
        break
