from flashcard import Flashcard, FlashcardDeck;
from storage import Storage;
import os;
import time;
def main(): 
    os.system('clear')
    print("Welcome to Flashcard App\n")
    time.sleep(2)
    while True:
        # Main menu
        os.system('clear')
        print("Main Menu")
        print("1. Create a new deck")
        print("2. Load a deck")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            deck_name = input("\nEnter a name for the deck: ")
            print("Creating deck...")
            time.sleep(2)

            if Storage.create_deck(deck_name):
                deck = FlashcardDeck()
                time.sleep(3)
                actions_menu(deck, deck_name)
            else:
                print("Deck creation failed")
                time.sleep(3)
        
        elif choice == "2":
            deck_name = input("\nEnter the name of the flashcard deck you wish to load: ")
            deck = FlashcardDeck()

            items = Storage.load(deck_name)
            for item in items:
                deck.add_flashcard(item)
            actions_menu(deck, deck_name)

        elif choice == "3":
            break   

        else:
            print("Invalid choice")
            input("\nPress enter to continue")



def actions_menu(deck, deck_name):
    while True:
        os.system('clear')
        print("Actions Menu")
        print("1. Add a flashcard")
        print("2. Delete a flashcard")      
        print("3. Learn and study your flashcards")
        print("4. Test yourself, take a quiz")
        print("5. Display all flashcards")
        print("6. Go to Main Menu")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            question = input("\nEnter the question: ")
            answer = input("\nEnter the answer: ")
            new_flashcard = Flashcard(question, answer)
            deck.add_flashcard(new_flashcard)
            Storage.save(new_flashcard, deck_name)
            time.sleep(3)
            

        
        elif choice == "2":
            index = int(input("\nEnter the index of the flashcard you want to delete: "))
            if index > 0 or index <= deck.get_flashcard_count():
                deck.delete_flashcard(index-1)
                Storage.delete(index, deck_name)
                time.sleep(3)

            else:
                print("Invalid index")
                time.sleep(3)
                
        
        elif choice == "3":
            os.system('clear')
            deck.learn()
            input("\nPress enter to continue")


        elif choice == "4": 
            os.system('clear')    
            deck.test()
            input("\nPress enter to continue")

        elif choice == "5":
            os.system('clear')
            deck.display_deck()
            input("\nPress enter to continue")
        

        elif choice == "6":
            print("\nExiting...")
            time.sleep(2)
            os.system('clear')
            break   

        else:
            print("Invalid choice")
            input("\nPress enter to continue")

if __name__ == "__main__":
    main()