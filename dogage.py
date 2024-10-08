def dog_age():
  
  while True:

    dog_years = float(input("Enter age: "))    
    if 0 < dog_years <= 2:
        dog_human = dog_years * 5.25
    else:
        dog_human = ((dog_years - 2) * 4) + 10.5


    print(f"Dog years is equal to {dog_human} ")

    user_input = input("Do you want to continue? (y/n): ")
    if user_input.lower() != 'y':
          break      
