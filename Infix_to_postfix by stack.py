operators=set(['+','-','*','/','(',')','^'])
priorty={'+':1,'-':1,'*':2,'/':2,'^':3}
def infix_to_postfix(expr):
    stack=[]
    output=""
    for ch in expr:
        if ch not in operators:
            output+=ch
        elif ch=='(':
            stack.append('(')
        elif ch==')':
            while stack and stack[-1]!='(':
                output+=stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!='(' and priorty[ch]<=priorty[stack[-1]]:
                output+=stack.pop()
                print(output)
            stack.append(ch)
    while stack:
        output+=stack.pop()
    return output
expr=input("enter a inifix expression:")
print("infix expression is:",expr)
print("postfix expression is:",infix_to_postfix(expr))
