import math

ui = input("Mersenne prime postion ?")

user_in = int(ui)

def perfect_num_check(user_num):
    factors = []
    for check_nums in range(1, user_num):
        if user_num % check_nums == 0:
            factors.append(check_nums)

    print(str(factors))
    sum_factors = 0
    for nums in factors:
        sum_factors = sum_factors + nums
    print(sum_factors)

    if sum_factors == user_num:
        print("Number is Perfect")
    else:
        print("Not Perfect Number")

def prime_num_check(num):
    #print("prime check function called")
    flag = False
    if (num == 1 or num == 0):
        #print(str(num) + " not a Prime Number !!")
        return 0
    elif (num == 2 or num == 3):
        #print(str(num) + " is a Prime Number !!")
        return 1
    else:
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

        # check if flag is True
        if flag:
            #print(num, "is not a prime number")
            return 0
        else:
            #print(num, "is a prime number")
            return 1



prime_list = []

m_prime_list = []


count = 0
natural_numbers = 0
pos = 0
#Regarding Table to display
print("\n")
print("------------------------------------------------------------")
print("Position             Prime Number            Mersenne prime")
print("------------------------------------------------------------")
while True:

    if prime_num_check(natural_numbers) == 1:
        prime_list.append(natural_numbers)
        #print(natural_numbers)
        for primes in [prime_list[pos]]:
            m_prime = pow(2, primes) - 1
            #print("\n")
            #print("Calculated Mersenne prime for prime number "+ str(primes)+" and Checking whether it is prime........... ")
            #print("Flag value for prime number "+str(primes)+" is "+str(prime_num_check(m_prime)))
            #print("\n")
            if prime_num_check(m_prime) == 1:
                m_prime_list.append(m_prime)
                count += 1
                #print(m_prime)
                print("   {}                      {}                      {}".format(count, natural_numbers, m_prime))


        pos += 1


    if count == user_in:
        print("------------------------------------------------------------")
        print("------------------------------------------------------------")
        print("\n")
        print("The Mersenne prime at "+str(user_in)+" is "+str(m_prime_list.pop()))
        print("*************************************************************")
        break


    natural_numbers += 1













