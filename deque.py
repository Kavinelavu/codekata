print("DEQUE IMPLEMENTATION")
deque=[]
while True:
     print("WHAT PERFORMANCE YOU WANT?\n 1.Insert an element,2.Remove an element,3.Check size of stack,4.Emptiness of stack,5.Exit")
     choice=int(input())
     if choice==1:
       print("Enter the element you want to insert")
       l=input()
       print("where to insert?1.first,2.last")
       c=int(input())
       if  c==1:
             deque.insert(0,1)
     if choice==2:
           deque.append(l)
     elif choice==2:
         if deque==[]:
            print("Empty stack.you can't delete!!")
         else:
             stack.pop()
             print("Elements in stacks are:",deque)
     elif choice==3:
           print("Size of stack in:",len(deque))
          #print("Elements in stack are:",stack)
     elif choice==4:
          if deque==[]:
               print("Your stack is empty!!")
          else:
             print("You have ",len(deque),"elements in our stack")
             print("Elements in stack are:",deque)
     elif choice==5:
        print("Exit")
        break
