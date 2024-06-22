def temp_conversion():
    try:
        f = input("What temperature is it in degrees Fahrenheit?: ")
        if f.lower() == "thirty":
            raise ValueError("Please enter a numeric value")
    
        f_input = int(f)
        c = (f_input - 32) * 5 /9

    except ValueError as ve:
        print(f"Error: {ve}")

    else:
        print(f"{f_input} degrees Fahrenheit is equal to {c:.2f} degrees celsius." )
    
    finally:
        print("Thank you for using the Excpetional Weather Forcast App")
    

temp_conversion()

  