'''ვქმნი ფუნქციას, რომელიც დაშიფრავს text-ს ვიჟინერის შიფრით, სადაც გასაღები იქნება key.
   text და key-ც არის ან string ან truple ან list'''
def encrypt(text, key):
    '''ინიცილიზაციას ვუკეთებ პასუხის სტრინგს'''
    answer='' 
    ''''სათითაოდ გავდივართ ყველა ასოს text-შიც და key-შიც, (ერთნაირი სიგრძე აქვს)'''
    for i in range(len(text)): 
        '''აქ გადაგვყავს char->int-ად და ვუმატებთ text-ის ასოს შესაბამისი key-ს ასოს და ვინახავთ answer-ში, ისე რომ 
           ანბანის ზღვრის გაცდენისას,ანბანს გადიოდეს მე-2 წრეზე, თან ყველა ასო გადამყავს დაბალ რეგსიტრშსი, შესაბამისად
           -> პასუხიც იქნება დაბალ რეგისტრშიც'''
        answer+=chr((ord(text[i].lower())+ord(key[i].lower())-2*97)%26+97) 
        '''ვაბრუნებთ პასუხს string-ად'''
    return answer 

'''დამატების მაგივრად text-ის ასოებს ვაკლებთ key-ს ასოებს დანარჩენი იგივენაირად მუშაობს'''
def decrypt(text,key):
    answer=''
    for i in range(len(text)):
        answer+=chr((ord(text[i].lower())-ord(key[i].lower()))%26+97)
    return answer

tuple_text=('a','t','t','a','c','k','a','t','d','a','w','n')
tuple_key =('l','e','m','o','n','l','e','m','o','n','l','e')

list_text=['a','t','t','a','c','k','a','t','d','a','w','n']
list_key =['l','e','m','o','n','l','e','m','o','n','l','e']

str_text='ATTACKATDAWN'
str_key ='LEMONLEMONLE'

str_encrypted_text='lxfopvefrnhr'

print(" Text: ",str_text+'\n',"Key: ",str_key+'\n',"Encrypted text: ", encrypt(str_text,str_key))
print('\n')
print(" Text: ",str_text+'\n',"Key: ",str_key+'\n',"Derypted text: ", decrypt(str_encrypted_text,str_key))