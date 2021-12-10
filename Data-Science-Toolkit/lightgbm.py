class ModelExtractionCallback(object):

    def __init__(self):
        self._model = None

    def __call__(self, env):
        # Keep the reference of _CVBooster 
        self._model = env.model

    def _assert_called_cb(self):
        if self._model is None:
            # Return error when callback has not called
            raise RuntimeError('callback has not called yet')

    @property
    def boosters_proxy(self):
        self._assert_called_cb()
        # Return proxy object to Booster
        return self._model

    @property
    def raw_boosters(self):
        self._assert_called_cb()
        # Rerun the list of Booster
        return self._model.boosters

    @property
    def best_iteration(self):
        self._assert_called_cb()
        # Return boosting round when Early stopped
        return self._model.best_iteration




#  データセットを読み込む

X, y = df.values, output

# デモ用にデータセットを分割する
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=0.3,
                                                    random_state=42)

# LightGBM 用のデータセット表現に直す
lgb_train = lgb.Dataset(X_train, y_train)

# 学習済みモデルを取り出すためのコールバックを用意する
extraction_cb = ModelExtractionCallback()
callbacks = [
    extraction_cb,
]

# データセットを 5-Fold CV で学習する
lgbm_params = {
    "boosting":"dart", #dart(drop out trees) often performs better
    'objective': 'multiclass',
    'num_class': 3
}
# NOTE: 一般的には返り値の内容 (交差検証の結果) を確認する
lgb.cv(lgbm_params,
        lgb_train,
        num_boost_round=100,
        early_stopping_rounds=10,
        nfold=10,
        shuffle=True,
        stratified=True,
        #seed=42,
        callbacks=callbacks,
        verbose_eval=1
        )

# コールバックのオブジェクトから学習済みモデルを取り出す
proxy = extraction_cb.boosters_proxy
boosters = extraction_cb.raw_boosters
best_iteration = extraction_cb.best_iteration


# # 各モデルで個別に推論する場合
pred_dict={}
for i, booster in enumerate(boosters):
    y_pred_proba = booster.predict(X_test,
                                    num_iteration=best_iteration)
    y_pred = np.argmax(y_pred_proba, axis=1)
    pred_dict.setdefault(i, y_pred)
    accuracy = accuracy_score(y_test, y_pred) #正解率　全体に対して予測が当たった割合
    precision = precision_score(y_test, y_pred) #適合率 1と予測した中で実際にどれだけ1であったかの割合 ex)異常検知システムがアラートを出した回数のうち、実際に異常であった割合
    recall = recall_score(y_test, y_pred) #再現率 実際は1のデータのうち正しく1と予測できた割合 ex)病気の診断システムで再現率100%といった場合
    f1 =f1_score(y_test, y_pred)              #F1スコア 適合率と再現率の調和平均
    booster.feature_importances
    print(f'Model {i}\n accuracy: {accuracy},\n precision: {precision},\n recall: {recall},\n f1: {f1}')





model = lgb.LGBMClassifier(objective='binary',
                        num_leaves = 23,
                        learning_rate=0.1,
                        n_estimators=100,
                        boosting= "dart")

# 学習する
result = model.fit(X_train, y_train,
                   eval_set=[(X_test, y_test)],
                   eval_metric='multi_logloss'
                  )

# テストデータで予測する
y_pred = model.predict(X_test, num_iteration=result.best_iteration_)

# Accuracy を計算する
accuracy = sum(y_test == y_pred) / len(y_test)
print()
print(f"accuracy: {accuracy}")
知print(f"Precision: {precision_score(y_test, y_pred)}") #適合率 1と予測した中で実際にどれだけ1であったかの割合 ex)異常検システムがアラートを出した回数のうち、実際に異常であった割合
print(f"Recall: {recall_score(y_test, y_pred)}") #再現率 実際は1のデータのうち正しく1と予測できた割合 ex)病気の診断システムで再現率100%といった場合
print(f"F1: {f1_score(y_test, y_pred)}")             #F1スコア 適合率と再現率の調和平均

# importanceを表示する
importance = pd.DataFrame(model.feature_importances_, index=df.columns, columns=['importance'])
display(importance)
importance.plot.barh(figsize=(40,40))



## Optuna and Auto Hyperparameter tuning
import optuna.integration.lightgbm as lgb
from sklearn.model_selection import train_test_split

# Set data as LGB
train = lgb.Dataset(X_train, y_train)
test  = lgb.Dataset(X_test, y_test)

# Hyper-parameter search
params = {"objective": "binary",
          "metric": "auc"}


lgb_trained = lgb.train(params,
                        train, valid_sets=test,
                        early_stopping_rounds=100)

best_params = lgb_trained.params
print("Params:     ")
for key, value in best_params.items():
    print(f"{key}: {value}")