import sqlite3

conn = sqlite3.connect('LevinEmployee.db')
import seaborn
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats

from pylab import savefig



def statsMenu():
    while True:
        

        print("\n1. Red")
        print("2. White")
        print("3. Main Menu")
        
        userChoice = input("Please select your wine preference: ")

                
        if userChoice == "1":
            wineColor = "red"
        elif userChoice == "2":
            wineColor = "white"
        elif userChoice == "3":
            break
        else:
            print("\nInvalid choice, please try again")
            continue
            
        while True:
            print("\n1. Residual Sugar")
            print("2. Volatile Acidity")
            print("3. Alcohol Percent")
            print("4. Fixed Acidity")
            print("5. Previous Menu")
            
            userChoice = input("Please select a value to test: ")
                
            if userChoice  == "1":
                wineTest("residual sugar", wineColor)
            elif userChoice == "2":
                wineTest("volatile acidity", wineColor)
            elif userChoice == "3":
                wineTest("alcohol", wineColor)
            elif userChoice == "4":
                wineTest("fixed acidity", wineColor)
            elif userChoice == "5":
                break
            else:
                print("\nWrong Input\n")
    
    
def wineTest(value, color):
    try:
        WineChar = value
        
        WineChar2 = "quality"
        
        if value == "alcohol":
            value += " percentage"
                
        allWines = pd.read_csv('winequality-both.csv')
        
        wine = allWines.loc[allWines['type'] == color, :]
         

        while True:
            try:
                print ("\nThe ranges for " + value + " are:\n")
                print ("Min: " + str(wine[WineChar].min()) + "\tMax: " + str(wine[WineChar].max()))   
                WineCharValue = float(input("Please select a numerical value to test: "))            

            except:
                print("\nI'm sorry, the input must be a number within the dataset")
                continue
            
            RedResidualSugar = wine.loc[wine[WineChar] == WineCharValue, :]
            
            if RedResidualSugar.empty:
                print("\nI'm sorry, I couldn't find anything, please try again")
            else:
                break
        
        WineCharValueDataset = RedResidualSugar.loc[:,WineChar2]
        
        if (WineCharValueDataset.size) == 1:
            plt.hist(WineCharValueDataset, bins = 10)
            plt.title(value + " value " + str(WineCharValue) + " frequencies by " + WineChar2)

            plt.xlabel(WineChar2)
            plt.ylabel('Number of wines')
            plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            plt.show()
        else:
            seaborn.distplot(WineCharValueDataset, bins = 10, kde = False)
            
            plt.title(value + " value " + str(WineCharValue) + " frequencies by " + WineChar2)
            plt.ylabel('Number of wines')
            
            plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            plt.show()
    
    except (KeyError, ZeroDivisionError) as e:
        print(e)
        
