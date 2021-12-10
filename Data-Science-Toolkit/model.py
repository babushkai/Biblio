# モデルの用意
mods = {
    'LogisticRegression': LogisticRegression(C=0.01, random_state=42),

    'StandardScaler + LogisticRegression': Pipeline([('ss', StandardScaler()), ('model', LogisticRegression(C=0.01, random_state=42))]),

    'DecisonTree': DecisionTreeClassifier(random_state=42),

    'StandardScaler + DecisonTree': Pipeline([('ss', StandardScaler()), ('model', DecisionTreeClassifier(random_state=42))])
}

# モデルの学習と評価
results = {}
for mod_name, mod in mods.items():
    mod.fit(X_train, y_train)
    results[(mod_name, 'train')] = round(accuracy_score(y_train, mod.predict(X_train)), 3)
    results[(mod_name, 'valid')] = round(accuracy_score(y_test, mod.predict(X_valid)), 3)

# 結果の整理
pd.Series(results).unstack().iloc[[1, 3, 0, 2]]