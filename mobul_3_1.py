calls=0

def count_calls():
    global calls
    calls += 1


def string_info(string):
    n = len (string), string.upper (), string.lower ()
    print (n)
    count_calls ()

def is_contains(string, list_to_search):
    list_to_search = str (list_to_search)
    list_to_search = list_to_search.upper ()
    print (string in list_to_search)
    count_calls ()

string_ = 'Сегодня отличная погода', 'Теплое лето', "вся земля"
for i in range (3):
    string = string_[i]
    string_info (string)

list_to_search_ = (('Теплое лето', "вся земля", 'город мой'), ('Теплое лето', 'земля вся'))
string = "ВСЯ земля"
string = string.upper ()
for i in range (2):
    list_to_search =  list_to_search_[i]
    is_contains (string, list_to_search)
print('Функции вызывались',calls,'раз')
