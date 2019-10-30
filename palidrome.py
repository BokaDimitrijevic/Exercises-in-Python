def palidrome(sentence):
    """Given a sequence, Check is it palidrome or not."""
    sentence = input("Enter a sentence:")
    s = sentence.replace (" ","").lower()
    if s[::-1] == s:
        print (f"Is '{s}' a palidrome? True")
    else:
        print ((f"Is '{s}' a palidrome? False"))
    
if __name__ == "__main__":
  palidrome("Hello")
 
            


       
