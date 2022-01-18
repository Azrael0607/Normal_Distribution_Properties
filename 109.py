import random
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics 
dice_result = []
count = []
for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1 + dice2)
    count.append(i)
#print(dice_result)
mean = sum(dice_result)/len(dice_result)
print(mean)
median = statistics.median(dice_result)
print(median)
mode = statistics.mode(dice_result)
print(mode)
std_deviation = statistics.stdev(dice_result)
print(std_deviation)
first_std_deviation_start, first_std_deviation_end = mean - std_deviation , mean + std_deviation

list_of_data_within_1_standard_deviation = [result for result in dice_result if result > first_std_deviation_start and result < first_std_deviation_end]

print('{} % of data lies within one standard deviation'.format(len(list_of_data_within_1_standard_deviation)*100/len(dice_result)))

second_std_deviation_start, second_std_deviation_end = mean - std_deviation*2 , mean + std_deviation*2

list_of_data_within_2_standard_deviation = [result for result in dice_result if result > second_std_deviation_start and result < second_std_deviation_end]

print('{} % of data lies within two standard deviation'.format(len(list_of_data_within_2_standard_deviation)*100/len(dice_result)))

third_std_deviation_start, third_std_deviation_end = mean - std_deviation*3 , mean + std_deviation*3

list_of_data_within_3_standard_deviation = [result for result in dice_result if result > third_std_deviation_start and result < third_std_deviation_end]

print('{} % of data lies within two standard deviation'.format(len(list_of_data_within_3_standard_deviation)*100/len(dice_result)))

fig = ff.create_distplot([dice_result],['result'],show_hist= False)

fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17], mode = 'lines', name = 'MEAN')) 

# first standard deviation graph
fig.add_trace(go.Scatter(x = [first_std_deviation_start,first_std_deviation_start], y = [0,0.17], mode = 'lines', name = 'Standard Deviation 1'))
fig.add_trace(go.Scatter(x = [first_std_deviation_end,first_std_deviation_end], y = [0,0.17], mode = 'lines', name = 'Standard Deviation 1'))

# second standard deviation graph
fig.add_trace(go.Scatter(x = [second_std_deviation_start,second_std_deviation_start], y = [0,0.17], mode = 'lines', name = 'Standard Deviation 2'))
fig.add_trace(go.Scatter(x = [second_std_deviation_end,second_std_deviation_end], y = [0,0.17], mode = 'lines', name = 'Standard Deviation 2'))

# third standard deviation graph
fig.add_trace(go.Scatter(x = [third_std_deviation_start,third_std_deviation_start], y = [0,0.17], mode = 'lines', name = 'Standard Deviation 3'))
fig.add_trace(go.Scatter(x = [third_std_deviation_end,third_std_deviation_end], y = [0,0.17], mode = 'lines', name = 'Standard Deviation 3'))

fig.show()

