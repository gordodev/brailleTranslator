# brailleTranslator
Convert text string to binary braille in ASCII (like: 11001100110000)

---

# Braille Converter in Python  

## Overview  
This project is a **Braille Converter** written in Python that translates English text into Braille binary encoding. It was developed as part of a **Google Foobar Challenge**, an invite-only coding test that Google sends to select developers based on their programming-related search history.  

I received this challenge after searching for Python-related topics, and I was prompted to solve it as part of Google’s **hidden talent identification process**. The test required converting text into Braille while handling uppercase letters correctly.

Note: This was completed as part of a timed challenge, where the focus was on quickly implementing a working solution rather than adding finishing touches like exception handling, logging, or extensive optimizations. The goal was to complete the core functionality within the given time limit.

## Features  
- Converts **English text** to **Braille binary encoding**  
- Handles **uppercase letters** by prefixing them with `000001`  
- Supports **spaces** with `000000`  
- Uses a **dictionary-based lookup** for fast encoding  

## How It Works  
1. The script defines a **Braille dictionary** that maps lowercase letters and spaces to Braille binary.  
2. If an uppercase letter is detected, it is prefixed with `000001` before conversion.  
3. The user enters a word or phrase, and the program outputs the corresponding **Braille representation**.  

## Example Usage  
```bash
$ python3 braille_converter.py
enter word:
Hello
000001100010000001101110100010101010
```

## Installation & Running  
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/braille-converter.git
   ```
2. Navigate to the project folder:  
   ```bash
   cd braille-converter
   ```
3. Run the script:  
   ```bash
   python3 braille_converter.py
   ```

## Future Enhancements  
- Support for **numbers** and **punctuation**  
- GUI or **Web-based interface** for easier interaction  

## Why This Project?  
This project was developed as part of the **Google Foobar Challenge**, demonstrating problem-solving skills, algorithmic thinking, and Python proficiency. It showcases my ability to tackle real-world coding challenges efficiently.  
