import math

def get_last_digits(num):
   # array to store the last digits of the pyramid
   digits = []
   # current value is 0
   curr = 0
   # get number of rows based on elements length
   rows = int((-1 + math.sqrt(1 + 8 * num)) / 2)
   # loop through
   for i in range(1, rows+1):
      if curr + i <= num:
         curr += i
         # append value to array
         digits.append(curr)
   return digits
   
def decode(message_file):
   dictionary = {}
   str = []
   # Read the encoded message from the file
   with open(message_file, 'r') as file:
       for line in file:
           # Split each line into numbers and words
           number, word = line.split(maxsplit=1)
           # add to dictionary ad key value pair
           dictionary[int(number)] = word.strip()
   # get the array of last digits for each row
   digits = get_last_digits(len(dictionary))
   # iterate through digits array and retrieve value for each digit
   for digit in digits:
      str.append(dictionary[digit])
   # return joined string
   return " ".join(str)

message_file_path = './coding_qual_input.txt'
decoded_message = decode(message_file_path)
print(decoded_message)