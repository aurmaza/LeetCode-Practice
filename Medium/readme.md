groupAnagrams:
use hashmap to store
sorted word: all words that matched that sorted word

topKFrequent elements:

    1. Create a dictionary
        number:frequency of number
    2.Create a list of lists that is of length n
        go through k,v pairs
        list[v].append(k)
    3.Go throgh said list in reverse order
        append to a res list all of the items in the nested list unitl
        the len of res is equal to k
    return res

    Something learned:
        Shadowing
        I shadowed the value of k with the last key found from doing for k,v in list.items();
