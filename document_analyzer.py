# document_analyzer.py - Your first working tool
# Run this with: python document_analyzer.py

def analyze_text(text):
    """Take text, return statistics"""
    # Split into words (split on whitespace)
    words = text.split()
    word_count = len(words)
    
    # Count characters (including spaces)
    char_count = len(text)
    
    # Count sentences (rough - look for periods)
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    
    return {
        'words': word_count,
        'characters': char_count,
        'sentences': sentence_count,
        'avg_word_length': char_count / word_count if word_count > 0 else 0
    }

def read_file(filename):
    """Try to open and read a file"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: Cannot find {filename}")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
