import sys
from stats import count_words,sort_on,alpha_count,dlist   


def get_book_text(file):
    with open(file) as f:
        contents=f.read()
    return contents


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book=sys.argv[1]
    
    readit=get_book_text(book)
    wc=count_words(readit)
        
    a_dict=alpha_count(readit)
    new_list=dlist(a_dict)
    
    new_list.sort(reverse=True,key=sort_on)
    
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print(f"----------- Word Count ----------")
    print(f"Found {wc} total words")
    print(f"--------- Character Count -------")
    for b in new_list:
        print(f"{b['char']}: {b['count']}")
    print(f"============= END ===============")

if __name__ == "__main__":
    main()
