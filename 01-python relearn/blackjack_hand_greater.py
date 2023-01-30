
#-----------------------------------
def blackjack_hand_greater_than(hand_1, hand_2):
    ten=["K",'J','Q']
    A_index_1=[]
    A_index_2=[]
    for i in range(len(hand_1)):
        if hand_1[i] in ten:
            hand_1[i]='10'
        elif hand_1[i]=='A':
            A_index_1.append(i)
            hand_1[i]='11'
            
    for i in range(len(hand_2)):
        if hand_2[i] in ten:
            hand_2[i]='10'
        elif hand_2[i]=='A':
            A_index_2.append(i)
            hand_2[i]='11'
          
    hand_1=[int(a) for a in hand_1]
    hand_2=[int(a) for a in hand_2]
    

    if sum(hand_1) >21:
        while len(A_index_1)!=0:
            if sum(hand_1)>21:
                hand_1[A_index_1.pop()]=1
            else:
                break
        if sum(hand_1)>21:
            return False
        
    if sum(hand_2)>21:
        while len(A_index_2)!=0:
            if sum(hand_2)>21:
                hand_2[A_index_2.pop()]=1
            else:
                break
        if sum(hand_2)>21:
            return True
        
    
    if sum(hand_1)>sum(hand_2):
        return True
    else:
        return False



#-----------------------------------
if __name__=='__main__':
    print(blackjack_hand_greater_than(['3', '2', '6', '8'], ['8', 'A', '5']))