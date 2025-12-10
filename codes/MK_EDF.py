from simso.core import Scheduler
from simso.schedulers import scheduler

@scheduler("simso.schedulers.MK_EDF")
class MK_EDF(Scheduler):
    """Earliest Deadline First with (m,k)-firm requirements"""
    def on_activate(self, job):
        job.cpu.resched()

    def on_terminated(self, job):
        job.cpu.resched()

    def schedule(self, cpu):
        ready_jobs = [t.job for t in self.task_list
                      if t.is_active() and not t.job.is_running()]

        if ready_jobs:
            job = min(ready_jobs, key=lambda x: (x.optional, x.absolute_deadline, x.period))

            if (((cpu_min.running is None) or ((cpu_min.running is not None and job is not None) and (cpu_min.running.optional and job.mandatory) and (cpu_min.running.absolute_deadline < job.absolute_deadline)) or (cpu_min.running.absolute_deadline > job.absolute_deadline)) and not ((cpu_min.running is not None and cpu_min.running.mandatory) and job.optional)):
                print(self.sim.now()/1000000, job.name, cpu_min.name)
                return (job, cpu_min)
