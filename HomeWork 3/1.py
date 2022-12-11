# O(1)
class Solution:
    def isPalindrome(self, head):
        x = head
        y = head
        while x and x.next:             #идет поиск середины
            x = x.next.next
            y = y.next
        bufer = None
        while y:                        #переворот второй половины списка
            y = y.next
            bufer = y.next
        l, r = head, bufer
        while r:                        #проверка на палиндром
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True



