from pydantic import BaseModel
from typing import Literal

class TimeSlotDto(BaseModel):
    classroom_name: str
    course_name: str
    teacher_name: str
    start: int
    end: int
    day: Literal["Lunedi", "Martedi", "Mercoledi", "Giovedi", "Venerdi"]
    color_hex: str
    
# we have a list for each year, and we have 3 years
class ScheduleDto(BaseModel):
    year_schedules: list[
        list[TimeSlotDto]
    ]
    query_time_ms: int
    