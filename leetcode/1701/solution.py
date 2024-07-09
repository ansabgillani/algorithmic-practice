class Solution:
    def averageWaitingTime(self, customers):
        total_wait = current_time = 0
        
        for arrival, time in customers:
            if current_time < arrival:
                current_time = arrival
            
            current_time += time
            total_wait += current_time - arrival
        
        return total_wait / len(customers)