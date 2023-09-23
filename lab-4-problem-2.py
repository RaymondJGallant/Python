#input= user temperature
#output= user temperature converted to farenheight

#Author = RaymondJGallant
#Date&&Time = 9/22/2023 21:31




userTemp=input("what is the temp in celcius: ")  # initial variable of users temperature in Celcius //input
celciusTemp=float(userTemp)                      # conversion of user input which is default string data type // this converts the users string into a floating pont number in order to perform arithmetic operation
farenheightTemp=(float(celciusTemp*9/5+32.0))    # actual arithmetic operation as described above

print(farenheightTemp)                           #output