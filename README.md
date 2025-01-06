# Device freeze protection

A script that uses Amazon Alexa + ECO Plugs smart switches to automatically turn on a switch when the air temperature is below freezing, in order to provide freeze protection.

Specifically tested with the [Dewenwils Smart Switch](https://www.amazon.com/gp/product/B07PP2KNNH)

Assisted by the following APIs:
* [Voicemonkey]("https://voicemonkey.io")
* [Zipcodebase]("https://zipcodebase.com/")
* [Open-meteo]("https://open-meteo.com/")

## Usage
A series of setup steps are required to use this automation.

1. Enable the [ECO Plugs skill](https://www.amazon.com/ECO-PLUGS-Plugs/dp/B0716C299L) in Alexa
2. Ensure your device is detected in Alexa devices; if working you should be able to turn the switch on/off from an Echo device.
3. Enable the [Voicemonkey skill](https://voicemonkey.io/start) in Alexa
4. Create a "Routine trigger" in Voicemonkey with the name of your choice (e.g. "turn-on-device")
5. Create a routine in Alexa, triggered by the Voicemonkey trigger, which turns on your ECO Plug smart switch
6. Create an account with Zipcodebase.com in order to get an API key

### Command-line interface:
```
python3 device_freeze_protect.py ZIP_CODE ROUTINE_TRIGGER
```

ZIP_CODE: the Zip code where the pool is located, used to derive local air temperature
ROUTINE_TRIGGER: the name of the Voicemonkey trigger for turning on the ECO Plug smart switch 

### Environment variables

As the Voicemonkey and Zipcodebase APIs require API keys, those are passed via environment variables.

```
ZIP_CODE_API_KEY=<yours>
VOICEMONKEY_API_KEY=<yours>
```
