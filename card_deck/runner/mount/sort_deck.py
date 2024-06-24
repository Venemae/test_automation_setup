def sort_deck(deck_to_sort, deck_to_reference):
        
    import create_deck
    
    state = {}
    
    for symbol in create_deck.card_symbols:
        
        if symbol not in state.keys():

<<<<<<< HEAD
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
=======
    import create_deck
    import json

    state = {}

    for symbol in create_deck.card_symbols:
        
        if symbol not in state.keys():
            
            state[symbol] = []

    print(state.keys())


    for random_card in deck_to_sort:
        
        state[random_card["symbol"]].append(random_card)


    for key in state.keys():
        
        print(f"length of symbol: {key}: {len(state[key])}")



    # for reference_card in deck_to_reference:
        
    #     # print(reference_card)

    #     for pre_sorted_card in state[reference_card["symbol"]]:
            
    #         if f"sorted_symbol_{reference_card['symbol']}" not in state.keys():
                
    #             state[f"sorted_symbol_{reference_card['symbol']}"] = []

    #             print("added empty list")



    #         if pre_sorted_card["value"] == reference_card["value"]:
                
    #             pre_sorted_card["side"] = create_deck.sides[0]

    #             state[f"sorted_symbol_{reference_card['symbol']}"].append(pre_sorted_card)


    refreshed_deck = []
    
    for key in state.keys():
        
        order = ", ".join([str(item["value"]) for item in state[key]])
        
        # print(f"length of symbol: {key}: {len(state[key])} with order: {order}")

        if "sorted_" in key:
            
            refreshed_deck = refreshed_deck + state[key]

    # for i in range(len(deck_to_reference)):
        
    #     print(f"\n{len(json.dumps(refreshed_deck[i]))*'#'}")
    #     print(refreshed_deck[i])
    #     print(deck_to_reference[i])
    #     print(len(json.dumps(refreshed_deck[i]))*"#", "\n")

    # deck_to_sort

    return state

# Bubble sort in Python

def bubbleSort(array, deck_to_reference):

    import json
    # print(array)

    temp = {}

    for key in array.keys():
     
        print(key)

        # loop to access each array element
        for i in range(len(array[key])):

            # loop to compare array elements
            for j in range(0, len(array[key]) - i - 1):

                # compare two adjacent elements
                # change > to < to sort in descending order
                if array[key][j]["value"] > array[key][j + 1]["value"]:

                    # swapping elements if elements
                    # are not in the intended order
                    temp[key] = array[key][j]
                    array[key][j] = array[key][j+1]
                    array[key][j+1] = temp[key]

#   print(array)

    refreshed_deck = []

    for key in array.keys():
        
        order = ", ".join([str(item["value"]) for item in array[key]])
            
        print(f"length of symbol: {key}: {len(array[key])} with order: {order}")

        refreshed_deck = refreshed_deck + array[key]


    for i in range(len(refreshed_deck)):
        
        print(f"\n{len(json.dumps(refreshed_deck[i]))*'#'}")
        print(refreshed_deck[i])
        print(deck_to_reference[i])
        print(len(json.dumps(refreshed_deck[i]))*"#", "\n")    


>>>>>>> e9ec508e76e99bd039de17e151e26d08b04595dc
