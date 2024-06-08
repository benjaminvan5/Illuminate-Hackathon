data = open('data.txt', 'r')
global dictionary
dictionary = {}
medical_information = data.read()
if medical_information != "":
  medical_information = medical_information.rstrip(medical_information[-1])
  dictionary = dict([x.split(',') for x in medical_information[1:-1].split('),(')])
