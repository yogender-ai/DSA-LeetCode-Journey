# 443. String Compression
class Solution:
    def compress(self, chars: list[str]) -> int:
        ans=""
        if len(chars)>0:
            start=1
            count=1
            q=chars[0]
            ans+=q
            for x in range(1,len(chars)):


                if q==chars[x]:
                    count+=1

                if x==len(chars)-1:
                    if q != chars[x] and start==0:
                        ans += q
                        if count != 1:
                            ans += str(count)

                        ans += chars[x]
                        break
                    elif q!=chars[x] and start==1:
                        if count!=1:
                            ans+=str(count)
                            ans+=chars[x]
                        break
                    else:
                        if start==0:
                            ans+=q
                            ans+=str(count)

                        else:
                            ans+=str(count)
                        break
                if q!=chars[x]:


                    if start==0 :
                        ans+=q
                        if count==1:
                            pass
                        else:
                            ans+=str(count)
                        count=1

                    else:
                        if count==1:
                            pass
                        else:
                            ans+=str(count)
                        count=1
                        start=0
                q=chars[x]
        chars[:]=ans
        return len(ans)

# 1047. Remove All Adjacent Duplicates In String
class Solution:
    def removeDuplicates(self, s: str) -> str:
        l=list(s)
        stack=[]
        stack.append(l[0])
        l.pop(0)
        a=0
        ans=list()
        while len(l)!=0:
            if stack and l[0]==stack[-1] :
                stack.pop()
                l.pop(0)
            else:
                stack.append(l[0])
                l.pop(0)
        while stack:
            ans.append(stack[-1])
            stack.pop()
        ans.reverse()
        a="".join(ans)
        return a

        
