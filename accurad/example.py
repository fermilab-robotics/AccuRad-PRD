from accurad import ACCURAD as ACR

def main():
	
	acr = ACR(port='/dev/ttyACM0')

	rate = acr.get_dose_rate # mrem/hr, counts/sec, mrem, duration
	print(f"{rate}")
	
	print(f"Millirem: {acr.millirem}")
	print(f"Millirem/hr: {acr.mrem_per_hour}")
	
if __name__ == '__main__':
    main()
