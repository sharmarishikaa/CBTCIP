import random
n1=random.randint(1000,9999)
n2=int(input("Enter four digit number: "))
display=[]
for i in range(len(str(n2))):
    display+="_"
if(n1==n2):
    print("YOU ARE A MASTERMIND YOU GOT THE CORRECT NUMBER IN JUST ONE GUESS!!")
ctr=0
guess=True
while guess:
    count=0
    ctr=ctr+1
    n1=str(n1)
    n2=str(n2)
    for i in range(0,4,1):
        if(n1[i]==n2[i]):
            display[i]=n2[i]
            count=count+1
        
    if(count>=0 and count<4):
        print(f"That's not the correct number, you have got {count} correct digits")
        print(display)
        n2=int(input("Again enter the number: "))

    if n1==n2:
        print("\n")
        print(f"The answer is {display}")
        print(f"you have got the correct number in {ctr} guesses")
        print("CONGRATS!! YOU ARE A MASTERMIND")
        guess=False
