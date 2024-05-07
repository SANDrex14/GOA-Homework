#დღეს ვისაუბრებთ სიებზე ეგრედწოდებულ  Lists ზე
# სიები გამოიყენება რამდენიმე ელემენტის ერთ ცვლადში შესანახად.

# სიები არის ერთ-ერთი 4 ჩაშენებული მონაცემთა ტიპიდან Python-ში, რომელიც გამოიყენება მონაცემთა კოლექციების შესანახად, 
# დანარჩენი 3 არის Tuple, Set და Dictionary, ყველა განსხვავებული ხარისხისა და გამოყენების.

# სიები იქმნება კვადრატული ფრჩხილების გამოყენებით:

# მაგალითი , მოდი შევქმნათ სია:

thislist = ["apple", "banana", "cherry"]
print(thislist)

#სიის ელემენტები ინდექსირებულია, პირველ პუნქტს აქვს ინდექსი [0], მეორე პუნქტს აქვს ინდექსი [1] და ა.შ.
 # გამოდის რომ "apple" არის ინდექსი [0] , "banana" არის ინდექსი [1] , "cherry" არის ინდექსი [2].

#როდესაც ვამბობთ, რომ სიები დალაგებულია, 
# ეს ნიშნავს, რომ ნივთებს აქვთ განსაზღვრული თანმიმდევრობა და ეს თანმიმდევრობა არ შეიცვლება თუ სიას ახალ ელემენტებს დაამატებთ, 
# ახალი ელემენტები სიის ბოლოს განთავსდება.

#დუბლიკატების დაშვება ვინაიდან სიები ინდექსირებულია, სიებს შეიძლება ჰქონდეთ იგივე მნიშვნელობის ელემენტები

#მაგალითი იმისა რომ სიები იძლევა დუბლიკატულ მნიშვნელობებს:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#სიის სიგრძე იმის დასადგენად, თუ რამდენი ელემენტი აქვს სიას, გამოიყენეთ len() ფუნქცია:
#მაგალითად ამობეჭდეთ სიაში არსებული ნივთების რაოდენობა:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# სიის ელემენტები - მონაცემთა ტიპები
# სიის ელემენტები შეიძლება იყოს ნებისმიერი ტიპის მონაცემთა:

# მაგალითი იმისა რომ შეიძლება იყოს string(str),integer(int),boolean მონაცემთა ტიპები:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# პითონის პერსპექტივიდან, სიები განისაზღვრება, როგორც ობიექტები მონაცემთა ტიპის 'list':
# რა არის სიის მონაცემთა ტიპი?
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#ასევე შესაძლებელია list() კონსტრუქტორის გამოყენება ახალი სიის შექმნისას.
#მაგალითი იმისა რომ , list() კონსტრყქტორის გამოყენება შეიძლება ახალი სიის შესაქმნელად:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#წვდომა ნივთებზე - სიის ელემენტები ინდექსირებულია და მათზე წვდომა შეგიძლიათ ინდექსის ნომრის მითითებით მაგალითად:
# ამობეჭდეთ სიის მეორე ელემენტი:

thislist = ["apple", "banana", "cherry"]
print(thislist[1]) #banana

# ნეგატიური ინდექსირება
# ნეგატიური ინდექსირება ნიშნავს ბოლოდან დაწყებას

# -1 ეხება ბოლო პუნქტს, -2 ეხება მეორე ბოლო პუნქტს და ა.შ.
#მაგალითი - ამობეჭდეთ სიის ბოლო ელემენტი:

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#ინდექსების დიაპაზონი (range)
#თქვენ შეგიძლიათ მიუთითოთ ინდექსების დიაპაზონი იმის მითითებით, თუ სად უნდა დაიწყოს და სად დასრულდეს დიაპაზონი.
# დიაპაზონის მითითებისას, დაბრუნების მნიშვნელობა იქნება ახალი სია მითითებული ელემენტებით.

#მაგალითი - დააბრუნეთ მესამე, მეოთხე და მეხუთე ელემენტი:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# ეს მაგალითი აბრუნებს ელემენტებს თავიდანვე, მაგრამ არ მოიცავს "kiwi" - ს

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# საბოლოო მნიშვნელობის გამოტოვებით, დიაპაზონი გადავა სიის ბოლომდე:
# ეს მაგალითი აბრუნებს ელემენტებს "cherry" დან ბოლომდე:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# უარყოფითი ინდექსების დიაპაზონი
# მიუთითეთ უარყოფითი ინდექსები, თუ გსურთ დაიწყოთ ძებნა სიის ბოლოდან:
#ეს მაგალითი აბრუნებს ელემენტებს "ფორთოხლის" (-4)-დან, მაგრამ არ შეიცავს "მანგოს" (-1):

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# შეამოწმეთ არის თუ არა ელემენტი სიაში 
# იმის დასადგენად, არის თუ არა მითითებული ელემენტი სიაში, გამოიყენეთ საკვანძო სიტყვა: in
# შეამოწმეთ არის თუ არა "ვაშლი" სიაში:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# ნივთის მნიშვნელობის შეცვლა
# კონკრეტული ცვლადის მნიშვნელობის შესაცვლელად, იხილეთ ინდექსის ნომერი:

