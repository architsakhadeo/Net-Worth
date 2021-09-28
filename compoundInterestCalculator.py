# Assuming monthly/annual investments are after taxes and after all expenses

initialInvestment = 0.0
monthlyInvestment = 2000.0
annualReturnPercentage = 15.0 #10.0 conservative
annualIncomeIncreasePercentage = 10.0 #8.0 conservative
annualInflationPercentage = 2.5
numberOfMonths = 20 * 12

monthlyReturnPercentage = (((1 + annualReturnPercentage/100)**(1.0/12)) - 1 ) * 100
monthlyInflationPercentage = (((1 + annualInflationPercentage/100)**(1.0/12)) - 1 ) * 100

# Variable inflation rate each year
annualInflationRate = 1

totalAmountInvested = 0.0
totalAmountInvestedAfterInflation = 0.0
totalValue = 0.0
totalValueAfterInflation = 0.0

listTotalValueMonthly = []
listTotalValueMonthlyAfterInflation = []
listTotalValueAnnual = []
listTotalValueAnnualAfterInflation = []

listTotalAmountInvestedMonthly = []
listTotalAmountInvestedMonthlyAfterInflation = []
listTotalAmountInvestedAnnual = []
listTotalAmountInvestedAnnualAfterInflation = []

# (num + 1) months have passed
totalAmountInvested = initialInvestment
totalAmountInvestedAfterInflation = initialInvestment
totalValue = initialInvestment
totalValueAfterInflation = initialInvestment



listTotalAmountInvestedMonthly.append(totalAmountInvested)
listTotalAmountInvestedMonthlyAfterInflation.append(totalAmountInvestedAfterInflation)
listTotalValueMonthly.append(totalValue)
listTotalValueMonthlyAfterInflation.append(totalValueAfterInflation)
listTotalAmountInvestedAnnual.append(totalAmountInvested)
listTotalAmountInvestedAnnualAfterInflation.append(totalAmountInvestedAfterInflation)
listTotalValueAnnual.append(totalValue)
listTotalValueAnnualAfterInflation.append(totalValueAfterInflation)



for num in range(numberOfMonths):
    
    totalAmountInvestedAfterInflation = totalAmountInvestedAfterInflation * (1 - monthlyInflationPercentage/100)
    totalAmountInvested += monthlyInvestment
    totalAmountInvestedAfterInflation += monthlyInvestment
    
    
    totalValue = totalValue * (1 + monthlyReturnPercentage/100)
    totalValue += monthlyInvestment
    totalValueAfterInflation = totalValueAfterInflation * (1 + monthlyReturnPercentage/100)
    totalValueAfterInflation = totalValueAfterInflation * (1 - monthlyInflationPercentage/100)
    totalValueAfterInflation += monthlyInvestment

    listTotalAmountInvestedMonthly.append(totalAmountInvested)
    listTotalAmountInvestedMonthlyAfterInflation.append(totalAmountInvestedAfterInflation)

    listTotalValueMonthly.append(totalValue)
    listTotalValueMonthlyAfterInflation.append(totalValueAfterInflation)

    if (num + 1) % 12 == 0:
        
        listTotalAmountInvestedAnnual.append(totalAmountInvested)
        listTotalAmountInvestedAnnualAfterInflation.append(totalAmountInvestedAfterInflation)

        listTotalValueAnnual.append(totalValue)
        listTotalValueAnnualAfterInflation.append(totalValueAfterInflation)


    # end of year
    if (num + 1) % 12 == 0:
        monthlyInvestment = monthlyInvestment * (1 + annualIncomeIncreasePercentage/100)
        
        # Variable inflation rate
        '''
        annualInflationPercentage = annualInflationPercentage * (1 + annualInflationRate/100)
        monthlyInflationPercentage = (((1 + annualInflationPercentage/100)**(1.0/12)) - 1 ) * 100
        '''

import matplotlib.pyplot as plt
colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

xAxis = [i+1 for i in range(numberOfMonths+1)] # +1 in range for initial investment, +1 in i+1 for starting from 1
plt.plot(xAxis, listTotalAmountInvestedMonthly, label='amount invested', color=colors[0])
plt.plot(xAxis, listTotalAmountInvestedMonthlyAfterInflation, label='amount invested after inflation', color=colors[0], linestyle='--')
plt.plot(xAxis, listTotalValueMonthly, label='total value', color=colors[1])
plt.plot(xAxis, listTotalValueMonthlyAfterInflation, label='total value after inflation', color=colors[1], linestyle='--')


xAxisTicks = []
for i in range(len(xAxis)):
    if (i+1) % 12 == 0:
        xAxisTicks.append(str(int(float(xAxis[i])/12)))
    else:
        xAxisTicks.append("")

plt.ylabel("$$$", rotation=0, labelpad=45)
plt.xlabel("Number of years")
plt.tight_layout()

plt.xticks(xAxis, xAxisTicks)
plt.legend()
plt.savefig("compoundInterestGraph.png", dpi=300)
plt.show()
