# Reference

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/kwdaisuke/Biblio/main?labpath=Deep%2520Learning%2FTimeSeries)

http://www.mi.u-tokyo.ac.jp/consortium2/pdf/4-4_literacy_level_note.pdf 

https://machinelearningmastery.com/decompose-time-series-data-trend-seasonality

Hidden Markov Model
https://www.albert2005.co.jp/service/case/420.html

https://www.kaggle.com/code/thebrownviking20/everything-you-can-do-with-a-time-series

# Decision Tree of model Selection
```
1. Is the time series stationary?
    Yes:
        2. Does the time series have a trend?
            Yes:
                3. Does the time series have seasonality?
                    Yes: Use a seasonal decomposition method (e.g. seasonal decomposition using Loess (STL))
                    No: Use a trend-based method (e.g. simple linear regression)
            No:
                3. Does the time series have seasonality?
                    Yes: Use a seasonal decomposition method (e.g. seasonal decomposition using Loess (STL))
                    No: Use a method for stationary time series (e.g. exponential smoothing)
    No:
        2. Does the time series have a trend?
            Yes:
                3. Does the time series have seasonality?
                    Yes: Use a seasonal decomposition method (e.g. seasonal decomposition using Loess (STL)) and then use a trend-based method on the residuals
                    No: Use a trend-based method (e.g. simple linear regression) on the differenced data
            No:
                3. Does the time series have seasonality?
                    Yes: Use a seasonal decomposition method (e.g. seasonal decomposition using Loess (STL)) and then use a method for stationary time series (e.g. exponential smoothing) on the residuals
                    No: Use a method for stationary time series (e.g. exponential smoothing) on the differenced data
```