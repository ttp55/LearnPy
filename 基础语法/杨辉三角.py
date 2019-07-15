
def yanghui(max):
   N = [1]
   m = 1

   while m < max:
       yield N
       N.append(0)
       N = [N[i-1]+N[i] for i in range(len(N))]
       m += 1
   return 'done!'


f = yanghui(11)


while True:
    try:
        x = next(f)
        print(x)
    except StopIteration as e:
        print(e.value)
        break

