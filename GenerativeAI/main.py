import generativeAIimplementation as gai
import googleSearcher as gs
import grammarImproviser as gi

def main():
    while True:
        print("Welcome to the Generative AI program!")
        print("Please enter a sentence to start with:")
        sentence = input()
        if sentence == "exit":
            break
        corrected_sentence = gi.correct_sentence(sentence)
        print(f"Maybe you meant: {corrected_sentence}")
        tobepassed = gs.perform_search(corrected_sentence)
        print(tobepassed)
        print(type(tobepassed))
        print(gi.correct_sentence(gai.generate_text(tobepassed)))

if __name__ == "__main__":
    main()