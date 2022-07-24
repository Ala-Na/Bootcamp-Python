import math


class TinyStatistician():

	def mean(self, x):
		if not isinstance(x, list) or len(x) == 0:
			print("Not a non-empty array or list")
			return None
		res = 0
		for elem in x:
			res += elem
		return float(res/len(x))

	def median(self, x):
		if not isinstance(x, list) or len(x) == 0:
			print("Not a non-empty array or list")
			return None
		x.sort()
		if (len(x) % 2 == 0):
			return float((x[int(len(x) / 2)] + x[int((len(x) - 1) / 2)]) / 2)
		else :
			return float(x[int((len(x) - 1) / 2)])

	def quartiles(self, x):
		if not isinstance(x, list) or len(x) == 0:
			print("Not a non-empty array or list")
			return None
		x.sort()
		if (len(x) / 4) % 2 == 0:
			first_ind = int((len(x) - 1) / 4)
		else:
			first_ind = int((len(x)) / 4)
		if (len(x) * 3 / 4) % 2 == 0:
			third_ind = int(((len(x) - 1) * 3) / 4)
		else:
			third_ind = int(((len(x)) * 3) / 4)
		return [float(x[first_ind]), float(x[third_ind])]

	def var(self, x):
		if not isinstance(x, list) or len(x) == 0:
			print("Not a non-empty array or list")
			return None
		mean = self.mean(x)
		res = 0
		for elem in x:
			res += (elem - mean) ** 2
		res /= len(x)
		return res

	def std(self, x):
		if not isinstance(x, list) or len(x) == 0:
			print("Not a non-empty array or list")
			return None
		var = self.var(x)
		return math.sqrt(var)


tstat = TinyStatistician()
a = [1, 42, 300, 10, 59]
print(tstat.mean(a))
# Expected result: 82.4
print(tstat.median(a))
# Expected result: 42.0
print(tstat.quartiles(a))
# Expected result: [10.0, 59.0]
print(tstat.var(a))
# Expected result: 12279.439999999999
print(tstat.std(a))
# Expected result: 110.81263465868862
