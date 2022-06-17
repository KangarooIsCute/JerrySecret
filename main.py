# TODO 没啥用函数
def stop():
    return
# TODO 定义变量
name = input("please enter your name:")
age = input("please enter your age:")
hobbie = input("please enter your hobbie:")
user_info = {
    "name": name,
    "age": age,
    "hobbie": hobbie
}
userCard = f"""
-------------{name}的信息卡--------------
             {name}'s user card        
name: {name}                           
名字: {name}                            
                                       
age: {age}years old                    
年龄: {age}岁                          
                                       
hobbie: {hobbie}                      
爱好: {hobbie}                       
----------------------------------------
"""
print(user_info)
print(userCard)
# TODO 坑严立恒
# if name == "Jerry":
#     print("滚！！！")
#     stop()
# elif name == "jerry":
#     print("滚！！！")
#     stop()
# elif name == "Alex":
#     print("输的真好！！！")
# elif name == "alex":
#     print("输的真好！！！")
# TODO 将数据写入文件里
with open("userInfo.txt", "a") as f:
    f.write("\n")
    f.write(userCard)
    print("over!")