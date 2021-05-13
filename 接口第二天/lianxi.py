'''
求列表的最大值
'''
# def get_max(list1):
#     max_list=list1[0]
#     for i in range(len(list1)):
#         if list1[i]>max_list:
#            max_list= list1[i]
#     return max_list
# list1=[1,4,7,9,10]
# max=get_max(list1)
# print(max)
'''
求学生最高分数的科目和分数
'''
# def get_max_score(dict1):
#     a=0
#     for b in dict1.values():
#         if b>a:
#             a=b
#     for c in dict1.keys():
#         if dict1[c]==a:
#             return c,a
# dict1={'语文':90,'数学':96,'英语':98}
# course,score=get_max_score(dict1)
# print(course,score)
'''
判断回文
'''
# def huiwen(str):
#     for i in range(len(str)):
#         if str[i]!=str[len(str)-i-1]:
#             return '不是回文字符'
#         else:
#             return '是回文字符'
# str=input('请输入字符串:')
# print(huiwen(str))
'''
打印九九乘法表
'''
j=1
while j<=9:
    i=1
    while i<=j:
        print(f'{i}*{j}={i*j}',end=' ')
        i=i+1
    j=j+1
    print()








