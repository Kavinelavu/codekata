print("STACK IMPLEMENTATION")
stack=[]
while True:
     print("WHAT PERFORMANCE YOU WANT?\n 1.Insert an element,2.Remove an element,3.Check size of stack,4.Emptiness of stack,5.Exit")
     choice=int(input())
     if choice==1:
       print("Enter the element you want to insert")
       l=input()
       stack.append(l)
       print("Elements in stacks are:",stack)
     elif choice==2:
         if stack==[]:
            print("Empty stack.you can't delete!!")
         else:
             stack.pop()
             print("Elements in stacks are:",stack)
     elif choice==3:
           print("Size of stack in:",len(stack))
          #print("Elements in stack are:",stack)
     elif choice==4:
          if stack==[]:
               print("Your stack is empty!!")
          else:
             print("You have ",len(stack),"elements in our stack")
             print("Elements in stack are:",stack)
     elif choice==5:
        print("Exit")
        break
    
    

    
        
