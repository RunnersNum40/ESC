class Matrix:
	def __init__(self, *rows, **kwargs):
		self.mat = list(map(list, rows))
		self.x_len = len(self.mat)
		self.y_len = len(self.mat[0])
		self.__dict__.update(kwargs)
	def __str__(self):
		return "["+",\n ".join(map(str, self.mat))+"]"
	#P2
	@staticmethod
	def get_lead_ind(row):
		return min(i for i in range(len(row)) if row[i]!=0)
	#P3
	def get_row_to_swap(self, start_i):
		"""Return the row with the leftmost 0 which can be swapped with start_i. If more than one row has the leftmost 0 return the furthest down of them.
		start_i is an int."""
		return min(range(start_i+1, self.x_len), key=lambda i: self.get_lead_ind(self.mat[i])) #find the index that has the least index of 0
	#P4
	@staticmethod
	def add_rows_coefs(r1, c1, r2, c2):
		r1 = [r1[i]*c1 for i in range(len(r1))]
		r2 = [r2[i]*c2 for i in range(len(r2))]
		return [*map(sum, zip(r1, r2))]
	#P5
	def eliminate(self, row_to_sub, best_lead_ind):
		print(row_to_sub, best_lead_ind)
		print(self.mat[row_to_sub], self.mat[row_to_sub][best_lead_ind])
		for i in range(self.x_len):
			if i != row_to_sub:
				row = self.mat[i]
				print("Row:", row)
				print("Coef:", -row[best_lead_ind]/self.mat[row_to_sub][best_lead_ind])
				print("Result:", self.add_rows_coefs(self.mat[row_to_sub], 1, row, -row[best_lead_ind]/self.mat[row_to_sub][best_lead_ind]))
				self.mat[i] = self.add_rows_coefs(self.mat[row_to_sub], 1, row, -row[best_lead_ind]/self.mat[row_to_sub][best_lead_ind])
	#P6
	def forward_step(self):
		for i in range(self.x_len):
			self.mat[i], self.mat[self.get_row_to_swap(i)] = self.mat[self.get_row_to_swap(i)], self.mat[i]
			print(self)
			self.eliminate(i, self.get_lead_ind(self.mat[i]))
			print(self)


m = Matrix(*[[0,0,1,0,2],[1,0,2,3,4],[3,0,4,2,1],[1,0,1,1,2]])
print(m)
m.forward_step()
print(m)