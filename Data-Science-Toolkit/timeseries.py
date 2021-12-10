

from statsmodels.tsa.stattools import adfuller
#DF検定の関数化
def test_stationarity(timeseries):
  
    # Determing rolling statistics
    # rollingを使って移動平均等の算出　Windowの幅を指定: 12(12ヶ月)
    rolmean = timeseries.rolling(window=12).mean() # 移動平均等
    rolstd     = timeseries.rolling(window=12).std()     # 分散の代わりに標準偏差をplot
    # rolstd = df["AirPassengers"].rolling(windows=12).var() 

    # Plot rolling statistics:
    orig = plt.plot(timeseries, color="blue", label="Original")
    mean = plt.plot(rolmean, color="red", label="Rolling Mean")
    std = plt.plot(rolstd, color="black", label="Rolling Std")
    plt.legend(loc="best")
    plt.title("Rolling Mean & Standard Deviation")
    plt.show(block=False)

    # Perform Dickey-Fuller test:
    print("Results of Dickey-Fuller Test:")
    # dftest = adfuller(timeseries, autolag="AIC")
    dftest = adfuller(timeseries)
    dfoutput = pd.Series(dftest[0:4], index=["Test Statistic", "p-value", "#Lags Used", "Number of Observations Used"])
    for key, value in dftest[4].items():
      dfoutput[f"Critical Value (key)"] = value
    print(dfoutput)





# Decomposing
#df["Global_active_power"] =  np.log(df["Global_active_power"])
from statsmodels.tsa.seasonal import seasonal_decompose

decomposition = seasonal_decompose(series, freq=30)

trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

plt.figure(figsize=(20, 6))
plt.subplot(411)
plt.plot(series[:1000], label='Original', color="red")
plt.legend(loc='best')
plt.subplot(412)
plt.plot(trend, label='Trend', color="orange")
plt.legend(loc='best')
plt.subplot(413)
plt.plot(seasonal,label='Seasonality', color="blue")
plt.legend(loc='best')
plt.subplot(414)
plt.plot(residual, label='Residuals', color="green")
plt.legend(loc='best')
plt.tight_layout()

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf #Plot ACF: 自己相関 AutoCorrelation

fig = plt.figure(figsize=(8, 8))
ax1 = fig.add_subplot(211)
fig = plot_acf(
   df_new['passengers_log'],    
   lags=48,                     # 出力するラグ数（ラグ0～48まで計41個の自己相関係数を出力）
   ax=ax1) #Plot PACF:偏自己相関
ax2 = fig.add_subplot(212)
fig = plot_pacf(df_new['passengers_log'], lags=48, ax=ax2) #Partial Autocorrelation
plt.tight_layout()