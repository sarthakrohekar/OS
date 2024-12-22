def fcfs_scheduling():
    n=int(input("Enter the number of processes:"))
    processes=[] #A list to hold the processes

    for i in range(n):
        print(f"\nProcess {i+1}:")
        pid=i+1
        arrival_time=int(input("Arrival Time:"))
        burst_time=int(input("Burst Time:"))

        processes.append((pid,arrival_time,burst_time))#adding processes and its detail to the list
    print(processes)

    processes_restructure=[(arrival_time,pid,burst_time) for pid,arrival_time,burst_time in processes]#restructuring the elements of list to sort the list based on arrival time
    print(processes_restructure)#print the restructured list

    processes_restructure.sort()#sorting the list based on their arrval time
    print(processes_restructure)#print the sorted list in order of their arrival

    processes_sorted=[(pid,arrival_time,burst_time) for arrival_time,pid,burst_time in processes_restructure]#restoring the original structure of the sorted list(pid,AT,BT)
    print(processes_sorted)
    
    Current_time=0
    gantt_chart=[]
    completion_time_list=[]
    waiting_time_list=[]
    turnaround_time_list=[]

    for pid,arrival_time,burst_time in processes_sorted:
        if Current_time<arrival_time:
            Current_time=arrival_time
        start_time=Current_time
        Current_time=Current_time+burst_time
        gantt_chart.append((pid,start_time,Current_time))

        completion_time=Current_time
        turnaround_time=completion_time-arrival_time
        waiting_time=turnaround_time-burst_time

        completion_time_list.append(completion_time)
        turnaround_time_list.append(turnaround_time)
        waiting_time_list.append(waiting_time)
    
    print("\nGantt  Chart:")
    for pid,start_time,Current_time in gantt_chart:
        print(f"P{pid} [{start_time}-{Current_time}]",end="")
    print("\n")

    # Print headers
    print(f"{'Process':<10}{'Arrival Time':<15}{'Burst Time':<15}{'Completion Time':<20}{'Turnaround Time':<20}{'Waiting Time':<15}")

    # Print each process details with proper alignment
    for i, (pid, arrival_time, burst_time) in enumerate(processes_sorted):
        print(f"P{pid:<8}{arrival_time:<15}{burst_time:<15}{completion_time_list[i]:<20}{turnaround_time_list[i]:<20}{waiting_time_list[i]:<15}")


    avg_turnaround_time=sum(turnaround_time_list)/n
    avg_waiting_time=sum(waiting_time_list)/n
    print("Average Turnaround Time:"+str(avg_turnaround_time))
    print("Average Waiting Time:"+str(avg_waiting_time))


fcfs_scheduling()