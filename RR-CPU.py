from collections import deque

def rrscheduling():
    n=int(input("Enter the number of processes:"))
    time_quantum=int(input("Enter the time quantum:"))

    processes=[]
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

    remaining_burst = [bt for _, _, bt in processes]  # Remaining burst times
    completion_time = [0] * n  # Completion times
    waiting_time = [0] * n  # Waiting times
    turnaround_time = [0] * n  # Turnaround times
    gantt_chart = []  # Gantt chart to display execution order

    ready_queue=deque()
    current_time=0
    completed=0

    i=0
    while completed<n:
        while i<n and processes[i][1]<=current_time:
            ready_queue.append(i)
            i=i+1
        
        if ready_queue:
            idx=ready_queue.popleft()
            gantt_chart.append(processes[idx][0])

            if remaining_burst[idx]>time_quantum:
                current_time=current_time+time_quantum
                remaining_burst[idx]=remaining_burst[idx]-time_quantum
            else:
                current_time=current_time+remaining_burst[idx]
                remaining_burst[idx]=0
                completed=completed+1
                completion_time[idx]=current_time

            while i<n and processes[i][1]<=current_time:
                ready_queue.append(i)
                i=i+1

            if remaining_burst[idx]>0:
                ready_queue.append(idx)
        
        else:
            current_time=current_time+1

    for i in range(n):
        turnaround_time[i] = completion_time[i] - processes[i][1]
        waiting_time[i] = turnaround_time[i] - processes[i][2]
    
    # Print Gantt Chart
    print("\nGantt Chart:")
    print(" -> ".join([f"P{pid}" for pid in gantt_chart]))
    
    # Print the header with properly aligned columns
    print(f"{'Process':<8}{'Arrival':<8}{'Burst':<8}{'Completion':<12}{'Turnaround':<12}{'Waiting':<8}")
    for i, (pid, at, bt) in enumerate(processes):
        print(f"P{pid:<7}{at:<8}{bt:<8}{completion_time[i]:<12}{turnaround_time[i]:<12}{waiting_time[i]:<8}")


    # Print Average Times
    avg_tat = sum(turnaround_time) / n
    avg_wt = sum(waiting_time) / n
    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")

rrscheduling()