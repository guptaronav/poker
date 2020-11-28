import random
import time
import sys
from collections import Counter

Deck_Value=[1,2,3,4,5,6,7,8,9,10,11,12,13,
            1,2,3,4,5,6,7,8,9,10,11,12,13,
            1,2,3,4,5,6,7,8,9,10,11,12,13,
            1,2,3,4,5,6,7,8,9,10,11,12,13]

def Compare(A,B):
  if Deck_Value[A]>Deck_Value[B]:
    return 1
  elif Deck_Value[A]<Deck_Value[B]:
    return -1
  else:
    return 0

########################### POKER RULES ###########################

def Is_Straight(Cards):
  Card_Value=[]
  for i in Cards:
    Card_Value.append(Deck_Value[i])
  Card_Value.sort()
  if Card_Value[0]+1==Card_Value[1] and Card_Value[1]+1==Card_Value[2] and Card_Value[2]+1==Card_Value[3] and Card_Value[3]+1==Card_Value[4]:
    return True
  elif Card_Value[4] in Aces:
      if Card_Value[4]-12==Card_Value[0] and Card_Value[0]+1==Card_Value[1] and Card_Value[1]+1==Card_Value[2] and Card_Value[2]+1==Card_Value[3]:
        return True
      else:
        return False
  else:
    return False

def Is_Flush(Cards):
  return all(item in Spades for item in Cards) or all(item in Clubs for item in Cards) or all(item in Hearts for item in Cards) or all(item in Diamonds for item in Cards)
  
def Is_Straight_Flush(Cards):
  return Is_Straight(Cards) and Is_Flush(Cards)

def Is_Royal_Flush(Cards):
  Cards.sort(reverse=1)
  return Cards[0] in Aces and Is_Straight_Flush(Cards)

def OAK(Cards):
  Card_Value=[]
  for i in Cards:
    Card_Value.append(Deck_Value[i])
  return max(Counter(Card_Value).values())

# Get Max Repeat Card
def Get_MRC(Cards):
  Card_Value=[]
  for i in Cards:
    Card_Value.append(Deck_Value[i])
  Values=list(Counter(Card_Value).values())
  Keys=list(Counter(Card_Value).keys())
  Max_Value_Index=Values.index(max(Values))
  return Keys[Max_Value_Index]

# Get Top Two Repeat Cards
def Get_TTRC(Cards):
  Card_Value=[]
  for i in Cards:
    Card_Value.append(Deck_Value[i])
  Values=list(Counter(Card_Value).values())
  Keys=list(Counter(Card_Value).keys())
  if 1 in Values:
      Min_Value_Index=Values.index(1)
      Keys.pop(Min_Value_Index)
  return Keys

def Is_Four_of_a_Kind(Cards):
  return OAK(Cards)==4

def Is_Three_of_a_Kind(Cards):
  return OAK(Cards)==3

def Is_One_Pair(Cards):
  return OAK(Cards)==2

def Is_Two_Pair(Cards):
  Card_Value=[]
  for i in Cards:
    Card_Value.append(Deck_Value[i])
  return not Is_Three_of_a_Kind(Cards) and len(Counter(Card_Value).keys())==3

def Is_Full_House(Cards):
  Card_Value=[]
  for i in Cards:
    Card_Value.append(Deck_Value[i])
  return len(Counter(Card_Value).keys())==2 and Is_Three_of_a_Kind(Cards)

## HIGH CARDS
def Get_High_Card(Cards):
  Card_Value=[]
  for i in Cards:
    Card_Value.append(Deck_Value[i])
  Card_Value.sort(reverse=1)
  return Card_Value[0]

def Get_2nd_High_Card(Cards):
  Card_Value=[]
  for i in Cards:
    Card_Value.append(Deck_Value[i])
  Card_Value.sort(reverse=1)
  return Card_Value[1]

def Get_3rd_High_Card(Cards):
  Card_Value=[]
  for i in Cards:
    Card_Value.append(Deck_Value[i])
  Card_Value.sort(reverse=1)
  return Card_Value[2]

def Get_4th_High_Card(Cards):
  Card_Value=[]
  for i in Cards:
    Card_Value.append(Deck_Value[i])
  Card_Value.sort(reverse=1)
  return Card_Value[3]

def Get_5th_High_Card(Cards):
  Card_Value=[]
  for i in Cards:
    Card_Value.append(Deck_Value[i])
  Card_Value.sort(reverse=1)
  return Card_Value[4]
  