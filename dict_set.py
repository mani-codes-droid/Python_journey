#que
dict = {
    "name" : "manasvi",
    "age" : 15,
    "is_teen" : True,
    "marks" : 91.4,
    "score" : {
        "chemistry" : 98,
        "physics": 99,
    },
    "subject" : ("java", "python", "C++"),
    "topics" : ["Dictionary", "Sets"]
}
print(dict)

#que
coll = {1, 2, 3, 4, 5, "manasvi", "karan", 2, 3, 2, 1}
print(coll.pop())
print(coll)
coll.add(("smriti", 67, 87))
print(coll)
print(len(coll))

print(len(coll))
print(coll)
coll.clear()

#que
set1= {1,2,3,4}
set2 = {3,4,5,6}
print(set1.intersection(set2))

#let's practice

dict = {
    "table" : ("a piece of furniture", "list of facts and figures"),
    "cat" : "a small animal"
}
print(dict)

#que
student = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print(student)
print(len(student))
 
 #que
marks = {}

a = int(input("Enter Physics marks: "))
marks.update ({"Physics" : a})

b = int(input("Enter Chemistry marks: "))
marks.update ({"Chemistry" : b})

c = int(input("Enter Biology marks: "))
marks.update ({"Biology" : c})

d = int(input("Enter Maths marks: "))
marks.update ({"Maths" : d} )

print(marks)

#que
set= {9 , "9.0"}
print(set)