def wineStats():

    WineCharX = "quality"
    allWines = pd.read_csv('winequality-both.csv')
    red = allWines.loc[allWines['type']=='red',:]
    white = allWines.loc[allWines['type']=='white',:]
    
    while True:
        print("\nWine Stats:\n")
        
        print("1. Red Wine")
        print("2. White Wine")
        print("3. Previous Menu")
        
        userinput = input("Please select an option: ")
        
        if userinput == "1":
            while True:
                print("\nWhat would you like to compare to red wine quality?\n")
                print("1. Volatile Acidity")
                print("2. Fixed Acidity")
                print("3. Alcohol Percent")
                print("4. Residual Sugar")
                print("5. Chlorides")
                print("6. Sulphates")
                print("7. pH")
                print("8. Previous Menu")
                

                userinput2 = input("Please select an option: ")
            
                if userinput2 == "1":
                    try:
                        WineCharY = "volatile acidity"               
                        getCorr = scipy.stats.spearmanr(red[WineCharX], red[WineCharY])
                        correlation = str(getCorr[0])
                        pValue = str(getCorr[1])
                        print("\nThe correlation between " +WineCharX + " and " + WineCharY + " is: " + correlation + " with a p value of: " + pValue)
                        seaborn.lmplot(x=WineCharX, y=WineCharY, data= red)
                        plt.xlabel(WineCharX)
                        plt.ylabel(WineCharY)
                        plt.title("Red Wine: " + WineCharX + " X " + WineCharY)
                        plt.show()
                        savefig("scatterplot1.png")
                        
                    except (KeyError) as e:
                        print ("Sorry, please try again")
                
                elif userinput2 == "2":
                    try:
                        WineCharY = "fixed acidity"
                        getCorr = scipy.stats.spearmanr(red[WineCharX], red[WineCharY])
                        correlation = str(getCorr[0])
                        pValue = str(getCorr[1])     
                        print("\nThe correlation between " +WineCharX + " and " + WineCharY + " is: " + correlation + " with a p value of: " + pValue)
                        seaborn.lmplot(x=WineCharX, y=WineCharY, data= red)
                        plt.xlabel(WineCharX)
                        plt.ylabel(WineCharY)
                        plt.title("Red Wine: " + WineCharX + " X " + WineCharY)
                        plt.show()
                        savefig("scatterplot3.png")
                        
                    except (KeyError) as e:
                        print ("Sorry, please try again")
                
                elif userinput2 == "3":
                    try:
                        WineCharY = "alcohol"
                        getCorr = scipy.stats.spearmanr(red[WineCharX], red[WineCharY])
                        correlation = str(getCorr[0])
                        pValue = str(getCorr[1])
                        print("\nThe correlation between " +WineCharX + " and " + WineCharY + " is: " + correlation + " with a p value of: " + pValue)
                        seaborn.lmplot(x=WineCharX, y=WineCharY, data= red)
                        plt.xlabel(WineCharX)
                        plt.ylabel(WineCharY + "percentage")
                        plt.title("Red Wine: " + WineCharX + " X " + WineCharY + " percentage")
                        plt.show()
                        savefig("scatterplot5.png")
                        
                    except (KeyError) as e:
                        print ("Sorry, please try again")
                        
                elif userinput2 == "4":
                    try:
                        WineCharY = "residual sugar"
                        getCorr = scipy.stats.spearmanr(red[WineCharX], red[WineCharY])
                        correlation = str(getCorr[0])
                        pValue = str(getCorr[1])       
                        print("\nThe correlation between " +WineCharX + " and " + WineCharY + " is: " + correlation + " with a p value of: " + pValue)
                        seaborn.lmplot(x=WineCharX, y=WineCharY, data= red)
                        plt.xlabel(WineCharX)
                        plt.ylabel(WineCharY)
                        plt.title("Red Wine: " + WineCharX + " X " + WineCharY)
                        plt.show()
                        savefig("scatterplot7.png")
                        
                    except (KeyError) as e:
                        print ("Sorry, please try again")
                
                elif userinput2 == "5":
                    try:
                        WineCharY = "chlorides"
                        getCorr = scipy.stats.spearmanr(red[WineCharX], red[WineCharY])
                        correlation = str(getCorr[0])
                        pValue = str(getCorr[1])       
                        print("\nThe correlation between " +WineCharX + " and " + WineCharY + " is: " + correlation + " with a p value of: " + pValue)
                        seaborn.lmplot(x=WineCharX, y=WineCharY, data= red)
                        plt.xlabel(WineCharX)
                        plt.ylabel(WineCharY)
                        plt.title("Red Wine: " + WineCharX + " X " + WineCharY)
                        plt.show()
                        savefig("scatterplot9.png")
                        
                    except (KeyError) as e:
                        print ("Sorry, please try again")
                
                
                elif userinput2 == "6":
                    try:
                        WineCharY = "sulphates"
                        getCorr = scipy.stats.spearmanr(red[WineCharX], red[WineCharY])
                        correlation = str(getCorr[0])
                        pValue = str(getCorr[1])       
                        print("\nThe correlation between " +WineCharX + " and " + WineCharY + " is: " + correlation + " with a p value of: " + pValue)
                        seaborn.lmplot(x=WineCharX, y=WineCharY, data= red)
                        plt.xlabel(WineCharX)
                        plt.ylabel(WineCharY)
                        plt.title("Red Wine: " + WineCharX + " X " + WineCharY)
                        plt.show()
                        savefig("scatterplot11.png")
                        
                    except (KeyError) as e:
                        print ("Sorry, please try again")
                
                elif userinput2 == "7":
                    try:
                        WineCharY = "pH"
                        getCorr = scipy.stats.spearmanr(red[WineCharX], red[WineCharY])
                        correlation = str(getCorr[0])
                        pValue = str(getCorr[1])       
                        print("\nThe correlation between " +WineCharX + " and " + WineCharY + " is: " + correlation + " with a p value of: " + pValue)
                        seaborn.lmplot(x=WineCharX, y=WineCharY, data= red)
                        plt.xlabel(WineCharX)
                        plt.ylabel(WineCharY)
                        plt.title("Red Wine: " + WineCharX + " X " + WineCharY)
                        plt.show()
                        savefig("scatterplot13.png")
                        
                    except (KeyError) as e:
                        print ("Sorry, please try again")
                
                elif userinput2 == "8":
                    break
                else:
                    print("\nInvalid input, please try again\n")
        elif userinput == "2":
            
            while True:
                print("\nWhat would you like to compare to white wine quality?\n")
                print("1. Volatile Acidity")
                print("2. Fixed Acidity")
                print("3. Alcohol Percent")
                print("4. Residual Sugar")
                print("5. Chlorides")
                print("6. Sulphates")
                print("7. pH")
                print("8. Previous Menu")
                
                userinput2 = input("Please select an option: ")
                
                if userinput2 == "1":
                    try:
                        WineCharY = "volatile acidity"
                        getCorr = scipy.stats.spearmanr(white[WineCharX], white[WineCharY])
                        correlation = str(getCorr[0])
                        pValue = str(getCorr[1])
                        print("\nThe correlation between " +WineCharX + " and " + WineCharY + " is: " + correlation + " with a p value of: " + pValue)
                        seaborn.lmplot(x=WineCharX, y=WineCharY, data= white)
                        plt.xlabel(WineCharX)
                        plt.ylabel(WineCharY)
                        plt.title("White Wine: " + WineCharX + " X " + WineCharY)
                        plt.show()
                        savefig("scatterplot2.png")
                    except (KeyError) as e:
                        print ("Sorry, please try again")
                elif userinput2 == "2":
                    try:
                        WineCharY = "fixed acidity"
                        getCorr = scipy.stats.spearmanr(white[WineCharX], white[WineCharY])
                        correlation = str(getCorr[0])
                        pValue = str(getCorr[1])
                        print("\nThe correlation between " +WineCharX + " and " + WineCharY + " is: " + correlation + " with a p value of: " + pValue)
                        seaborn.lmplot(x=WineCharX, y=WineCharY, data= white)
                        plt.xlabel(WineCharX)
                        plt.ylabel(WineCharY)
                        plt.title("White Wine: " + WineCharX + " X " + WineCharY) 
                        plt.show()
                        savefig("scatterplot4.png")
                    except (KeyError) as e:
                        print ("Sorry, please try again")
                elif userinput2 == "3":
                    try:
                        WineCharY = "alcohol"
                        getCorr = scipy.stats.spearmanr(white[WineCharX], white[WineCharY])
                        correlation = str(getCorr[0])
                        pValue = str(getCorr[1])
                        print("\nThe correlation between " +WineCharX + " and " + WineCharY + " is: " + correlation + " with a p value of: " + pValue)
                        seaborn.lmplot(x=WineCharX, y=WineCharY, data= white)
                        plt.xlabel(WineCharX)
                        plt.ylabel(WineCharY + "percentage")
                        plt.title("White Wine: " + WineCharX + " X " + WineCharY + " percentage")
                        plt.show()
                        savefig("scatterplot6.png")
                    except (KeyError) as e:
                        print ("Sorry, please try again")
                elif userinput2 == "4":
                    try: 
                        WineCharY = "residual sugar"
                        getCorr = scipy.stats.spearmanr(white[WineCharX], white[WineCharY])
                        correlation = str(getCorr[0])
                        pValue = str(getCorr[1])
                        print("\nThe correlation between " +WineCharX + " and " + WineCharY + " is: " + correlation + " with a p value of: " + pValue)
                        seaborn.lmplot(x=WineCharX, y=WineCharY, data= white)
                        plt.xlabel(WineCharX)
                        plt.ylabel(WineCharY)
                        plt.title("White Wine: " + WineCharX + " X " + WineCharY)
                        plt.show()
                        savefig("scatterplot8.png")

                    except (KeyError) as e:
                        print ("Sorry, please try again")
                
                elif userinput2 == "5":
                    try: 
                        WineCharY = "chlorides"
                        getCorr = scipy.stats.spearmanr(white[WineCharX], white[WineCharY])
                        correlation = str(getCorr[0])
                        pValue = str(getCorr[1])
                        print("\nThe correlation between " +WineCharX + " and " + WineCharY + " is: " + correlation + " with a p value of: " + pValue)
                        seaborn.lmplot(x=WineCharX, y=WineCharY, data= white)
                        plt.xlabel(WineCharX)
                        plt.ylabel(WineCharY)
                        plt.title("White Wine: " + WineCharX + " X " + WineCharY)
                        plt.show()
                        savefig("scatterplot10.png")

                    except (KeyError) as e:
                        print ("Sorry, please try again")
                        
                elif userinput2 == "6":
                    try: 
                        WineCharY = "sulphates"
                        getCorr = scipy.stats.spearmanr(white[WineCharX], white[WineCharY])
                        correlation = str(getCorr[0])
                        pValue = str(getCorr[1])
                        print("\nThe correlation between " +WineCharX + " and " + WineCharY + " is: " + correlation + " with a p value of: " + pValue)
                        seaborn.lmplot(x=WineCharX, y=WineCharY, data= white)
                        plt.xlabel(WineCharX)
                        plt.ylabel(WineCharY)
                        plt.title("White Wine: " + WineCharX + " X " + WineCharY)
                        plt.show()
                        savefig("scatterplot12.png")

                    except (KeyError) as e:
                        print ("Sorry, please try again")
                
                elif userinput2 == "7":
                    try: 
                        WineCharY = "pH"
                        getCorr = scipy.stats.spearmanr(white[WineCharX], white[WineCharY])
                        correlation = str(getCorr[0])
                        pValue = str(getCorr[1])
                        print("\nThe correlation between " +WineCharX + " and " + WineCharY + " is: " + correlation + " with a p value of: " + pValue)
                        seaborn.lmplot(x=WineCharX, y=WineCharY, data= white)
                        plt.xlabel(WineCharX)
                        plt.ylabel(WineCharY)
                        plt.title("White Wine: " + WineCharX + " X " + WineCharY)
                        plt.show()
                        savefig("scatterplot14.png")

                    except (KeyError) as e:
                        print ("Sorry, please try again")
                        
                elif userinput2 == "8":
                    break
                else:
                    print("Invalid input\n")
        elif userinput == "3":
            break
        else:
            print("Invalid Input\n")
            
