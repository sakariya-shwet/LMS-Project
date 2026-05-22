print("<<<< Welcome To My Program :-- Function Treat >>>>")

print("\n Welcome To Data Analyzer And Transformer Program")

print("\n Main Menu:")
print("i.) Input Data")
print("ii.) Display Data Summary (built-in function)")
print("iii.) Calculate Factorial (Recursion)")
print("iv.) Filter Data by Threshold (lambda function)")
print("v.) Sort Data")
print("vi.) Display Dataset Statistics")
print("vii.) Exit program")

choice = input("\nEnter your choice: ")



if choice == "i":
    data = input("Enter data for a 1D array: ")
    
    print(data)
    print("\nData has been stored successfully!")

elif choice == "ii":

    data = input("Enter data first: ")
    data_str=str(data)

    print("\nYou've entered in DATA SUMMARY")

    total_elements = len(data_str)
    minimum_value = min(data_str)
    maximum_value = max(data_str)
    


    print("total_elements =", total_elements)
    print("minimum_value =", minimum_value)
    print("maximum_value =", maximum_value)
    

    
