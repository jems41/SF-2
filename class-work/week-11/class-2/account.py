from __future__ import annotations

class Account:
    def __init__(self, gold):
        '''
        crate Account with gold
        '''
        self.gold = gold

    def addGold(self, amount: int) -> None:
        self.gold += amount
    
    def zeroGold(self) -> None:
        self.gold = 0
    
    def doubleGold(self) -> None:
        self.gold = self.gold * 2
    
    def __lt__(self, other: Account) -> bool:
        '''
        return True if Account and other are of the same type
        and gold of Account is less than gold of other
        '''
        return isinstance(other, Account) and self.gold < other.gold
    
    def __eq__(self, other: Account) -> bool:
        return isinstance(other, Account) and self.gold == other.gold
    
a1 = Account(500)
a2 = Account(500)
a3 = Account(56)
a4 = Account(34)

value = 500

print('a4 <? a3: ', a4 < a3)
print('a1 <? a4: ', a1 < a4)
print('a1 ==? a3: ', a1 == a3)
print('a1 ==? a2: ', a1 == a2)
print('a1 ==? value: ', a1 == value)