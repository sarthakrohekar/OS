def cscandisk_scheduling():
    n=int(input("Enter the number of requests:"))
    request_list=[]

    for i in range(n):
        request=int(input(f"Enter request {i+1}:"))
        request_list.append(request)

    head=int(input("Enter the initial head position(0 to 200):"))
    
    seek_sequence=[head]
    total_seek_time=0

    request_list.sort()

    left_request_list=[req for req in request_list if req<head]
    right_request_list=[req for req in request_list if req>head]

    seek_sequence=seek_sequence+right_request_list
    seek_sequence.append(200)
    seek_sequence.append(0)
    seek_sequence=seek_sequence+left_request_list

    for i in range(1,len(seek_sequence)):
        total_seek_time=total_seek_time+abs(seek_sequence[i]-seek_sequence[i-1])

    print("\nSeek Sequence")
    for seq in seek_sequence:
        print(seq)
    print("Total seek time:"+str(total_seek_time))

cscandisk_scheduling()