person={"name":"John Green","gender":"M","age":"35","address":"109 Penny Lane","phone":"0774154353"}

key=input("What information do you want to know about the person?").lower()

result=person.get(key,"That information is not available")

print(result)
