from collections import deque
from enum import Enum

class ProcessState(Enum):
    NEW = 0
    READY = 1
    RUNNING = 2
    TERMINATED = 3

class Process:
    next_id = 0

    def __init__(self, arrive, service):
        self.id = Process.next_id
        Process.next_id += 1
        self.arrive = arrive
        self.service = service
        self.execute = 0
        self.waiting = 0
        self.terminated = 0
        self.state = ProcessState.NEW

    def update(self):
        if self.state == ProcessState.READY:
            self.waiting += 1
        elif self.state == ProcessState.RUNNING:
            self.execute += 1

    def update_state(self, new_state, current_time):
        if self.state == ProcessState.NEW and new_state == ProcessState.READY:
            self.arrive = current_time
        elif self.state == ProcessState.RUNNING and new_state == ProcessState.TERMINATED:
            self.terminated = current_time
        self.state = new_state

    def render(self):
        if self.state == ProcessState.NEW:
            return
        print(f"Process id: {self.id} state: {self.state.name} arrive: {self.arrive} "
              f"service: {self.service} execute: {self.execute} waiting: {self.waiting} "
              f"turnaround: {self.service + self.waiting} terminated: {self.terminated}")

    def get_arrive_time(self):
        return self.arrive

    def get_service_time(self):
        return self.service

    def get_executed_time(self):
        return self.execute

    def get_turnaround_time(self):
        return self.service + self.waiting

class SchedulerSimulator:
    def __init__(self):
        self.new_processes = deque()
        self.run_process = None
        self.terminated_processes = deque()
        self.running = False
        self.current_time = 0

    def add_process(self, process):
        self.new_processes.append(process)

    def start(self):
        self.running = True
        self.current_time = 0
        while self.running:
            self.scheduler()
            if not self.run_process:
                break
            self.running = not self.all_processes_completed()
            if self.running:
                self.current_time += 1

    def end(self):
        for process in self.terminated_processes:
            process.render()

    def scheduler(self):
        raise NotImplementedError

    def all_processes_completed(self):
        raise NotImplementedError

class FCFSSimulator(SchedulerSimulator):
    def __init__(self):
        super().__init__()
        self.ready_processes = deque()

    def scheduler(self):
        i = 0
        for process in list(self.new_processes):
            if process.get_arrive_time() == self.current_time:
                process.update_state(ProcessState.READY, self.current_time)
                self.ready_processes.append(process)
                self.new_processes.remove(process)
                i += 1

        if not self.run_process:
            if self.ready_processes:
                self.run_process = self.ready_processes.popleft()
                self.run_process.update_state(ProcessState.RUNNING, self.current_time)
        else:
            self.run_process.update()
            if self.run_process.get_service_time() - self.run_process.get_executed_time() == 0:
                self.run_process.update_state(ProcessState.TERMINATED, self.current_time)
                self.terminated_processes.append(self.run_process)
                self.run_process = None
                if self.ready_processes:
                    self.run_process = self.ready_processes.popleft()
                    self.run_process.update_state(ProcessState.RUNNING, self.current_time)

        for process in self.ready_processes:
            process.update()

    def all_processes_completed(self):
        return self.run_process is None

if __name__ == "__main__":
    sim = FCFSSimulator()
    sim.add_process(Process(0, 3))
    sim.add_process(Process(2, 6))
    sim.add_process(Process(4, 4))
    sim.add_process(Process(6, 5))
    sim.add_process(Process(8, 2))
    
    sim.start()
    sim.end()
