class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class FlashcardDeck:
    def __init__(self):
        self.flashcards = []; 

    #add a flashcard to the deck
    def add_flashcard(self, flashcard):
        self.flashcards.append(flashcard)
    
    #delete a flashcard at a specific index
    def delete_flashcard(self, index):
        if index < 0 or index > len(self.flashcards):
            print("Invalid index")
        
        elif len(self.flashcards) == 0:
            print("No flashcards to delete")

        else:
            self.flashcards.pop(index)
            print("Flashcard deleted successfully")
     

    #return the whole deck of flashcards
    def get_flashcards(self):
        return self.flashcards
    
    #return a specific flashcard at a specific index
    def get_flashcard(self, index):
        return self.flashcards[index]

    #return the number of flashcards in the deck
    def get_flashcard_count(self):
        return len(self.flashcards)

    #Learn the flashcards in the deck
    def learn(self):
        if len(self.flashcards) == 0:
            print("No flashcards to learn")
            return
        
        for flashcard in self.flashcards:
            print("Question: " + flashcard.question + "\n")
            input("Press enter to see the answer \n")
            print("Answer: " + flashcard.answer + "\n")
            input("Press enter to continue \n")

            
    #Test the user on the flashcards in the deck
    #User will be prompted to enter an answer for each question
    def test(self):
        if len(self.flashcards) == 0:
            print("No flashcards to test")
            return

        for flashcard in self.flashcards:
            print("Question: " + flashcard.question)
            answer = input("Enter your answer: ")
            if answer == flashcard.answer:
                print("\nCorrect")
            else:
                print("\nIncorrect, the answer is: " + flashcard.answer)
    
    #Display all flashcards in the deck
    def display_deck(self):
        if len(self.flashcards) == 0:
            print("No flashcards to display")
            return
        for flashcard in self.flashcards:
            print(f"Q: {flashcard.question}\nA: {flashcard.answer}\n") 
            print("\n")
        