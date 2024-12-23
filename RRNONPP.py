def print_gantt_chart(processes, arrival_times, burst_times, wait_times, turn_around_times, completion_times, response_times):
    print("\nGantt Chart:")
    print("P\tAT\tBT\tWT\tTAT\tCT\tRT")
    for i in range(len(processes)):
        print(f"{processes[i]}\t{arrival_times[i]}\t{burst_times[i]}\t{wait_times[i]}\t{turn_around_times[i]}\t{completion_times[i]}\t{response_times[i]}")

    print(f"\nAverage Waiting Time: {sum(wait_times) / len(wait_times):.2f}")
    print(f"Average Turnaround Time: {sum(turn_around_times) / len(turn_around_times):.2f}")


def non_preemptive_priority_round_robin(processes, arrival_times, burst_times, priorities, time_quantum):
    n = len(processes)
    remaining_times = burst_times[:]
    completion_times = [0] * n
    wait_times = [0] * n
    turn_around_times = [0] * n
    response_times = [-1] * n
    current_time = 0
    queue = []

    # Sort processes by priority and arrival time
    sorted_indices = sorted(range(n), key=lambda x: (priorities[x], arrival_times[x]))

    while any(rt > 0 for rt in remaining_times):
        for i in sorted_indices:
            if arrival_times[i] <= current_time and remaining_times[i] > 0 and i not in queue:
                queue.append(i)

        if queue:
            process_index = queue.pop(0)

            # Response time
            if response_times[process_index] == -1:
                response_times[process_index] = current_time - arrival_times[process_index]

            # Execute the process for time quantum or remaining burst time
            execution_time = min(time_quantum, remaining_times[process_index])
            current_time += execution_time
            remaining_times[process_index] -= execution_time

            # If process is completed
            if remaining_times[process_index] == 0:
                completion_times[process_index] = current_time
            else:
                queue.append(process_index)

    # Calculate waiting time and turnaround time
    for i in range(n):
        turn_around_times[i] = completion_times[i] - arrival_times[i]
        wait_times[i] = turn_around_times[i] - burst_times[i]

    print_gantt_chart(processes, arrival_times, burst_times, wait_times, turn_around_times, completion_times, response_times)


# Example Usage
processes = ["A", "B", "C", "D"]
arrival_times = [0, 1, 2, 3]
burst_times = [5, 3, 8, 6]
priorities = [1, 1, 2, 2]
time_quantum = 2

non_preemptive_priority_round_robin(processes, arrival_times, burst_times, priorities, time_quantum)
