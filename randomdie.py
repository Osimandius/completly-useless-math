import random
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics

count = []
dice_result = []
for i in range (0,100000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    #print(dice1,dice2)
    dice_result.append(dice1+dice2)
    #print(dice_result)
    count.append(i)


mean = sum(dice_result)/len(dice_result)
std_deviation = statistics.stdev(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)

print("Mean :"+ str(mean))
print("Std_deviation : "+ str(std_deviation))

print("Median :"+ str(median))

print("Mode :"+ str(mode))

# graf2=px.bar(x=dice_result, y=count)
# graf2.show()

#To specify range
first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
scnd_std_deviation_start, scnd_std_deviation_end = mean-2*std_deviation, mean+2*std_deviation
thrd_std_deviation_start, thrd_std_deviation_end = mean-3*std_deviation, mean+3*std_deviation

#Collect data in the rage of first standard deviation
list_of_data_within_1_std_deviation = [result for result in dice_result if result > first_std_deviation_start and result < first_std_deviation_end]

print("{}% of data lies within 1st standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(dice_result)))

list_of_data_within_2_std_deviation = [result for result in dice_result if result > scnd_std_deviation_start and result < scnd_std_deviation_end]

print("{}% of data lies within 2nd standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(dice_result)))

list_of_data_within_3_std_deviation = [result for result in dice_result if result > thrd_std_deviation_start and result < thrd_std_deviation_end]

print("{}% of data lies within 3rd standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(dice_result)))


fig = ff.create_distplot([dice_result],["Result"],show_hist=True)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[scnd_std_deviation_start, scnd_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[scnd_std_deviation_end, scnd_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[thrd_std_deviation_start, thrd_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.add_trace(go.Scatter(x=[thrd_std_deviation_end, thrd_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))

fig.show()

