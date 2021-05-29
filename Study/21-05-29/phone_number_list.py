phone_book = ["18", "129", "2345","487","2346","23456"]
 
def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(0, len(phone_book)-1):
        if len(phone_book[i]) <= len(phone_book[i+1]):
            if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
                answer = False
        if answer == False:
            break

    return answer

print(solution(phone_book))