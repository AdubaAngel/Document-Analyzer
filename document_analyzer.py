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

def find_common_words(text, top_n=5):
    """Find the most frequent words in text"""
    # Convert to lowercase and split
    words = text.lower().split()
    
    # Remove common punctuation
    clean_words = []
    for word in words:
        # Remove . , ! ? ; : from ends of words
        clean_word = word.strip('.,!?;:()"\'')
        if clean_word:  # Only add if not empty
            clean_words.append(clean_word)
    
    # Count occurrences
    word_counts = {}
    for word in clean_words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    # Sort by count (highest first)
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Return top N
    return sorted_words[:top_n]

def save_results_to_file(filename, stats):
    with open(f"{filename}_analysis.txt", "w", encoding='utf-8') as newFile:
        newFile.write("=" * 40 + "\n") 
        newFile.write("ANALYSIS REPORT\n") 
        newFile.write("=" * 40 + "\n\n")   
        newFile.write(f"Words: {stats['words']}\n")
        newFile.write(f"Characters: {stats['characters']}\n")
        newFile.write(f"Sentences: {stats['sentences']}\n")
        newFile.write(f"Average word length: {stats['avg_word_length']:.2f} characters\n")
        newFile.write("=" * 40 + "\n") 
        newFile.write("REPORT FINALIZED\n") 
        newFile.write("=" * 40 + "\n\n")





def main():
    print("=" * 50)
    print("DOCUMENT ANALYZER - Version 0.1")
    print("=" * 50)
    
    # Ask user for filename
    filename = input("\nEnter the filename to analyze: ")
    
    # Read the file
    content = read_file(filename)
    
    if content is None:
        return
    
    # Analyze the content
    stats = analyze_text(content)
    
    # Display results
    print("\n" + "=" * 50)
    print("ANALYSIS RESULTS")
    print("=" * 50)
    print(f"Words: {stats['words']}")
    print(f"Characters: {stats['characters']}")
    print(f"Sentences: {stats['sentences']}")
    print(f"Average word length: {stats['avg_word_length']:.2f} characters")
    
    # Show first 200 characters as preview
    print("\n" + "=" * 50)
    print("PREVIEW (first 200 characters)")
    print("=" * 50)
    print(content[:200])
    if len(content) > 200:
        print("...")

    print("\n" + "=" * 50)
    print("MOST COMMON WORDS")
    print("=" * 50)
    common = find_common_words(content, 5)
    for word, count in common:
        # Skip very common words (stop words)
        if word not in ['the', 'and', 'to', 'of', 'a', 'in', 'is', 'it', 'for']:
            print(f"  '{word}' appears {count} times")
    
    # After your last print statement in main()
    ask_save = input("\nSave results to file? (yes/no): ")

    if ask_save.lower() == 'yes' or ask_save.lower() == 'y':
        save_results_to_file(filename, stats)
        print(f"✓ Results saved to {filename}_analysis.txt")
    else:
        print("Results not saved")

if __name__ == "__main__":
    main()