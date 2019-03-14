from abc import ABC, abstractmethod
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt 

class AbstractChart(ABC):
    type = "Generic Chart"

    @abstractmethod
    def __init__(self, type):
        self.type = type
        pass

    @abstractmethod
    def plot(self):
        pass

    @abstractmethod
    def save(self):
        pass

class DailyChart(AbstractChart):

    def __init__(self):
        super().__init__("daily")

    def plot(target):
        ts = TimeSeries(key='API KEY', output_format='pandas')
        data, meta_data = ts.get_daily(symbol=target, outputsize='full')
        data['4. close'].plot()
        plt.title('Daily Series for the ' + target + ' stock')
        plt.show()

    def save(target):
        ts = TimeSeries(key='API KEY', output_format='pandas')
        data, meta_data = ts.get_daily(symbol=target, outputsize='full')
        data['4. close'].plot()
        plt.title('Daily Series for the ' + target + ' stock')
        plt.savefig(target + "_daily.png")

class IntraDay(AbstractChart):

    def __init__(self):
        super().__init__("intraday")

    def plot(target):
        ts = TimeSeries(key='API KEY', output_format='pandas')
        data, meta_data = ts.get_intraday(symbol=target, interval='1min', outputsize='full')
        data['4. close'].plot()
        plt.title('Intraday Times Series for the ' + target + ' stock (1 min)')
        plt.show()

    def save(target):
        ts = TimeSeries(key='API KEY', output_format='pandas')
        data, meta_data = ts.get_intraday(symbol=target, interval='1min', outputsize='full')
        data['4. close'].plot()
        plt.title('Intraday Times Series for the ' + target + ' stock (1 min)')
        plt.savefig(target + "_intraday.png")

