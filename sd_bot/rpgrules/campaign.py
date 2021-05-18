import sched
import time

from typing import List
from sd_bot.rpgrules.note import NoteList


class Campaign:
    notes: NoteList
    supplies: int = 0

    scheduler = sched.scheduler(time.time, time.sleep)

    def create_campaign(
        self, 
        name: str,
        master: str,
        zoombie_clock_minutes: int

    ) -> None:
        self.set_name(name)
        self.set_master(master)
        self.set_zoombie_clock_interval(zoombie_clock_minutes)
        self.set_refuge(0)
        self.set_supplies(0)
        self.set_zoombie_clock(0)

    def set_name(self, name: str) -> None:
        if not name.strip():
            raise ValueError("Campaign name cannot be Empty")    
        self.name = name

    def get_name(self) -> str:
        return self.name    

    def set_master(self, master: str) -> None:
        if not master.strip():
            raise ValueError("Campaign master cannot be Empty")    
        self.master = master
    
    def get_master(self) -> str:
        return self.master

    def set_zoombie_clock_interval(self, zoombie_clock_minutes: int) -> None:
        if zoombie_clock_minutes < 10:
            raise ValueError("Zoombie Clock interval needs to be greater than 10")
        self.zoombie_clock_interval = zoombie_clock_minutes

    def get_zoombie_clock_interval(self) -> int:
        return self.zoombie_clock_interval

    def set_zoombie_clock(self, zoombie_clock=0) -> None:
        if zoombie_clock < 0:
            raise ValueError("Zoombie Clock needs to be greater or equal 0")
        self.zoombie_clock = zoombie_clock

    def get_zoombie_clock(self) -> int:
        return self.zoombie_clock

    def increment_zoombie_clock(self) -> None:
        self.zoombie_clock += 1

    def tick_zoombie_clock(self) -> str:
        self.increment_zoombie_clock()
        self.remove_supplies(1)

        if self.get_refuge() <= self.get_zoombie_clock():
            self.set_zoombie_clock()
            return "Refuge invasion!"
        else: 
            return "Refuge still safe!"

    def set_notes(self, notes: NoteList) -> None:
        self.notes = notes

    def get_notes(self) -> NoteList:
        return self.notes

    def set_supplies(self, supplies: int) -> None:    
        self.supplies = supplies

    def get_supplies(self) -> int:
        return self.supplies

    def add_supplies(self, supplies: int) -> None:
        self.supplies += supplies

    def remove_supplies(self, supplies: int) -> None:
        if (self.supplies - supplies ) > 0:
            self.supplies -= supplies
        else: 
            self.supplies = 0

    def set_refuge(self, refuge: int) -> None:
        if refuge < 0:
            raise ValueError("Refuge Level needs to be greater or equal 0")
        self.refuge = refuge

    def get_refuge(self) -> int:
        return self.refuge

    def queue_clock(self) -> List[sched.Event]:
        return self.scheduler.queue

    def start_clock(self) -> sched.Event:
        if not self.scheduler.empty():        
            self.stop_clock()
        self.scheduler.run()
        return self.scheduler.enter(self.get_zoombie_clock_interval(), 1, self.tick_zoombie_clock())

    def stop_clock(self) -> None:
        for event in self.queue_clock():
            self.scheduler.cancel(event)