def login():
    with conn:
        
        cur = conn.cursor()
        
        while True:
            
            try:
                email = input("Email: ")
                password = input("Password: ")
                
                cur.execute("SELECT COUNT(EmployeeID) FROM Employee WHERE Email = '" + email + "' AND Password = '" + password + "';")
                
                count = cur.fetchone()
                
                if email == "" and password == "":
                    print("No email or password entered")
                elif email == "":
                    print("No email entereed")
                elif password == "":
                    print("No password entered")
                elif count[0] == 0:
                    print("\nSorry, we couldn't find that account ;(") 
                    wrong_entry = input("\n1) Try again?\n2) Return to previous menu\n\n")
                    if wrong_entry == "1":
                        pass
                    else:
                        return False
                    
                else:
                    print("\nThanks for logging in!\n") 
                    return True
                 
            except:
                print("Connection Failed")

def employee_id():
    while True:
        ID = input("Please enter your Employee ID: ").strip()
        
        while not ID:
            ID = input("Employee ID cannot be blank: ").strip()
        
        with conn:
            cur = conn.cursor()
        
            try:
                
                cur.execute("SELECT COUNT(*) FROM Employee WHERE (EmployeeID = '" + ID + "')")
                
                results = cur.fetchone()
                
                while results[0] == 1:
                    ID = input("Emoloyee ID already in use. Please enter a new one: ").strip()
                    cur.execute("SELECT COUNT(*) FROM Employee WHERE EmployeeID = '" + ID + "'")
                    results = cur.fetchone()
                
                print("\nEmployee ID " + ID + " accepted, thank you")
                return ID
            
            except sqlite3.Error as e:
                print (e)
    
