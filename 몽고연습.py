import pymongo

a_var = {
    "name": "james",
    "age": 25,
    "city": "ChungJu",
    "profile_pic" : [
        "pic_a.png",
        "pic_b.png"
    ]
}

b_var = {
    "name": "jongho",
    "age": 24,
    "city": "ChungJu",
    "profile_pic" : [
        "pic_a.png",
        "pic_b.png"
    ]
}

c_var = {
    "name": "name",
    "age": 22,
    "city": "ChungJu",
    "profile_pic" : [
        "pic_a.png",
        "pic_b.png"
    ]
}

connect_to = pymongo.MongoClient("localhost",27017) #파이썬에서 mongodb로 연결한다. 27017은 mongodb에서 설정한 포트번호
mdb = connect_to.test_db # connection에서 test_db라는 카테고리 명을 만들고 

collection = mdb.members # 그 밑에 collection 명을 members
collection.insert_many([a_var,b_var,c_var]) # 데이터 입력

searched = collection.find()
print(searched)
print(searched[0])

searched = collection.find({"$or": [{"name": "jongho"},{"name": "name"}]})

for _ in searched :
    print(_)