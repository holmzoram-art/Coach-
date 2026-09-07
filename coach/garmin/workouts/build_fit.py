import os, datetime
from fit_tool.fit_file_builder import FitFileBuilder
from fit_tool.profile.messages.file_id_message import FileIdMessage
from fit_tool.profile.messages.workout_message import WorkoutMessage
from fit_tool.profile.messages.workout_step_message import WorkoutStepMessage
from fit_tool.profile.profile_type import (
    FileType, Manufacturer, Sport, WorkoutStepDuration, WorkoutStepTarget, Intensity
)

OUT = "/home/user/Coach-/coach/garmin/workouts"
HR_OFFSET = 100  # FIT: 1-100 = % av makspuls, 101-255 = bpm + 100

def hr(bpm):
    assert 55 <= bpm <= 210, bpm  # feltet er uint32, ingen 255-tak
    return bpm + HR_OFFSET

def step(idx, name, dur, intensity=Intensity.ACTIVE, seconds=None, meters=None,
         lo=None, hi=None):
    s = WorkoutStepMessage()
    s.message_index = idx
    s.workout_step_name = name
    s.intensity = intensity
    if dur == "time":
        s.duration_type = WorkoutStepDuration.TIME
        s.duration_time = float(seconds)
    elif dur == "distance":
        s.duration_type = WorkoutStepDuration.DISTANCE
        s.duration_distance = float(meters)
    elif dur == "open":
        s.duration_type = WorkoutStepDuration.OPEN
    if lo is None and hi is None:
        s.target_type = WorkoutStepTarget.OPEN
        s.target_value = 0
    else:
        s.target_type = WorkoutStepTarget.HEART_RATE
        s.target_value = 0                      # 0 = egendefinert sone
        s.custom_target_value_low = hr(lo)
        s.custom_target_value_high = hr(hi)
    return s

def repeat(idx, from_idx, times):
    s = WorkoutStepMessage()
    s.message_index = idx
    s.duration_type = WorkoutStepDuration.REPEAT_UNTIL_STEPS_CMPLT
    s.duration_value = from_idx
    s.target_type = WorkoutStepTarget.OPEN
    s.target_value = times
    return s

def build(filename, wkt_name, steps):
    b = FitFileBuilder(auto_define=True)
    fid = FileIdMessage()
    fid.type = FileType.WORKOUT
    fid.manufacturer = Manufacturer.DEVELOPMENT.value
    fid.product = 0
    fid.time_created = round(datetime.datetime.now().timestamp() * 1000)
    fid.serial_number = 0x12345678
    b.add(fid)
    w = WorkoutMessage()
    w.workout_name = wkt_name
    w.sport = Sport.RUNNING
    w.num_valid_steps = len(steps)
    b.add(w)
    b.add_all(steps)
    path = os.path.join(OUT, filename)
    b.build().to_file(path)
    return path

# 3 bpm luft utenfor grensen (fysiolog); tak-økter får gulv 90 så alarmen
# bare fyrer oppover.
FLOOR = 90

W = []

# 1. I1 restitusjon - tak 138
W.append(("01_I1_restitusjon.fit", "I1 Restitusjon", [
    step(0, "Rolig, under 138", "open", lo=FLOOR, hi=141),
]))

# 2. Sondag rolig 4 km - tak 142
W.append(("02_Sondag_rolig.fit", "Sondag rolig", [
    step(0, "Rolig, under 142", "open", lo=FLOOR, hi=145),
]))

# 3. Langtur i gruppe I2 - tak 157
W.append(("03_Langtur_I2.fit", "Langtur I2", [
    step(0, "Oppvarming 10 min uten alarm", "time", seconds=600,
         intensity=Intensity.WARMUP),
    step(1, "Langtur, under 157", "open", lo=FLOOR, hi=160),
]))

# 4. 8K Flat referanseokt - 142-148
W.append(("04_8K_Flat_referanse.fit", "8K Flat referanse", [
    step(0, "Oppvarming 10 min", "time", seconds=600, intensity=Intensity.WARMUP),
    step(1, "8 km i 142-148", "distance", meters=8000, lo=139, hi=151),
    step(2, "Nedjogg", "time", seconds=300, intensity=Intensity.COOLDOWN,
         lo=FLOOR, hi=141),
]))

# 5. I3 tempo / kalibrering - 157-166
W.append(("05_I3_tempo_kalibrering.fit", "I3 Tempo kalibrering", [
    step(0, "Oppvarming 10 min", "time", seconds=600, intensity=Intensity.WARMUP),
    step(1, "Tempo 157-166", "time", seconds=1800, lo=154, hi=169),
    step(2, "Nedjogg 10 min", "time", seconds=600, intensity=Intensity.COOLDOWN,
         lo=FLOOR, hi=141),
]))

# 6. I4 terskelintervaller - tak 176, 4 x 6 min / 2 min
W.append(("06_I4_terskelintervaller.fit", "I4 Terskel 4x6", [
    step(0, "Oppvarming 15 min", "time", seconds=900, intensity=Intensity.WARMUP),
    step(1, "6 min terskel, under 176", "time", seconds=360, lo=FLOOR, hi=179),
    step(2, "2 min trav", "time", seconds=120, intensity=Intensity.REST,
         lo=FLOOR, hi=150),
    repeat(3, 1, 4),
    step(4, "Nedjogg 10 min", "time", seconds=600, intensity=Intensity.COOLDOWN,
         lo=FLOOR, hi=141),
]))

# 7. Dagens okt - 40-50 min flatt, I2 137-150
W.append(("07_Dagens_I2_40-50min.fit", "I2 40-50 min flatt", [
    step(0, "Oppvarming 10 min uten alarm", "time", seconds=600,
         intensity=Intensity.WARMUP),
    step(1, "35 min i 137-150", "time", seconds=2100, lo=134, hi=153),
    step(2, "Nedjogg 5 min", "time", seconds=300, intensity=Intensity.COOLDOWN,
         lo=FLOOR, hi=141),
]))

for fn, name, steps in W:
    print(build(fn, name, steps))
