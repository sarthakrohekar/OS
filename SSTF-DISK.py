def sstfdisk_scheduling():
    n=int(input("Enter the number of requests:"))
    request_list=[]

    for i in range(n):
        request=int(input(f"Enter request {i+1}:"))
        request_list.append(request)

    head=int(input("Enter the initial head position:"))

    seek_sequence=[head]
    total_seek_time=0
    remaining_requests_list=request_list.copy()

    while remaining_requests_list:
        min_seek_time=float('inf')
        closest_request=None

        for request in remaining_requests_list:
            seek_time=abs(request-head)
            if seek_time<min_seek_time:
                min_seek_time=seek_time
                closest_request=request
        
        seek_sequence.append(closest_request)
        total_seek_time=total_seek_time+min_seek_time
        head=closest_request

        remaining_requests_list.remove(closest_request)
    
    print("\nSeek Sequence")
    for seq in seek_sequence:
        print(seq)
    print("Total Seek Time:"+str(total_seek_time))

sstfdisk_scheduling()