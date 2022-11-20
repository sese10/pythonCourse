def calculate_SI_interest(amount, year, rate):
    #Interest = (amount x year x rate)/100
    result = (amount * year * rate) / 100
    print('The Interest is', result)
    return result



calculate_SI_interest(5000,3,2.3)