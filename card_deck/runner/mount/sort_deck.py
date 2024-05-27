def sort_deck(deck_to_sort, deck_to_reference):
        
    import create_deck
    
    state = {}
    
    for symbol in create_deck.card_symbols:
        
        if symbol not in state.keys():

                state[symbol] = []
            
    print(state.keys())
        
    print("sorting starts here")
    
    for random_card in deck_to_sort:
        
        state[random_card['symbol']].append(random_card)
        
    for key in state.keys():
        
        print(f"lenght of symbol: {key}: {len(state[key])}")
        
        
    
    # for reference_card in deck_to_reference:
        
    #     print(reference_card)
        
    #     for pre_sorted_card in state[reference_card["symbol"]]:
            
    #         if f"sorted_symbol_{reference_card['symbol']}" not in state.keys():
            
    #             state[f"sorted_symbol_{reference_card['symbol']}"] = []
                
    #             print("added empty list")
                
    #         if pre_sorted_card["value"] == reference_card["value"]:
            
    #             state[f"sorted_symbol_{reference_card['symbol']}"].append(pre_sorted_card)
                
    #         for key in state.keys():
            
    #             order = ",".join([str(item["value"]) for item in state [key]])
                
    #             print (f"lenght of symbol: {key}: {len(state[key])} with order: {order}")
                
                
                
            
            
            
    
    # deck_to_sort
    
    return state

def bubbleSort(array):

    print(array)
    temp = ()
    
    for key in array.keys():
    
        print(key)
        
for i in range(len(array[key])):

    for j in range(0, len(array[key]) - j  - 1):
        
        if array[key][j]["value"] > array[key][j + 1]["value"]:
        
            temp[key] = array[key][j]
            array[key][j] = array[key][j + 1]
            array[key][j + 1] = temp[key]