def additional():
    while True:
        print("\n1. Food Pairings")
        print("2. Most Popular Wines")
        print("3. Calorie Counter")
        print("0. Previous Menu\n")
        
        add = input("Please select an option: ")
        if add == "1":
            wine = input("Wine Preference? ('red' or 'white') ")
            if wine == "red":
                print("\nThese are the top 5 food pairings for red wine:\n")
                print("1. Rich Fish")
                print("2. White Meat")
                print("3. Red Meat")
                print("4. Cured Meat")
                print("5. Desserts")
                print("----------------")                
            elif wine == "white":
                print("\nThese are the top 5 food pairings for white wine:\n")
                print("1. Curry")
                print("2. Veggies")
                print("3. Cheese")
                print("4. Seafood")
                print("5. Starches")
                print("----------------")                
            else:
                print("\nSorry, please select 'red' or 'white'")                
        elif add == "2":
            popular = input("Wine Preference? ('red' or 'white') ")
            if popular == "red":
                print ("\nThese are the most popular red wines:\n")
                print("1. Syrah")
                print("2. Merlot")
                print("3. Cabernet Sauvignon")
                print("4. Zinfandel")
                print("5. Pinot Noir")   
                print("----------------")
            elif popular == "white":
                print ("\nThese are the most popular white wines:\n")
                print("1. Chardonnay")
                print("2. Sauvignon Blanc")
                print("3. Semillon")
                print("4. Moscato")
                print("5. Pinot Grigio")   
                print("----------------")    
            else:
                print("\nSorry, please select 'red' or 'white'")                                     
        elif add == "3":
            calorie = float(input("Please input an alcohol percentage: "))
            print("\nFor your average 4 oz. glass of wine, the amount of calories is:\n ")
            print(6.4*calorie)
        else:
            break
            
