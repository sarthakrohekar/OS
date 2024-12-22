def fcfsdisk_scheduling():
    n=int(input("Enter the number of requests:"))
    request_list=[]

    for i in range(n):
        request=int(input(f"Enter request {i+1}:"))
        request_list.append(request)

    head=int(input("Enter the initial head position:"))

    seek_sequence=[head]+request_list
    total_seek_time=0

    for i in range(len(request_list)):
        seek_time=abs(seek_sequence[i+1]-seek_sequence[i])
        total_seek_time=total_seek_time+seek_time
    
    print("Seek sequence:")
    for seq in seek_sequence:
        print(seq)
    print("Total Seek time:"+str(total_seek_time))

fcfsdisk_scheduling()