# შევცვალოთ მეორე ცვლადი 

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# შეცვალეთ საქონლის მნიშვნელობების დიაპაზონი
# ერთეულების მნიშვნელობის შესაცვლელად კონკრეტულ დიაპაზონში, განსაზღვრეთ სია ახალი მნიშვნელობებით და მიმართეთ ინდექსის ნომრების დიაპაზონს, სადაც გსურთ ახალი მნიშვნელობების ჩასმა:

# შეცვალეთ მნიშვნელობები "banana" და "cherry" მნიშვნელობებით "blackcurrant" და "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# თუ თქვენ ჩასვამთ უფრო მეტ ელემენტს, ვიდრე ჩაანაცვლებთ, ახალი ერთეულები ჩასმული იქნება იქ, სადაც თქვენ მიუთითეთ, ხოლო დანარჩენი ელემენტები შესაბამისად გადაადგილდებიან:
# შეცვალეთ მეორე მნიშვნელობა, შეცვალეთ იგი ორი ახალი მნიშვნელობით:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# თუ ჩასვამთ იმაზე ნაკლებ ელემენტს, ვიდრე ჩაანაცვლებთ, ახალი ელემენტები ჩასმული იქნება იქ, სადაც თქვენ მიუთითეთ, ხოლო დანარჩენი ელემენტები შესაბამისად გადაადგილდებიან:
# შეცვალეთ მეორე და მესამე მნიშვნელობა ერთი მნიშვნელობით შეცვლით:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

# ნივთების ჩასმა
# სიის ახალი ელემენტის ჩასასმელად, რომელიმე არსებული მნიშვნელობის ჩანაცვლების გარეშე, შეგვიძლია გამოვიყენოთ insert() მეთოდი.

# insert() მეთოდი ათავსებს ელემენტს მითითებულ ინდექსზე:

# მაგალითი ,  ჩადეთ "საზამთრო" მესამე პუნქტად:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# ნივთების დამატება
# სიის ბოლოს ელემენტის დასამატებლად გამოიყენეთ append() მეთოდი:

#  მიიღეთ თქვენი საკუთარი Python სერვერი:
# ელემენტის დასამატებლად append() მეთოდის გამოყენებით:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# სიის გაფართოება
# სხვა სიიდან მიმდინარე სიაში ელემენტების დასამატებლად გამოიყენეთ extend() მეთოდი.

# მაგალითი , დაამატეთ tropical ელემენტები ამ სიაში:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#ამოიღეთ მითითებული ელემენტი
#remove() მეთოდი შლის მითითებულ ელემენტს.

#მაგალითი ამოიღეთ "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# თუ არის ერთზე მეტი ელემენტი მითითებული მნიშვნელობით, remove() მეთოდი აშორებს პირველ შემთხვევას:
# მაგალითად წაშალეთ "banana" პირველი შემთხვევა:

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#ამოიღეთ მითითებული ინდექსი
#pop() მეთოდი შლის მითითებულ ინდექსს.

# მაგალითად წაშალეთ მეორე ელემენტი:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# თუ არ მიუთითებთ ინდექსს, pop() მეთოდი წაშლის ბოლო ელემენტს.

# მაგალითად ამოიღეთ ბოლო ელემენტი:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# საკვანძო სიტყვა del ასევე შლის მითითებულ ინდექსს:

# მაგალითად ამოიღეთ პირველი ელემენტი:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


# საკვანძო სიტყვა del ასევე შეუძლია წაშალოს სია მთლიანად.

# მაგალითად წაშალეთ მთელი სია:

thislist = ["apple", "banana", "cherry"]
del thislist


#nსიის გასუფთავება
# clear() მეთოდი ასუფთავებს სიას.

#სია კვლავ რჩება , მაგრამ მას არ აქვს შინაარსი.

# მაგალითად სიის შინაარსის გასუფთავება:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# ციკლი სიის მეშვეობით
# თქვენ შეგიძლიათ გადახედოთ სიის ელემენტებს for loop-ის გამოყენებით:
# დაბეჭდეთ ყველა ელემენტი სიაში, სათითაოდ:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# ციკლი ინდექსის ნომრების მეშვეობით თქვენ ასევე შეგიძლიათ გადახედოთ სიის ელემენტებს მათი ინდექსის ნომრის მითითებით.

# გამოიყენეთ range() და len() ფუნქციები შესაბამისი გამეორების შესაქმნელად.

#მაგალითად დაბეჭდეთ ყველა ელემენტი მათი ინდექსის ნომრის მითითებით:
  
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

# while Loop-ის გამოყენება
# თქვენ შეგიძლიათ გადახედოთ სიის ელემენტებს while loop-ის გამოყენებით.

# გამოიყენეთ len() ფუნქცია სიის სიგრძის დასადგენად, შემდეგ დაიწყეთ 0-დან და გაიარეთ გზა სიის ელემენტებში მათი ინდექსების მითითებით.

# გახსოვდეთ, რომ ყოველი გამეორების შემდეგ უნდა გაზარდოთ ინდექსი 1-ით.

# მაგალითად დაბეჭდეთ ყველა ელემენტი, დროის მარყუჟის გამოყენებით ყველა ინდექსის ნომრის გასავლელად
  
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1