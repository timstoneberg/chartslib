from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt 

class DailyChart(self):

    def plot(target):
        ts = TimeSeries(key='API KEY', output_format='pandas')
        data, meta_data = ts.get_daily(symbol=target, outputsize='full')
        data['4. close'].plot()
        plt.title('Daily Series for the ' + target + ' stock')
        return plt.show()

class IntraDay(self):

    def plot(target):
        ts = TimeSeries(key='API KEY', output_format='pandas')
        data, meta_data = ts.get_intraday(symbol=target, interval='1min', outputsize='full')
        data['4. close'].plot()
        plt.title('Intraday Times Series for the ' + target + ' stock (1 min)')
        return plt.show()

