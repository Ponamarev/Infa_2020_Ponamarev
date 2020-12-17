import random
from winsound import *
import sys


# dict with samples' addresses
samples = {
    "strumento melodico": {
        "low": "samples\\melodia\\low.wav",
        "high": "samples\\melodia\\high.wav"
    },
    "tamburi": {
        1: "samples\\tamburi\\1.wav"
    }
}

# the main dict of rules according to which notes change
# note that everything may go to hell if some list shell not be sorted
harmony = {
    "basic harmony": {
        "after keys": {
            -4: [-4, -1, 1, 3],
            -3: [-1, 1, 3, 4],
            -2: [-1, 1, 3],
            -1: [-2, 1, 2, 3],
            1: [-1, 1, 3, 4],
            2: [1, 3],
            3: [-2, -1, 1, 2],
            4: [-4, 3, 4]
        },
        "before keys": {
            -4: [-3, 1, 4],
            -3: [-1, ],
            -2: [],
            -1: [],
            1: [],
            2: [],
            3: [],
            4: []
        }
    },
    "advanced harmony": {

    },
    "cool endings": {

    },
    "drum hooks": {

    }
}


class MelodyPattern:
    def __init__(self, timesign, duration):
        self.timesign = timesign
        self.duration = duration
        self.notes = []
        self.old_notes = []
        stronginterval = random.choice((-1, 1, 3))
        self.strongnote = random.randint(0, self.timesign - 1)

        for i in range(self.timesign):
            if not i == self.strongnote:
                self.notes.append(0)

            else:
                self.notes.append(stronginterval)
        self.relaxation(self.notes)

        # stages of the melody
        self.stages = {
            0: "starting",
            1: "first variation",
            2: "second variation",
            3: "ending"
        }
        # initial stage is "starting", then it shell define a current stage
        self.stage = self.stages[0]

    def new_stage(self, name_of_stage):
        if type(name_of_stage) == int:
            self.stage = self.stages[name_of_stage]
        else:
            self.stage = name_of_stage


class Melody (MelodyPattern):
    def __init__(self, timesign, duration=0):
        super().__init__(timesign, duration)
        self.background = []

        for i in range(self.timesign**2 - self.timesign):
            self.background.append(0)

    def var(self, notes):
        """
        building a list of notes` variations by changing some one note
        :param notes: list of notes
        :return: notes` variation
        """
        lenght = len(notes)
        variations = []

        if self.stage == "starting":
            notes_nums = []
            if not notes.count(0):
                notes_nums = range(lenght)
            else:
                array_of_notes = [nts for nts in notes if notes[nts] == 0]

            for i in notes_nums:
                var1 = []
                var2 = []

                notesMatter = [notes[i - 2], notes[i - 1], notes[i + 1], notes[i + 2]]
                var1 = harmony["basic harmony"]["after keys"][notesMatter[1]]
                var2 = harmony["basic harmony"]["before keys"][notesMatter[2]]

                if lenght >= 4:
                    for ntoe in var1 + var2:
                        if ntoe == notesMatter[0] or ntoe == notesMatter[2]:
                            var1.remove(ntoe)
                            var2.remove(ntoe)

                variant = [var1[ant] for ant in var1 if var2.count(var1[ant])]

                for j in variant:
                    new_variation = []

                    for k in notes:
                        if not k == i:
                            new_variation.append(notes.key)
                        else:
                            new_variation.append(j)

                    variations.append(new_variation)

        elif self.stage == "first variation":
            pass

        elif self.stage == "second variation":
            pass

        elif self.stage == "ending":
            pass

        return variations

    def relaxation(self):
        if self.stage == "starting":
            self.old_notes = self.notes

            if len(self.notes) == self.timesign:
                new_note = random.choice(self.var(self.old_notes))

                for i in range(self.timesign - 1):
                    if not i == self.strongnote:
                        self.notes.extend(new_note)

                    else:
                        absolutely_new_notes = new_note

                        for j in range(self.timesign - 2):
                            absolutely_new_notes = random.choice(self.var(absolutely_new_notes))

                        self.notes.extend(absolutely_new_notes)

            else:
                bar = random.choice([i for i in range(self.timesign) if not i == self.strongnote])
                partNote = [self.old_notes[note] for note in range(bar * self.timesign, (bar + 1) * self.timesign)]

                new_note = random.choice(self.var(partNote))
                for i in range(self.timesign - 1):
                    if not i == self.strongnote:
                        for j in range(self.timesign):
                            self.notes.insert(i * self.timesign + j, new_note[j])

        elif self.stage == "variation 1":
            pass

        elif self.stage == "variation 2":
            pass

        elif self.stage == "ending":
            pass


class Beat (MelodyPattern):
    def __init__(self, timesign, duration=0):
        super().__init__(timesign, duration)

    def relaxation(self):
        pass


def updating(mel, beat, set_stage=0):
    pass


# FIXME: winsound may not work adequately; lib for linux even can not be plugged
def play_melody(gamma, volume, duration, agressive="low"):
    pass
