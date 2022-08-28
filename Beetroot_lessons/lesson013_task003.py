"""TV controller
Create a simple prototype of a TV controller in Python. It’ll use the following
commands:
first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers
start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one,
turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the
first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns
"Yes", if the channel N or 'name' exists in the list, or "No" - in the other case.

The default channel turned on before all commands is №1.
Your task is to create the TVController class and methods described above.

```
CHANNELS = ["BBC", "Discovery", "TV1000"]
class TVController:
pass

controller = TVController(CHANNELS)
controller.first_channel() == "BBC"
controller.last_channel() == "TV1000"
controller.turn_channel(1) == "BBC"
controller.next_channel() == "Discovery"
controller.previous_channel() == "BBC"
controller.current_channel() == "BBC"
controller.is_exist(4) == "No"
controller.is_exist("BBC") == "Yes"
```"""

CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    channel_index = 0

    def __init__(self, channels):
        self.channels = channels

    def first_channel(self):
        TVController.channel_index = 0
        print(self.channels[TVController.channel_index])

    def last_channel(self):
        TVController.channel_index = -1
        print(self.channels[TVController.channel_index])

    def turn_channel(self, number: int):
        TVController.channel_index = number - 1
        try:
            print(self.channels[TVController.channel_index])
        except IndexError:
            print("Channel is not exist")

    def next_channel(self):
        if TVController.channel_index + 1 > len(self.channels) - 1:
            TVController.channel_index -= len(self.channels) - 1
        else:
            TVController.channel_index += 1
        print(self.channels[TVController.channel_index])

    def previous_channel(self):
        if TVController.channel_index - 1 < 0:
            TVController.channel_index += len(self.channels) - 1
        else:
            TVController.channel_index -= 1
        print(self.channels[TVController.channel_index])

    def current_channel(self):
        print(self.channels[TVController.channel_index])

    def is_exist(self, channel):
        try:
            if (type(channel) == int and self.channels[channel-1] or
                    type(channel) == str and channel in self.channels):
                print("Yes")
            else:
                print("No")
        except IndexError:
            print("No")


controller = TVController(CHANNELS)
controller.first_channel()      # == "BBC"
controller.last_channel()       # == "TV1000"
controller.turn_channel(1)      # == "BBC"
controller.next_channel()       # == "Discovery"
controller.previous_channel()   # == "BBC"
controller.current_channel()    # == "BBC"
controller.is_exist(4)          # == "No"
controller.is_exist("BBC")      # == "Yes"
