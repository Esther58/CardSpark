class Storage:
    #create a new file for flashcards
    def create_deck(filename):
        filename = filename + ".txt"
        try:
            with open(filename, 'x') as f:
                print("Deck created successfully")
                f.close()
                return True
        except FileExistsError: 
            print("File already exists")
            return False
            


    #save the flashcard to a file
    def save(flashcard, filename):
        filename = filename + ".txt"
        f = open(filename, 'a')
        f.write("Q: " + flashcard.question + " A: " + flashcard.answer)
        f.write("\n")
        f.close
        print("Flashcards saved successfully")
        
    
    #delete a flashcard from a file
    def delete(index, filename):
        from flashcard import FlashcardDeck
        filename = filename + ".txt"
        try:
            with open (filename, 'r') as f:
                lines = f.readlines()
                ptr = 1
                with open (filename, 'w') as fw:
                    for line in lines:
                        if ptr != index:
                            fw.write(line)
                        ptr += 1
            f.close()
        except:
            print("Error Could not delete flashcard from file")



    #load the flashcards from a file into a list
    def load(filename):
        from flashcard import Flashcard;
        filename = filename + ".txt"
        flashcards = []

        try:
            with open(filename, 'r') as f:
                for line in f:
                    #remove any whitespace
                    line = line.strip()
                    #check if the line starts with Q: and has A: in it
                    if (line.startswith("Q:") and "A:" in line):
                        divider = line.split("A:")
                        q = divider[0].split("Q:")[1]
                        a = divider[1]
                        q = q.strip(" ")
                        a = a.strip(" ")
                        flashcards.append(Flashcard(q,a))
                    
                    else:
                        print("Invalid flashcard format")
                        break
            print("Flashcards loaded successfully")
            f.close()
        except FileNotFoundError:
            print("File not found")    

        return flashcards
    
   