def register():
    with conn:
        
        print("\nOkay, I'm going to need a few things from you before you can be registered")
        ID = employee_id()
        
        firstName = input("First Name: ")
        lastName = input("Last Name: ")
        address = input("Address: ")
        city = input("City: ")
        state = input("State: ")
        zipCode = input("Zip Code: ")
        email = input("Email: ")
        password = input("Password: ")
    
        cur = conn.cursor()
        try:
            
            cur.execute("INSERT INTO Employee VALUES ('" + ID + "', '" + firstName + "', '" + lastName + "', '" + address \
                                                      + "', '" + city + "', '" + state + "', '" + zipCode + "', '" + email \
                                                      + "', '" + password + "')")
            
            cur.execute("SELECT * FROM Employee WHERE EmployeeID = '" + ID + "'")
            conn.commit()
            
            print("User inserted")
            
            results = cur.fetchone()
            
            print(results)
            
        except sqlite3.Error as e:
            print (e)
    
if __name__ == "__main__":
    
    loggedin = False
    while True:
        if loggedin:
            print("1. Register")
            print("2. View Wine Statistics")
            print("3. Wine Characteristic Analysis")
            print("4. View Additional Features")
            print("0. Exit")
                
            choice = input("Please select an option: ")
            
            if choice == "1":
                register()
            elif choice == "2":
                wineStats()
            elif choice == "3":
                statsMenu()
            elif choice == "4":
                additional()
            elif choice == "0":
                break
            else:
                print("\nSorry, I didn't recognize that option\n")
        
        else:
            print("\n========================") 
            print("Welcome to Le Vin Coupe!")
            print("========================\n")
            print("1. Login")
            print("0. Exit")
                    
            choice = input("Please select an option: ")
            
            if choice == "1":
                loggedin = login()
            elif choice == "0":
                print("\nAw, I'm sorry you have to go. Have a good day! :)")
                break
            else:
                print("\nSorry that wasn't an option, please try again")
        