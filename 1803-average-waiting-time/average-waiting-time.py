class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        start_time = customers[0][0] + customers[0][1]
        waiting_times = []
        waiting_times.append(customers[0][1])
        for i in range(1, len(customers)):
            arrival, time  = customers[i][0], customers[i][1]
            time = customers[i][1]
            start_time = arrival+time if arrival > start_time else start_time+time
            waiting_times.append(start_time - arrival)
        return sum(waiting_times)/len(waiting_times)
                
        