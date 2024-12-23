def fifo_page_replacement(pages,capactity):
    memory=[]
    page_fault=0

    for page in pages:
        if page not in memory:
            if len(memory)<capacity:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            page_fault=page_fault+1
        print("Page:"+str(page)+"->"+"Memory"+str(memory))
    print("Total page faults:"+str(page_fault))

def lru_page_replacement(pages,capacity):
    memory=[]
    page_fault=0

    for page in pages:
        if page not in memory:
            if len(memory)<capacity:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            page_fault=page_fault+1
        else:
            memory.remove(page)
            memory.append(page)
        print("Page:"+str(page)+"->"+"Memory"+str(memory))
    print("Total page faults:"+str(page_fault))

def optimal_page_replacement(pages, capacity):
    memory = []  # Current pages in memory
    page_faults = 0

    for i in range(len(pages)):
        page = pages[i]
        if page not in memory:
            if len(memory) < capacity:
                memory.append(page)  # Add page if memory is not full
            else:
                # Determine the optimal page to replace
                future_uses = []
                for p in memory:
                    if p in pages[i+1:]:
                        future_uses.append(pages[i+1:].index(p))
                    else:
                        future_uses.append(float('inf'))
                # Replace the page with the farthest future use
                replace_index = future_uses.index(max(future_uses))
                memory[replace_index] = page

            page_faults += 1  # Page fault occurs
        print(f"Page: {page} -> Memory: {memory}")

    print(f"Total Page Faults (Optimal): {page_faults}\n")


pages = list(map(int, input("Enter the page reference sequence (space-separated): ").split()))
capacity = int(input("Enter the memory capacity: "))

print("\nFIFO Page Replacement:")
fifo_page_replacement(pages, capacity)

print("\nLRU Page Replacement:")
lru_page_replacement(pages, capacity)

print("\nOptimal Page Replacement:")
optimal_page_replacement(pages, capacity)

#7 0 1 2 0 3 0 4 2 3 0 3 2
#3