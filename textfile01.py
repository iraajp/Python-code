def find_words_by_length(filename, lengths):
    words_by_length = {length: [] for length in lengths}
    try:
        with open(filename, 'r') as file:
            for line in file:
                for word in line.split():
                    word = word.strip('.,!?()"\'').lower()
                    if len(word) in lengths:
                        words_by_length[len(word)].append(word)
        return words_by_length
    except FileNotFoundError:
        return "File not found"

filename = input("Enter filename: ")
lengths = [int(x) for x in input("Enter word lengths (comma-separated): ").split(',')]
results = find_words_by_length(filename, lengths)

if isinstance(results, dict):
    for length, words in results.items():
        print(f"Words with {length} letters: {', '.join(words)}")
else:
    print(results)