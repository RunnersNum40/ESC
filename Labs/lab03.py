#Problem 1
import lab02
if 'main' == 'main':
    lab02.initialize()
    lab02.add(45)
    if lab02.current_value == 45:
      print("Test 1 passed")
    else:
      print("Test 1 failed")

#Problem 2
def check_sum(n):
    return sum(i for i in range(n))**2 == sum(i**3 for i in range(n))

def check_sums_up_to_n(N):
    return all(check_sum(n) for n in range(N+1))

print(check_sums_up_to_n(100))

#Problem 3
total = 0
for i in range(1001):
    total += ((-1)**i)/(2*i+1)
print(total*4)