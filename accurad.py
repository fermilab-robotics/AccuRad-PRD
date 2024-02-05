from serial import Serial

class ACCURAD:
	def __init__(self, port='/dev/ttyACM0', baud=115200, timeout=1):
		self.port = port
		self.baud = baud
		self.timeout = timeout
		self.serial = Serial(port=self.port, baudrate=self.baud, timeout=self.timeout)
		self.mrem = 0
		self.mrem_p_h = 0
		
	@property
	def millirem(self):
		self.get_dose_rate
		return self.mrem
		
	@property
	def mrem_per_hour(self):
		self.get_dose_rate
		return self.mrem_p_h
		
	@property
	# returns millirem per hour, counts per second, millrem, duration
	def get_dose_rate(self):
		DOSE_RATE_INDEX = [19, 18, 17, 16]
		CPS_INDEX = [23, 22, 21, 20]
		DOSE_INDEX = [47, 46, 45, 44]
		DURATION_INDEX = [51, 50, 49, 48]
		BYTES_TO_READ = 64
		REQUEST_DATA_MESSAGE = bytes.fromhex(
			"23 21 41 63 63 75 52 61 64 21 23 0A 00 01 00 7E 04 00 11 A7 1E 43 E7")
		try:
			self.serial.write(REQUEST_DATA_MESSAGE)
			# Read the response
			response_bytes = self.serial.read(BYTES_TO_READ)
		except serial.SerialException as e:
			print(f"Error during communication: {e}")
			
		dri = self.bytes_to_hex_string(DOSE_RATE_INDEX, response_bytes)
		cps = self.bytes_to_hex_string(CPS_INDEX, response_bytes)
		dos = self.bytes_to_hex_string(DOSE_INDEX, response_bytes)
		dur = self.bytes_to_hex_string(DURATION_INDEX, response_bytes)
		
		uSv_rate 			= self.hex_to_float(dri)
		counts_per_second 	= self.hex_to_float(cps)
		uSv 				= self.hex_to_float(dos)
		seconds 			= self.hex_to_float(dur)

		self.mrem_p_h 	= self.microsevert_to_mrem(uSv_rate)
		self.mrem 		= self.microsevert_to_mrem(uSv)
		duration = self.seconds_to_hours(seconds)

		return {self.mrem_p_h, counts_per_second, self.mrem, duration}
		
	def seconds_to_hours(self, seconds):
		return seconds / 3600

	def microsevert_to_mrem(self, uSv):
		return uSv / 10

	def hex_to_float(self, hex_str):
		import struct
		return struct.unpack("!f", bytes.fromhex(hex_str))[0]

	def bytes_to_hex_string(self, index_list, response_bytes):
		result_str = ""
		# Parse and rearrange data
		for index in index_list:
			# Use f-string formatting to add the hex value to the result string.
			# The f-string automatically converts the bytes to a string.
			# Our formatting specification after the colon tells tells the f-string to
			# convert to a hex string, and then pad the string with leading zeros.
			
			result_str = f"{result_str}{response_bytes[index]:02x}"
			# After having a better understanding of how this is used, I don't think
			# we need to convert this to a string. We can just use the bytes directly.
			#
			# result = b''
			# for index in index_list:
			#    result = result + response_bytes[index]
			# return result
			#
			# I'm not making this change because I can see an argument that
			# converting to hex is simpler to reason about.
			
		return result_str

