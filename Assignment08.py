# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Ethan Morgan,8/31/2021,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #


# Data Start ------------------------------------------------------------- #
strFileName = 'products_name_price.txt'
ListTable = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Ethan Morgan,08/31/2021,Modified code to complete assignment 8
    """

    def __init__(self, product_name: str, product_price: float):
        self.__product_name = ""
        self.__product_price = ""
        try:
            self.product_name = str(product_name)
            self.product_price = float(product_price)
        except Exception as e:
            raise Exception("Error")

    def __str__(self):
        return self.product_name+","+str(self.product_price)

    @property # Setter for Product Name
    def product_name(self):
        return str(self.__product_name)

    @product_name.setter # Getter for Product Name
    def product_name(self, value: str):
        self.__product_name = str(value)

    @property # Setter for Product Price
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter # Getter for Product Price, Warning if the User doesn't enter a float value
    def product_price(self, value: float):
        try:
            self.__product_price = float(value)
        except ValueError:
            raise Exception("User must enter a number for the price.")
# Data End ---------------------------------------------------------------- #


# Processing Start -------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Ethan Morgan,08/31/2021,Modified code to complete assignment 8
    """

    @staticmethod
    def file_read(FileName: str):
        List_Table = []
        file = open(FileName, "r")
        for row in file:
            ListData = row.split(",")
            ListRow = Product(ListData[0], ListData[1])
            List_Table.append(ListRow)
        file.close()
        print()
        print("Previous data file exists and data is uploaded.")
        return List_Table

    def file_save(FileName: str, ListRows: list):
        file = open(FileName,"w")
        for row in ListRows:
            file.write(row.__str__() + "\n")
        print()
        print("File is saved.")

    # Attempted to create a file but was getting an error when there wasn't
    #   a file already existing with data in it. This program requires a
    #   text file with the proper name in order to run.
    #def file_create(FileName: str):
    #    List_Table = []
    #    ListRow = [0,0]
    #    file = open(FileName,"w")
    #    #ListRow = Product(ListTable[0]=="", ListTable[1]=="")
    #    List_Table.append(ListRow)
    #    file.close()
    #    print()
    #    print("File is created.")
# Processing End----------------------------------------------------------- #


# Presentation (Input/Output) Start --------------------------------------- #
class IO:
    @staticmethod
    def print_menu():
        print("""
            Product Name/Price Menu:
            [1] - Show Existing/Current Data
            [2] - Add Product Name/Price to Existing Data
            [3] - Save Current Data
            [4] - Quit The Program
            """)

    @staticmethod
    def input_menu():
        MenuOption = str(input("Menu #: ").strip())
        return MenuOption

    @staticmethod
    def print_list(input_list: list):
        if len(input_list) != 0:
            print("The Current List Has: ")
            for row in input_list:
                print(row.product_name+","+str(row.product_price))
        else:
            print()
            print("Please add some data using Option [2]!")

    @staticmethod
    def input_data():
        ProductName_Input = str(input("Product Name: ").strip())
        while True:
            try:
                ProductPrice_Input = float(input("Product Price: ").strip())
                if type(ProductPrice_Input) == float:
                    Product_Name_Price = Product(product_name=ProductName_Input,product_price=ProductPrice_Input)
                    return Product_Name_Price
                else:
                    continue
            except ValueError:
                print("Please enter a numeric value for the price.")
# Presentation (Input/Output) End ----------------------------------------- #

# Main Body of Script Start ----------------------------------------------- #
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program

# Refer to file_create fucntion definition for issue description
#try:
ListTable = FileProcessor.file_read(strFileName) # Command to Read Existing File
#except:
#    print()
#    print("File does not exist, therefore a file will be created.")
#    ListTable = FileProcessor.file_create(strFileName) # Command to Create File if it Doesn't Exist

while True: # Use 'while' Loop to Continue Asking for User Input
    IO.print_menu() # Print Menu for Selection
    UserInput = IO.input_menu() # Take in User Input from Menu Selection

    if UserInput == "1": # Show Existing/Current Data
        try:
            IO.print_list(ListTable) # Print the data to screen
        except:
            print()
            print("There is nothing in the list yet, please use Option [2] to add things to the list.")
        continue

    elif UserInput == "2": # Add Product Name/Price to Existing Data
        ListTable.append(IO.input_data())

    elif UserInput == "3": # Save Current Data
        try:
            FileProcessor.file_save(strFileName, ListTable)
        except:
            print()
            print("No data was added please add something first.")
        continue

    elif UserInput == "4": # Quit the Program
        print()
        print("You are exiting the program.")
        break

    else:
        print()
        print("Please enter Option [1], [2], [3], or [4]")
# Main Body of Script End ------------------------------------------------- #