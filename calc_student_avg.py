import csv
#open reader object
scores = open('student_scores.csv', 'r')
student_scores = csv.reader(scores, delimiter=',')
#create writer object
averages = open('student_avg.csv', 'w', newline='')
student_averages = csv.writer(averages, delimiter=',')
#loop to write row
for record in student_scores:
    avg = 0
    name = record[0]
    scoreOne = float(record[1])
    scoreTwo = float(record[2])
    scoreThree = float(record[3])
    #calc average
    avg = (scoreOne + scoreTwo + scoreThree)/3
    #write name and average
    student_avg = [name, format(avg, '.2f')]
    student_averages.writerow(student_avg)
#close files
scores.close()
averages.close()