# Please read the following comment

https://github.com/kellerza/python-ids-alarm/issues/2#issuecomment-486716578

# python-ids-alarm
(Draft) Python library to interface with IDS Alarm panels.

There seems to be little support for interfacing with Inhep Digital Security (IDS) alarm panels. The older generation IDS 816/1632 models seem to have no support for third part interfacing. On the newer X64 models, there is onboard serial port with IDSwift software. No third party libraries found yet and IDS does not seem willing to share any details.

If you are looking into a new system the DSC (+Envisalink) is probably the better choice.

If, like me, you have IDS thats working perfectly well, this might be helpful.

The IDS X64 is also distributed as the WatchGuard WGAP864.

## RS485 bus interface

Based on a FTDI 232R USB to serial adaptor (5V) with a Maxim MAX485E RS-485 driver connected directly to `D+` & `D-` of the alarm bus

Only receive at the moment, with `RE'` & `DE` pulled to `GND`, but bidirectional communications could be achived by connecting this to `RTS`

## idsdecode.py

Monitors the serial port (using the RS485 interface) and prints out alarm events.

Example output:

![idsdecode](/img/idsdecode.png)
