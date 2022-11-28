test_cases=int(input("Enter the number of test cases:"))
print(test_cases)
# dict1={}
final_dict={}
final_list = []
for each in range(1,test_cases+1):
    
    no_of_tweets=int(input("Enter the number of tweets in each test case:"))
    print(no_of_tweets)
    dict_new={}
    
    for each_tweet in range(1,no_of_tweets+1):        
        
        #each_tweet
        enter_name,tweet_id=input("Enter the inputs:").split()
    
        if enter_name in dict_new:
            dict_new[enter_name]+=1
        else:
            dict_new[enter_name]=1
    
    #print(dict_new)

    
    tweet_max = max(dict_new, key= lambda x: dict_new[x])
    print(tweet_max, dict_new[tweet_max])
    
    
    final_dict[tweet_max] = dict_new[tweet_max]

    print("sort by value")
    
    
    if final_dict[tweet_max] in dict_new.values():
        print("the list ")
        print(list(dict_new.keys())[list(dict_new.values()).index(dict_new[tweet_max])])
    
    final_list.append(final_dict.copy())

    
        
print(final_list)        
