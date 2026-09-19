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


         