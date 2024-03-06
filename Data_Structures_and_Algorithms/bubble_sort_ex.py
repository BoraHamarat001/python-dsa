def bubble_sort(numbers,key):
    last_index=len(numbers)
    for _ in range(len(numbers)-1):
        last_index=last_index-1
        swapped=False
        for i in range(last_index):
            if numbers[i][key]>numbers[i+1][key]:
                number2=numbers[i]
                numbers[i]=numbers[i+1]
                numbers[i+1]=number2 
                swapped=True
        if not swapped:
            break
    return numbers       
elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]    
print(bubble_sort(elements,"transaction_amount"))