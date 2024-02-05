# AccuRad PRD USB Python Interface

This Python library provides methods for accessing the AccuRad PRD via USB. 

## Dependency installation

```sh
python -m pip install -r requirements.txt
``````

## Local pip install 

`accurad` is configured as module that can be installed on your local machine 

1. Clone the repository

```
cd /your-dir
git clone https://github.com/fermilab-robotics/AccuRad-PRD.git
```

2. Install the module 

Make sure `setuptools` is installed. If not: 
```
pip install setuptools -U
```
Then:
```
cd yourdir/AccuRad-PRD
pip install .
```


## Example 

```
from accurad.accurad import ACCURAD as ACR

acr = ACR(port='/dev/ttyACM0')
	rate = acr.get_dose_rate # mrem/hr, counts/sec, mrem, duration
	print(f"{rate}")
	print(f"Millirem: {acr.millirem}")
	print(f"Millirem/hr: {acr.mrem_per_hour}")

```


