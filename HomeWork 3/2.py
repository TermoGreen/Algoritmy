#О(N)
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        h_list = head
        score = ''
        while h_list:                           # добавление каждого элемента цикла в h_list
            score += str(h_list.val)
            h_list = h_list.next
        return(int(score,2))                    # возвращение числа в десятичной СС